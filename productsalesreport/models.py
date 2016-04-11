from django.db.models import Model
from . import apps
import gspread
import logging

# Create your models here.
# Get an instance of a logger
logger = logging.getLogger(__name__)


class GoogleSheetsService(Model):
    logger.debug("Connecting to Google Spreadsheets with Credentials...")
    sheet_service = gspread.authorize(apps.get_credentials())

