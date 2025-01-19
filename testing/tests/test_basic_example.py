import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

from app import myapp
import pytest

def test_some_func(mocker):
    mocker.patch("app.myapp.some_func", return_value=100)
    result = myapp.some_func()
    assert result == 100