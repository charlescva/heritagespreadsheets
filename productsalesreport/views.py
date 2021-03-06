from django.shortcuts import render
from re import sub
from decimal import Decimal
from . import models
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def sheet_total(worksheet):
    list_from_worksheet = worksheet.get_all_values()
    total_sales = Decimal('0.00')
    row_iter = iter(list_from_worksheet)
    # Skip Header
    logger.debug(next(row_iter))
    for row in row_iter:
        if str(row[0]):
            logger.debug(row[0] + ' (SKU:' + row[1] + ') ' + row[4])
            total_sales += Decimal(sub(r'[^\d.]', '', row[4]))
    logger.debug("========================")
    logger.debug("Total Sales: $" + str(total_sales))
    return total_sales


def index(request):
    sheet_service = models.GoogleSheetsService.sheet_service
    sheetiter = iter(sheet_service.open('ProductSalesReport').worksheets())
    workbook_totals = {}
    workbook_total_sales = Decimal('0.00')
    for worksheet in sheetiter:
        worksheet_total = sheet_total(worksheet)
        workbook_total_sales += worksheet_total
        workbook_totals[str(worksheet.title)] = worksheet_total
    return render(request,
                  'index.html',
                  {'data': sorted(workbook_totals.items()),
                   'totalSales': workbook_total_sales})
