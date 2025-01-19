import pytest
from app import myapp

def test_my_function(mocker):
    mocker.patch("test_app.test_function", return_value=100)
    result = myapp.some_func()
    assert result == 100
