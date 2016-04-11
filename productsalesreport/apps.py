from django.apps import AppConfig
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

api_settings = settings.GOOGLE_API


class ProductsalesreportConfig(AppConfig):
    name = 'productsalesreport'


def get_credentials():
    scopes = api_settings['default']['SCOPES'][0]
    keyfile = api_settings['default']['JSON_KEYFILE']
    return ServiceAccountCredentials.from_json_keyfile_name(
        keyfile, scopes)
