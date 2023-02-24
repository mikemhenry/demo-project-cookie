"""
Unit and regression test for the demo_project_cookie package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import demo_project_cookie


def test_demo_project_cookie_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", demo_project_cookie.__name__)
    assert "demo_project_cookie" in sys.modules


# Assert that a certain exception is raised
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
