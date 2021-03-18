import requests
import logging
from time import gmtime, strftime
from constants import *
from file_handler import create_dir, save_response_to_file_by_tqdm

logger = logging.getLogger(__name__)

downloadable_files = {'application/pdf': '.pdf', 'image/png': '.png',
         'image/jpeg': '.jpeg', 'video/x-msvideo': '.avi'}
data_path = "./../data/"

def print_method(response: requests.models.Response):
    logger.info(f"{requested_url} {response.url}")


def print_status(response: requests.models.Response):
    logger.info(status_code)
    if response.ok:
        logger.warning(f"{response.status_code} : {response.request.method} : {response.reason}")
    else:
        logger.critical(f"{response.status_code} : {response.request.method} : {response.reason}")


def print_header(response: requests.models.Response):
    logger.info(header_seperator)
    logger.info('\r\n'.join('{}: {}'.format(k, v)
                            for k, v in response.headers.items()))
    logger.info("")


def print_body(response: requests.models.Response):
    logger.info(body_seperator)
    logger.info(f"{response.text}")


def is_downloadable_file(response: requests.models.Response):
    c = response.headers[content_type]
    return c in downloadable_files.keys()



def download_body(response: requests.models.Response):
    create_dir(data_path)
    ct = response.headers[content_type]
    path = f'{data_path}{strftime("%Y-%m-%d-%H-%M-%S", gmtime()) + downloadable_files[ct]}'
    save_response_to_file_by_tqdm(path, response)

def handle_response(response: requests.models.Response):
    print_method(response)
    print_status(response)
    print_header(response)
    if (not is_downloadable_file(response)):
        print_body(response)
    else:
        download_body(response)
