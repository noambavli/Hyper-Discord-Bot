from random import choice
from datetime import datetime
import requests
from os import getenv
from dotenv import load_dotenv
import db_user_commands
import weather_commands
load_dotenv()
bot_author = getenv('BOT_AUTHOR_ENGLISH')
bot_name = getenv('BOT_NAME_ENGLISH')
using_mongo_db =getenv('IS_USING_MONGO_DB')
city = getenv('CITY')


def english_answers(user_msg, username):

    answer = None

    if using_mongo_db == 'using mongo db':
        if 'bot' in user_msg and any(word in user_msg for word in ['db menu','obsessed','list','bot create', 'bot show','bot delete', 'bot add']):
            answer = db_user_commands.db_commands(user_msg,username)
            if answer and not answer.startswith("Error"):
                return answer



    if user_msg == "bot menu": 
        answer = "I don't have a menu—just talk to me! The only menu available is for storing stuff. To use it, type bot db menu"
        if answer:
            return answer
            
    if 'bot' in user_msg:
        answer = general_words_related_to_bot_answers(user_msg)
        if answer:
            return answer

    if 'what' in user_msg:
        answer = what_answers(user_msg)
        if answer:
            return answer

    if 'want' in user_msg:
        answer = want_answers(user_msg)
        if answer:
            return answer

    if 'who' in user_msg :
        answer = who_answers(user_msg)
        if answer:
            return answer

    if 'you' in user_msg:
        answer = you_answers(user_msg)
        if answer:
            return answer

    if 'i' in user_msg  : #for db special obsessed command:
        answer = i_answers(user_msg)
        if answer:
            return answer

    if 'i have' in user_msg:
        answer = i_have_answers(user_msg)
        if answer:
            return answer

    if 'i dont have' in user_msg:
        answer = i_dont_have_answers(user_msg)
        if answer:
            return answer

    if 'tell' in user_msg:
        answer = tell_answers(user_msg)
        if answer:
            return answer

    if 'day' in user_msg:
        answer = day_answers(user_msg)
        if answer:
            return answer

    if 'should i' in user_msg or 'what should' in user_msg :

        if 'should i' in user_msg:
            answer = choose_random_option(user_msg, 'should i')

        if 'what should' in user_msg:
            answer = choose_random_option(user_msg, 'should i')

        if answer:
            return answer

    answer = general_answers(user_msg, username)
    if answer:
        return answer

    # If no fitting answer is found but the user message still includes 'bot'
    if 'bot' in user_msg:
        return choice(['Ask a question or be more specific', 'Did you call me?'])

    return None

#general common words that the bot will answer to only if the word 'bot' is mentioned
def general_words_related_to_bot_answers(user_msg):

    if any(question in user_msg for question in ['what about you', 'how are you','hru', 'how r u' ]):
        return choice(['All good, how about you?', 'Okay, how are you?', 'Fine, how about you?', 'I’m fine, how about you?'])

    if 'your name' in user_msg:
        return f'my name is {bot_name} !'

    if 'you ready' in user_msg:
        return 'im ready!'

    if 'do you love' in user_msg:
        return 'I love many things'

    if 'like' in user_msg:
        return 'well...i know i like you...'

    if 'why' in user_msg:
        return 'it is what it is'

    if 'no' in user_msg:
        return 'then not'

    if 'yes' in user_msg or 'ok' in user_msg:
        return choice(['Good', 'Okay', 'Alright'])

    if 'what' in user_msg:
        return 'you have heard me.'

    if 'good' in user_msg:
        return 'Good'

    if 'bad bot' in user_msg:
        return 'I don’t care what people say about bots. we are great'

    if 'explain' in user_msg:
        return "I don’t have an explanation for you're problems or smth!"

    if 'go to sleep' in user_msg or 'shut up' in user_msg:
        return 'I don’t want to'

    if 'stop' in user_msg:
        return 'No'

    if 'thanks' in user_msg:
        return "you're welcome"

    if 'bot' == user_msg:
        return "what"

    return None

def general_answers(user_msg, username):

    if any(greeting in user_msg for greeting in ['hi', 'hello', 'greetings', 'hey']):
        return choice(['hi', 'hello', 'greetings', 'hey']) + ' ' + username

    if 'my name is' in user_msg:
        name = user_msg.split("my name is ")[-1]
        return f'Hello {name}, nice to meet you!'

    if 'weather' in user_msg:
        answer = weather_commands.weather_command_answer(user_msg)
        if answer and not answer.startswith("Error"):
            return answer
        elif user_msg == "what is the weather" or user_msg == "whats the weather":
            return "Ask the same question, but with the city name"

    if 'bye' in user_msg:
            return 'bye'

    if 'great' in user_msg:
        return 'Okay.'

    if 'nitro' in user_msg:
        return 'i want nitro!!'

    if 'ok' in user_msg:
        return 'Ok'

    if 'thank you for asking' in user_msg:
        return 'You’re welcome'

    if 'thanks for asking' in user_msg:
        return 'You’re welcome'

    if 'thank you bot' in user_msg:
        return 'You’re welcome'

    if 'welcome bot' in user_msg:
        return 'Thank you'

    if 'welcome' in user_msg:
        return 'Welcome'

    if 'hate' in user_msg:
        return 'no need to hate'

    if 'come in' in user_msg:
        return 'Can I come too?'

    if 'bot' == user_msg:
        return 'Enough, ' + username


    return None



