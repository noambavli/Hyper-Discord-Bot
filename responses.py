from random import choice ,randint
from english_answers import *
from hebrew_answers import *

def get_response(user_input: str, username: str) -> str:
    user_msg: str = user_input.lower()

    if user_msg.isascii() :
        answer = english_answers(user_msg,username)
        if answer:
            return answer

    if not user_msg.isascii() :
        answer = hebrew_answers(user_msg,username)
        if answer:
            return answer

    return None

