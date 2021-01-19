import os

import datetime
from freezegun import freeze_time

import pytest

import memoization

# Global function for memoize value which is called through each test cases and test coverage
# Postional Argument (memoizeValue) with lambda anonymous function
varMemoizeValue = lambda memoizeValue: memoizeValue

# memoization-statement-coverage class for controlling memoize Test Plan (TP)
@pytest.mark.describe('memoization-statement-coverage')
class Test_memoization_stat_cov:
    ###############################################################################
    # Test Suite1 (TS1) : Statement Coverage

    # To ensure maximum number of statements in the test code is at least tested once.
    # Doesn't need to do Branch Coverage here,
    # as it will be automatically cover in Test Suite2,
    # which is Path Coverage.

    # Test Cases* (TC*) : One test case = One statement coverage flow

    # The total test coverage for TS1 is:
    # (Tested Lines / Total Lines) * 100 =
    ###############################################################################

    # Function for memoize value
    global varMemoizeValue

    @pytest.mark.it('Test Should Passed - Ensure to cover the path when resolver is not None. Parameters: (1, 100, 1000)')
    def test_TS1_TC1(self):
        self.varReturnValue = 1

        # Assertion for checking return value, it should passed
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), 100, 1000) == 1

    @pytest.mark.it('Test Should Failed - Their is no expiry of old value, so it should failed. Parameters: (2, 100, 1000)')
    def test_TS1_TC2(self):
        self.varReturnValue = 2

        # Assertion for checking new value, but it will returned old value
        # thus failing the result
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), 100, 1000) == 2


    @pytest.mark.it('Test Should Passed - Ensure to cover the path when resolver is not None and memoize value timed '
                    'out. Also pass tuples to cover statement coverage of function resolver(). '
                    'Parameters: (2, (100, 101), 1000)')
    def test_TS1_TC3(self):
        self.varReturnValue = 2

        with freeze_time(datetime.datetime.now() + datetime.timedelta(milliseconds=1001)):
            # Assertion for checking new value, it will returned new value because old value expire
            # thus passing the result
            assert memoization.memoize(varMemoizeValue(self.varReturnValue), (100, 101), 1000) == 2

    @pytest.mark.it('Test Should Passed - Ensure to cover the path when resolver is None. Parameters: (11, None, 1000)')
    def test_TS1_TC4(self):
        self.varReturnValue = 11

        # Assertion for checking return value, it should passed
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 11

    @pytest.mark.it('Test Should Failed - Their is no expiry of old value, so it should failed. Parameters: (11, None, 1000)')
    def test_TS1_TC5(self):
        self.varReturnValue = 11

        # Assertion for checking new value, but it will returned old value
        # thus failing the result
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 11

    @pytest.mark.it('Test Should Passed - Ensure to cover the path when resolver is None and memoize value timed out. Parameters: (12, None, 1000)')
    def test_TS1_TC6(self):
        self.varReturnValue = 12

        with freeze_time(datetime.datetime.now() + datetime.timedelta(milliseconds=1001)):
            # Assertion for checking new value, it will returned new value because old value expire
            # thus passing the result
            assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 12


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