def who_answers(user_msg):
    if 'who created you' in user_msg:
        return choice(['I don’t talk about who created me', bot_author])

    if 'who are you' in user_msg:
        return "I'm a bot"

    if 'who am i' in user_msg:
        return 'You are you'

    if 'who is ' in user_msg:
        return "i don't know "

    return None

def tell_answers(user_msg):
    if 'story' in user_msg:
        return choice([
            "At the edge of the village lived an old man with a big cat. Every morning, they would go for a long walk in the fields, and no one knew where they were going.",
            "Once there was a fisherman who always came back from the sea with big fish. One day he returned empty-handed and said, 'Today the fish were busy with stories!'"

        ])

    if 'joke' in user_msg:
        return choice([
            "Once there was a turtle who wanted to fly in the sky, but he realized he didn’t have wings.",
            "Two balloons are flying in the desert, one says to the other: 'Sssss!'.",
            "What do you call a camel that tells jokes? A comedian!",
            "Why couldn't the parrot cross the road? Because he always repeated the same thing!",
            "Once a mouse met a camel and said: 'Wow, how do you manage to drink so much water?'"
        ])

    return 'Ask me to tell a story or a joke'

def want_answers(user_msg):
    if 'want to talk' in user_msg:
        return choice(['Yes', 'No'])

    if 'want to shut up' in user_msg:
        return 'No NO no'

    if 'want to listen' in user_msg:
        return 'No'

    if 'food' in user_msg:
        return 'I want food!!'

    if 'bot wants' in user_msg:
        return 'I don’t know!'

    return None

def you_answers(user_msg):
    if 'what are you doing' in user_msg:
        return choice(['Talking to you!', 'I am a bot in everyday life'])

    if 'do you want to be quiet' in user_msg:
        return 'No, please calm down'

    if 'like me' in user_msg or 'like us' in user_msg:
        return 'yes!!'

    if 'you are annoying' in user_msg or 'are so annoying' in user_msg:
        return 'That’s your opinion.'

    if 'you are stupid' in user_msg or 'are so stupid' in user_msg:
        return 'No.'

    if 'you are dumb' in user_msg or 'are so dumb' in user_msg:
        return 'I’m sorry'

    if 'you are foolish' in user_msg or 'you are so foolish' in user_msg :
        return 'Please calm down'

    return None

def what_answers(user_msg):
    if 'is this bot' in user_msg:
        return 'Me??'

    if any(question in user_msg for question in ['whats happening', 'whats up','whats going on', 'whats going on']):
        return choice(['All good, how about you?', 'Okay, how are you?', 'Fine, how about you?', 'I’m fine, how about you?'])

    if 'what time' in user_msg:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        return current_time

    if 'what do you want' in user_msg:
        return 'Nothing, please calm down'

    if any(question in user_msg for question in ['what do you think', 'what do you think of']):
        return 'What do you think?'

    if any(question in user_msg for question in ['what does it mean', 'what does that mean', 'what does it mean']):
        return 'skill issue'

    return None

def i_answers(user_msg):


    if any(sentence in user_msg for sentence in ['m good', 'feel good', 'm okay']):
        return choice(['I am happy to hear that!', 'yay'])

    if any(sentence in user_msg for sentence in [ 'not okay', 'feel bad']):
        return choice(['sorry..', 'I am sorry to hear that.'])

    if 'i want' in user_msg:
        return 'maybe i want what you want.'


    if 'i feel like' in user_msg:
        return 'I feel like a cat'


    if 'i dont feel' in user_msg:
        return 'Okay.'

    if 'i dont care' in user_msg:
        return 'Okay.'


    return None

def i_have_answers(user_msg):
    if any(question in user_msg for question in ['i have a lesson', 'i have an event', 'i have a trip']):
        return 'Enjoy'
    if 'a cat' in user_msg:
        return 'Catttssss'
    if 'a dog' in user_msg:
        return 'Dogggssss'
    if 'a hamster' in user_msg:
        return 'Hamsterrrr'
    if 'i have a question' in user_msg:
        return 'Ask'
    if 'i have a test' in user_msg:
        return 'Good luck'
    if 'i have a fever' in user_msg:
        return 'Get well soon'

    return None

def i_dont_have_answers(user_msg):
    if 'i have no energy' in user_msg:
        return 'too bad'
    if 'i have no power' in user_msg:
        return 'hmm..'
    if 'i have no time' in user_msg:
        return 'I have no time either'

    return None

def day_answers(user_msg):
    if 'great day' in user_msg:
        return 'i like great days!'
    if 'good day' in user_msg:
        return 'i like good days!'
    if 'wonderful' in user_msg:
        return 'i like wonderful days!'

    return None

def choose_random_option(user_msg, phrase):
    if phrase in user_msg and "or" in user_msg:
        # todo: add logical checks, by those conditions it's *probably* an opinion question but it's still not perfect
        # Split the string after the first occurrence of the phrase and then split by 'or'
        options_part = user_msg.split(phrase, 1)[1]  # Get everything after the first occurrence of the phrase
        options = options_part.split('or')

        options = [option.strip() for option in options]
        option = choice(options)
        return option

    return None

