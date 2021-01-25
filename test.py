import os

import pytest

import memoization


# memoization-branch-coverage class for controlling memoize Test Plan (TP)
@pytest.mark.describe('memoization-branch-coverage')
class Test_memoization_branch_cov:
    ###############################################################################
    # Test Suite1 (TS1) : Branch Coverage

    # Reasons Documented in: Design_Rationale.pdf

    # The total test coverage for TS1 is:
    # (Tested Branch / Total Branch) * 100 = 4 / 4 * 100 = 100% Branch Coverage
    ###############################################################################

    @pytest.mark.it('Checking memoized function for testing memoized values.')
    def test_TS1_TC1(self):
        returnValue = 5

        # Function, which return value should be memoized
        testFunction = lambda key: returnValue

        # Setting up callback function
        memoized = memoization.memoize(testFunction, lambda key: key, 1000)

        # Assertion for checking return value via callback to be memoized, it should passed
        assert memoized("e1-51-01-efg") == 5

        returnValue = 10

        # Should returned memoized value as their is no timeout no testFunction call, hence, passed,
        # despite having new returnValue in the variable
        assert memoized("e1-51-01-efg") == 5

    @pytest.mark.it('This test will be failed as the timeout occur, hence, memoized value will timeout '
                    'and function will be called again to return new value.')
    def test_TS1_TC2(self):
        returnValue = 45

        # Function, which return value should be memoized
        testFunction = lambda key: returnValue

        # Setting up callback function
        memoized = memoization.memoize(testFunction, lambda key: key, 5000)

        # Assertion for checking return value via callback to be memoized, it should passed
        assert memoized("e1-51-01-efg") == 45

        returnValue = 55

        memoization.timeout_results_FakeTimer.pass_time(5)

        # Should returned new value to be memoized as their is timeout, hence failing with old value check
        assert memoized("e1-51-01-efg") == 45

    @pytest.mark.it('When resolver is not provided, the first argument should be memoized values key.')
    def test_TS1_TC3(self):
        args1 = 5
        args2 = 10
        args3 = 15

        # Function, which return value should be memoized
        testFunction = lambda args1, arg2, arg3: args1 + arg2 + arg3

        # Setting up callback function
        memoized = memoization.memoize(testFunction, None, 1000)

        # Assertion for checking return value via callback to be memoized, it should passed
        assert memoized(args1, args2, args3) == 30

        args1 = 5
        args2 = 20
        args3 = 30

        # Should returned memoized value as their is no timeout, hence passed despite having new returnValue
        assert memoized(args1, args2, args3) == 30

    @pytest.mark.it('The test will failed as the timeout occur, hence, new memoized value will be returned. '
                    'The first argument as memoized key because resolver is not provided.')
    def test_TS1_TC4(self):
        args1 = 5
        args2 = 10
        args3 = 15

        # Function, which return value should be memoized
        testFunction = lambda args1, arg2, arg3: args1 + arg2 + arg3

        # Setting up callback function
        memoized = memoization.memoize(testFunction, None, 5000)

        # Assertion for checking return value via callback to be memoized, it should passed
        assert memoized(args1, args2, args3) == 30

        args1 = 5
        args2 = 20
        args3 = 30

        memoization.timeout_results_FakeTimer.pass_time(5)

        # Should returned new value to be memoized as their is timeout, hence failing with old value check
        assert memoized(args1, args2, args3) == 30


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
