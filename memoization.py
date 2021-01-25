# Create fake timer for threading timer mocking in test.py
from resettabletimer import FakeTimer


# FakeTimer object initialization for testing timeout to be used via test.py
timeout_results_FakeTimer = None

def memoize(func, resolver, timeout):
    # Memoize results with assigned Key
    memoize_func_results = {}

    # Multithreading with timeout to delete memoized results when timeout occurs
    def timeout_memoize_results():
        # Storing FakeTimer object in variable for faking timeout in test.py
        global timeout_results_FakeTimer

        # Delete memoized results after timeout and start of creation of object
        memoize_func_results.clear()

        # Timeout calling recursively until main program is terminated or object is created again
        timeout_results_FakeTimer = FakeTimer(timeout / 1000, timeout_memoize_results)
        timeout_results_FakeTimer.start()

    # Starting thread at the start of initialization of object
    timeout_memoize_results()

    def func_wrapper(*args):
        # If resolver is provided, else first argument of the memoized results function.
        if resolver is not None:
            key = resolver(*args)
        else:
            key = args[0]

        try:
            # If key already exist then return the memoize results
            if key in memoize_func_results.keys():
                memoize_func_value = memoize_func_results[key]

            # New key provided or memoized values timeout, hence call memoized results function again,
            # cached value and return value via (memoize_func_value) variable
            else:
                memoize_func_value = memoize_func_results[key] = func(*args)

        except (ValueError, TypeError):
            print("Invalid or empty values were give for the key, please enter correct values to be processed,")
            return None

        return memoize_func_value

    return func_wrapper
