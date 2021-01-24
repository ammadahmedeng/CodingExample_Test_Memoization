# Create fake timer for threading mocking in testing
import time

from resettabletimer import FakeTimer


timeout_results_FakeTimer = None

def memoize(func, resolver, timeout):
    memoize_func_results = {}

    def timeout_memoize_results():
        global timeout_results_FakeTimer
        print("Hera")
        memoize_func_results.clear()
        timeout_results_FakeTimer = FakeTimer(timeout / 1000, timeout_memoize_results)
        timeout_results_FakeTimer.start()

    timeout_memoize_results()

    def func_wrapper(*args):
        # If resolver is provided, else first argument of the called function i.e. (timeResults)
        if resolver is not None:
            key = resolver(*args)
        else:
            key = args[0]

        if key in memoize_func_results.keys():
            memoize_func_value = memoize_func_results[key]

        # New key provided, hence called function again, cached value and return value via (memoize_func_value)
        # variable
        else:
            memoize_func_value = memoize_func_results[key] = func(*args)

        return memoize_func_value

    return func_wrapper

def timeResults(day, month):
    return time.time() + day + month

memoized = memoize(timeResults, lambda day, month: day + month, 5000)

results = memoized(2, 2)
print(results)  # 1611271663.9391403 # First Result

results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results

time.sleep(10)
timeout_results_FakeTimer.pass_time(5.1)
results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results
results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results
time.sleep(10)
results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results
timeout_results_FakeTimer.pass_time(5.1)
results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results

