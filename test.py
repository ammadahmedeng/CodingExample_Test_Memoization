import memoization
import pytest
import os
import sys


# If the function is called then the test result are logged in (memoizationLog) folder;
# instead of showing on console
def log_Memoization_Test_Results(logFileName):
    logTestResults = open(os.path.join(os.getcwd(), "logMemoization", logFileName + ".log"), "a")
    sys.stdout = logTestResults


# memoization class for controlling memoize Test Plan (TP)
@pytest.mark.describe('memoization')
class Test_memoization:
    # Memoized test (failed or passed) result logged
    log_Memoization_Test_Results("logFailedTC")

    # Test Suite1 (TS1) : Statement Coverage
    # Test Cases* (TC*) : One test case = One statement coverage
    @pytest.mark.it('Should failed in attempt of doing memoize due to missing function')
    def test_TS1_TC1(self):
        # Initial test with BDD/TDD -> Fail - Pass - Scenario

        varReturnValue = 5

        # Postional Argument (key) with lambda anonymous function
        varMemoizeValue = lambda key: varReturnValue

        # Use assertion for returned value check with the Key passed for failed or passed TC scenario
        memoized = memoization.memoize(varMemoizeValue, lambda key: key, 1000)
        assert memoized('c544d3ae-a72d-4755-8ce5-d25db415b776') == 5


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
