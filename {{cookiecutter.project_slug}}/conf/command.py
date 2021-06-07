from functools import wraps

import os
import sys


def command_decorator(start_msg="Run command"):
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            print(start_msg)
            argv: str = " ".join([arg for i, arg in enumerate(sys.argv) if i > 0])
            func(argv, *args, **kwargs)

        return decorator

    return wrapper


@command_decorator(start_msg="Run test")
def run_pytest(argv: str):
    """
    Run pytest
    """
    os.system(f"dotenv --file .env.test run -- pytest {argv}")


@command_decorator(start_msg="Run coverage")
def check_coverage(argv: str):
    """
    Run coverage
    """
    os.system(f"dotenv --file .env.test run -- coverage run -m pytest {argv}")


@command_decorator(start_msg="Run Server")
def run_server(argv: str):
    """
    Run server
    """
    os.system(f"uvicorn app.main:app --reload {argv}")
