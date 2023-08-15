import functools
import time

def function():
    print("FUNCTION INVOKED!!!!!")
    
def logFunction(function):
    def log_wrapper():
        print("Invocation started")
        function()
        print("Invocation completed")
    return log_wrapper

logged_function = logFunction(function)
# logged_function()

def logFunction_With_Args(function):
    @functools.wraps(function)
    def log_wrapper(*args):
        print("Invocation started")
        function(*args)
        print("Invocation completed")
    return log_wrapper

@logFunction_With_Args
def add(x, y):
    print(f"Add result = {x + y}")

add(500, 500)

def record_time(function):
    @functools.wraps(function)
    def time_wrapper(*args, **kwargs):
        start = time.perf_counter()
        function(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"[{function.__name__}] Time Taken : {elapsed}")
        return time_wrapper

def do_something(no_times):
    for _ in range(no_times):
        sum([index ** 2 for index in range(1000)])

