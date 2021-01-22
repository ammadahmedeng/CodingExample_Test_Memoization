import time


def memoize(func, resolver, timeout):
    memoize_func_results = {}

    def func_wrapper(*args):
        # If resolver is provided, else first argument of the called function i.e. (timeResults)
        if resolver is not None:
            key = resolver(*args)
        else:
            key = args[0]

        if key in memoize_func_results.keys():
            if ((time.time() - memoize_func_results[key][1]) * 1000) > timeout:
                # Timeout occur, delete old value and call original function to cache and return results
                del memoize_func_results[key]
                memoize_func_value = memoize_func_results[key] = func(*args), time.time()
            else:
                memoize_func_value = memoize_func_results[key]

        # New key provided, hence called function again, cached value and return value via (memoize_func_value) variable
        else:
            memoize_func_value = memoize_func_results[key] = func(*args), time.time()

        return memoize_func_value[0]

    return func_wrapper


def timeResults(day, month):
    return time.time() + day + month


memoized = memoize(timeResults, lambda day, month: day + month, 1000)

results = memoized(2, 2)
print(results)  # 1611271663.9391403 # First Result

results = memoized(2, 2)
print(results)  # 1611271663.9391403 # Cached Results

time.sleep(1.1)
results = memoized(2, 2)
print(results)  # 1611271665.0522864 # Timeout, so function called, new results
