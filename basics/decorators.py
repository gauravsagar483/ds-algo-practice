import time
from datetime import datetime


def repeat(n):
    def execution_time(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(
                    f"Itr:{_+1}, Calling function: {func.__name__} at : {datetime.now()}"
                )
                result = func(*args, **kwargs)
                print(
                    f"Function {func.__name__} finished execution at : {datetime.now()}"
                )
            return result

        return wrapper

    return execution_time


@repeat(3)
def testing():
    print("Testing 1 2 3...")
    time.sleep(1)


testing()
