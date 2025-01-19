import sys
import os
sys.path.append("/Users/saurabhsaran/Documents/git/pythonbasics/testing/app/")

import myapp
import pytest

def test_some_func(mocker):
    mocker.patch("myapp.some_func", return_value=100)
    result = myapp.some_func()
    assert result == 100