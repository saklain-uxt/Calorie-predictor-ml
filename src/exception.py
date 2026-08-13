#The sys module in Python is a built-in module that gives you access to Python interpreter/system-related information and functionality.

# sys.exc_info() is a function in the sys module that returns a tuple containing information about the most recent exception caught by an except clause in the current thread. The tuple contains three values: the exception type, the exception value, and a traceback object.
import sys
from src.logger import logging


def error_handler(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_path = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_path,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        self.error_message = error_handler(
            error_message,
            error_detail
        )

    def __str__(self):
        return self.error_message