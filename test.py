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

    # Test Cases* (TC*) : One test case = One Branch Coverage flow

    # The total test coverage for TS1 is:
    # (Tested Branch / Total Branch) * 100 = 14 / 14 * 100 = 100% Branch Coverage
    ###############################################################################

    # Function for memoize value
    global varMemoizeValue

    @pytest.mark.it('Test Should Passed - Ensure to cover the branch when resolver is not None. '
                    'It will cover branch of Line 26 (if), Line 20 (else), Line 55 (else) and Line 59 (if).'
                    'Parameters: (1, 100, 1000)')
    def test_TS1_TC1(self):
        self.varReturnValue = 1

        # Assertion for checking return value, it should passed
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), 100, 1000) == 1

    @pytest.mark.it('Test Should Failed - Their is no expiry of old value, so it should failed. '
                    'It will cover remaining branch coverage of Line 59 (if - False condition) '
                    'as well as Line 59 Conditions (if-elif- (else)).'
                    'Parameters: (2, 100, 1000)')
    def test_TS1_TC2(self):
        self.varReturnValue = 2

        # Assertion for checking new value, but it will returned old value
        # thus failing the result
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), 100, 1000) == 2

    @pytest.mark.it('Test Should Passed - Ensure to cover the branch when resolver is not None and '
                    'memoize value timed out. Also pass tuples to cover branch coverage of function resolver().'
                    'It will cover remaining branch of Line 18 (if), Line 66 (elif).'
                    'Parameters: (2, (100, 101), 1000)')
    def test_TS1_TC3(self):
        self.varReturnValue = 2

        with freeze_time(datetime.datetime.now() + datetime.timedelta(milliseconds=1001)):
            # Assertion for checking new value, it will returned new value because old value expire
            # thus passing the result
            assert memoization.memoize(varMemoizeValue(self.varReturnValue), (100, 101), 1000) == 2

    @pytest.mark.it('Test Should Passed - Ensure to cover the branch when resolver is None. '
                    'It will cover remaining branch of Line 26 (if - False condition), Line 35 (if), Line 39 (if).'
                    'Parameters: (11, None, 1000)')
    def test_TS1_TC4(self):
        self.varReturnValue = 11

        # Assertion for checking return value, it should passed
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 11

    @pytest.mark.it('Test Should Passed - Although, their is no expiry of old value, but without resolver key,'
                    'the value will just be added in the List. '
                    'It will cover remaining branch of Line 39 (if - False condition) '
                    'as well as Line 39 Conditions (if-elif- (else)).'
                    'Parameters: (11, None, 1000)')
    def test_TS1_TC5(self):
        self.varReturnValue = 11

        # Assertion for checking new value, but it will returned old value but the test will be passed
        # because their is no resolver to match the Key in correspondence with the memoize value
        assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 11

    @pytest.mark.it('Test Should Passed - Ensure to cover the branch when resolver is None and memoize value timed out.'
                    'It will cover remaining branch of Line 46 (elif).'
                    'Parameters: (11, None, 1000)')
    def test_TS1_TC6(self):
        self.varReturnValue = 11

        with freeze_time(datetime.datetime.now() + datetime.timedelta(milliseconds=1001)):
            # Assertion for checking new value, it will returned new value because old value expire
            # thus passing the result
            assert memoization.memoize(varMemoizeValue(self.varReturnValue), None, 1000) == 11


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
