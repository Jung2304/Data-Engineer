import pytest
from advanced_python import weather_check

@pytest.mark.parametrize("temp,expected", [
    (-5, "It's freezing outside!"),
    (10, "It's a bit chilly!"),
])
def test_weather_check(temp, expected):
    assert weather_check(temp) == expected

#< python -m pytest Python\test_weather_check.py (to run PyTest)