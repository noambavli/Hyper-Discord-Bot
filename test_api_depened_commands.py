import time

import weather_commands


def test_weather():
    #lowercase are intended because all messages converted to lowercase only at first
    commands_examples = [
        'what is the weather in new york',
        'what is the weather in london',
        'what is the weather in paris',
        'what is the weather in tokyo',

    ]

    for command in commands_examples:
        result = weather_commands.weather_command_answer(command)
        time.sleep(1)
        if not result.startswith("Location"):
            print(f"Failed for command: {command}, result: {result}")
        assert result.startswith("Location")





