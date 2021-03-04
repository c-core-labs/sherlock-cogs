import timeit
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def timer(function):
    def function_wrapper(*args, **kwargs):
        log.info(f"Beginning '{function.__name__}'")
        start_time = timeit.default_timer()
        result = function(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        log.info(f"Function '{function.__name__}' took {elapsed} seconds to complete.")

        return result

    return function_wrapper


if __name__ == '__main__':
    pass
