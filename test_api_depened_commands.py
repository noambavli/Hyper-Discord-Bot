import time

import weather_commands


def test_weather():
    commands_examples = [
        'what is the weather in new york',
        'what is the weather in chicago',
        'what is the weather in san francisco',
        'what is the weather in london',
        'what is the weather in paris',
        'what is the weather in tokyo',
        'what is the weather in sydney',
        'what is the weather in berlin',
        'what is the weather in madrid',
        'what is the weather in rome',
        'what is the weather in seoul',
        'what is the weather in dubai',
        'what is the weather in moscow',
        'what is the weather in beijing',
        'what is the weather in bangkok',
        'what is the weather in cape town',
        'what is the weather in vancouver',
        'what is the weather in toronto',
        'what is the weather in mexico city',
        'what is the weather in los angeles',
        'what is the weather in barcelona',
        'what is the weather in amsterdam',
        'what is the weather in stockholm',
        'what is the weather in rio de janeiro',
        'what is the weather in montreal',
        'what is the weather in melbourne',
        'what is the weather in toronto',
        'what is the weather in buenos aires'
    ]

    for command in commands_examples:
        result = weather_commands.weather_command_answer(command)
        time.sleep(1)
        if not result.startswith("Location"):
            print(f"Failed for command: {command}, result: {result}")
        assert result.startswith("Location")





