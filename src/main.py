from argumentParser import get_args
from argsmapper import get_request
from exceptions import Error
import coloredlogs, logging

logging.basicConfig(
    level=logging.DEBUG,
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)
logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(levelname)s %(message)s', logger=logger)

if __name__ == "__main__":
    # logger.debug("this is a debugging message")
    # logger.info("this is an informational message")
    # logger.warning("this is a warning message")
    # logger.error("this is an error message")
    # logger.critical("this is a critical message")
    args = get_args()
    try:
        request = get_request(args)
        # print(request.make_request().text)
    except Error as e:
        logger.error(e.message)
