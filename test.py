import os

# Faking timeout for the expiration of memoized stored value
import datetime
from freezegun import freeze_time

import pytest

import memoization

# Global function for memoize value which is called through each test cases and test coverage
# Postional Argument (memoizeValue) with lambda anonymous function
varMemoizeValue = lambda memoizeValue: memoizeValue

# memoization-branch-coverage class for controlling memoize Test Plan (TP)
@pytest.mark.describe('memoization-branch-coverage')
class Test_memoization_branch_cov:
    ###############################################################################
    # Test Suite1 (TS1) : Branch Coverage

    # Reasons Documented in: Design_Rationale.pdf

    # Test Cases* (TC*) : One test case = One Branch Coverage

    # The total test coverage for TS1 is:
    # (Tested Branch / Total Branch) * 100 =
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
