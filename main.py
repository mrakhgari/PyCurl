from request import Request
from argumentParser import get_args
from argsmapper import get_request, Error

if __name__ == "__main__":
    args = get_args()
    try:
        request = get_request(args)
        print(request.make_request().text)
    except Error as e:
        print(str(e.message))
