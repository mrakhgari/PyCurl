from argument_parser import get_args
from arg_mapper import get_request
from exceptions import Error
from response_handler import handle_response
import coloredlogs
import logging

logging.basicConfig(
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s', logger=logger)

if __name__ == "__main__":
    args = get_args()
    try:
        request = get_request(args)
        response = request.make_request()
        handle_response(response)
    except Error as e:
        logger.error(e.message)
