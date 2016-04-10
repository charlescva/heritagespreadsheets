from django.shortcuts import render

#  Charlie's Python for Kris' Google Sheets API.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from re import sub
from decimal import Decimal


def sheet_total(worksheet):
    list_from_worksheet = worksheet.get_all_values()
    total_sales = Decimal('0.00')
    row_iter = iter(list_from_worksheet)
    # Skip Header
    print(next(row_iter))

    for row in row_iter:
        if str(row[0]):
            print(row[0] + '(SKU:' + row[1] + ')' + row[4])
            total_sales += Decimal(sub(r'[^\d.]', '', row[4]))

    print("========================")
    print("Total Sales: $" + str(total_sales))
    return total_sales


def get_credentials():
    scopes = ['https://spreadsheets.google.com/feeds']
    return ServiceAccountCredentials.from_json_keyfile_name(
        'heritageSpreadsheets.json', scopes)


def index(request):
    sheet_service = gspread.authorize(get_credentials())
    sheetiter = iter(sheet_service.open('ProductSalesReport').worksheets())
    workbook_totals = {}
    for worksheet in sheetiter:
        workbook_totals[str(worksheet.title)] = sheet_total(worksheet)

    return render(request, 'index.html', {'data': sorted(workbook_totals.items())})
