import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from script import addition


def test_add():
    assert addition(2, 3) == 5
