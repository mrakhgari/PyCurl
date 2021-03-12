from argumentParser import get_args
from argsmapper import get_request
from exceptions import Error
import coloredlogs, logging

import requests
logging.basicConfig(
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(levelname)s %(message)s', logger=logger)

if __name__ == "__main__":
    args = get_args()
    try:
        request = get_request(args)
        print(request.make_request().text)
    except Error as e:
        logger.error(e.message)
