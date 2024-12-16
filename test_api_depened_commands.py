# test_example.py

# Importing the function to be tested
from  english_answers import *


# Test function
def test_weather():
    result = weather_answers()
    assert result.startswith("Location:"), result



