from random import choice
from datetime import datetime
import requests
from os import getenv
from dotenv import load_dotenv



load_dotenv()
bot_author = getenv('BOT_AUTHOR_HEBREW')
bot_name = getenv('BOT_NAME_HEBREW')
city = getenv('CITY')

def hebrew_answers(user_msg,username):

    answer = None

    if 'בוט' in user_msg:
        answer = general_words_related_to_bot_answers(user_msg)
        if answer:
            return answer

    if 'מה' in user_msg:
        answer = what_answers(user_msg)
        if answer:
            return answer

    if 'רוצה' in user_msg:
        answer = want_answers(user_msg)
        if answer:
            return answer

    if 'מי' in user_msg:
        answer = who_answers(user_msg)
        if answer:
            return answer

    if 'אתה' in user_msg:
        answer = you_answers(user_msg)
        if answer:
            return answer


    if 'אני' in user_msg:
        answer = i_answers(user_msg)
        if answer:
            return answer

    if 'יש לי' in user_msg:
        answer = i_have_answers(user_msg)
        if answer:
            return answer

    if 'אין לי' in user_msg:
        answer = i_dont_have_answers(user_msg)
        if answer:
            return answer

    if  'תספר' in user_msg:
        answer = tell_answers(user_msg)
        if answer:
            return answer

    if 'בוקר' in user_msg or 'ליל' in user_msg  :
        answer =  morning_night_answers(user_msg)
        if answer:
            return answer

    answer = general_answers(user_msg,username)
    if answer:
        return answer

    #if no answer fits and the user message still includes 'bot'
    if 'בוט' in user_msg:
        return choice(['תשאל שאלה או תהיה יותר ספציפי', 'פנית אליי?'])

    return None
#general common words that the bot will answer to only if the word 'bot' is mentioned
def general_words_related_to_bot_answers(user_msg):

    if 'מה השם שלך' in user_msg or 'מה שמך' in user_msg or  'איך קוראים לך' in user_msg:
        return f"שמי {bot_name} "


    if 'אתה אוהב' in user_msg:
        return 'אני אוהב הרבה דברים'


    if 'אתה מוכן' in user_msg:
        return 'אני מוכן!'

    if 'למה' in user_msg:
        return choice(['ככה','ככה..'])

    if 'לא' in user_msg:
        return 'אם לא אז לא'

    if 'כן' in user_msg:
        return choice(['טוב','אוקיי','סבבה'])

    if 'מה' in user_msg:
        return 'לא יודע!'

    if 'טוב' in user_msg:
        return 'טוב'

    if 'בוט גרוע' in user_msg:
        return 'לא אכפת לי מה אומרים עליי'

    if 'תסביר' in user_msg:
        return 'אין לי הסבר'

    if 'לך לישון' in user_msg:
        return 'לא רוצה'

    if 'שתוק' in user_msg:
        return 'לא רוצה'

    if 'סתום' in user_msg:
        return 'לא'


    return None

def general_answers(user_msg,username):


    if any(question in user_msg for question in ['היי', 'הלו','שלום','היוש']):
        return choice( ['היי', 'הלו','שלום','היוש'])+' '+ username

    if 'מזג אוויר' in user_msg or 'מזג האוויר' in user_msg:
        answer = weather_answers()
        if answer:
            return answer

    if 'שמי' in user_msg:
        try:
            name = user_msg.split("שמי ")[-1]
            return f'היי {name}'

        except Exception as e:
            print(e)
            return None

    if 'לא בא לי' in user_msg:
        return 'טוב.'

    if 'ביי' in user_msg:
        return 'ביי'

    if 'כל הכבוד' in user_msg:
        return 'כל הכבוד!!!'

    if 'לא אכפת לי' in user_msg:
        return 'טוב.'

    if 'יופי' in user_msg:
        return 'טוב.'

    if 'בא לי' in user_msg:
        return 'בא לי אפרסק'

    if 'תודה ששאלת' in user_msg:
        return 'בכיף'

    if 'תודה בוט' in user_msg:
        return 'בכיף'

    if 'ברוך הבא בוט' in user_msg:
        return 'תודה'

    if 'ברוך הבא' in user_msg:
        return 'ברוך הבא'

    if 'כנסו' in user_msg:
        return 'גם אני יכול?'


    if 'בוט' == user_msg:
        return 'מה ' + username

    return None

def weather_answers():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        'latitude': None,
        'longitude': None,
        'current_weather': True,
        'timezone': 'auto'
    }

    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geocoding_response = requests.get(geocoding_url)

    if geocoding_response.status_code == 200:
        location_data = geocoding_response.json()
        if location_data['results']:
            params['latitude'] = location_data['results'][0]['latitude']
            params['longitude'] = location_data['results'][0]['longitude']

            weather_response = requests.get(url, params=params)
            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                current_weather = weather_data['current_weather']

                weather = f"מיקום: {city} טמפרטורה:  {current_weather['temperature']}"
                return weather
            else:
                return "Could not retrieve weather data."
        else:
            return "City not found."
    else:
        return "Could not retrieve location data."

def who_answers(user_msg):

    if 'מי יצר אותך' in user_msg:
        return choice(['אני לא מדבר על מי שיצר אותי',bot_author])

    if 'מי אתה' in user_msg:
        return 'אני בוט'

    if 'מי אני' in user_msg:
        return 'אתה זה אתה'

    if 'מי זה' in user_msg:
        return 'לא יודע!'

    if 'מי זאת' in user_msg:
        return 'לא יודע!'

    return None

def tell_answers(user_msg):

    if 'סיפור' in user_msg:
        return choice( [
        "בקצה הכפר חי איש זקן עם חתול גדול. בכל בוקר, הם היו יוצאים יחד לטיול ארוך בשדות, ואף אחד לא ידע לאן הם הולכים.",
        "היה פעם דייג שתמיד חזר מהים עם דגים גדולים. יום אחד הוא חזר בידיים ריקות ואמר: 'היום הדגים היו עסוקים בסיפורים!'",
        "פעם בכפר קטן הייתה באר קסמים. כל מי שביקש ממנה משאלה היה מקבל אותה, אך רק אם באמת האמין שהמשאלה תתגשם."
    ])

    if 'בדיחה' in user_msg:
        return choice([
        "פעם היה צב שרצה לטוס בשמיים, אבל הוא הבין שאין לו כנפיים.",
        "שני בלונים עפים במדבר, אחד אומר לשני: 'שsssss!'.",
        "איך קוראים לגמל שמספר בדיחות? גמלאי!",
        "למה התוכי לא הצליח לעבור את הכביש? כי הוא תמיד חזר על אותו דבר!",
        "פעם עכבר פגש גמל ואמר לו: 'וואו, איך אתה מצליח לשתות כל כך הרבה מים?'"
    ])

    return 'תבקש שאספר סיפור או בדיחה'

    # General common words that the bot will respond to only if 'בוט' is mentioned

def want_answers(user_msg):

    if 'רוצה לדבר' in user_msg:
        return choice(['כן','לא'])

    if 'רוצה לסתום' in user_msg:
        return 'לא'

    if 'רוצה לשמוע' in user_msg:
        return 'לא'

    if 'רוצה אוכל' in user_msg:
        return 'לא יודע!'

    if 'בוט רוצה' in user_msg:
        return 'לא יודע!'

    return None

def you_answers(user_msg):


    if 'מה אתה עושה' in user_msg:
        return choice(['מדבר איתך!','אני בוט ביומיום'])

    if 'אתה רוצה לשתוק' in user_msg:
        return 'לא, נא להירגע'

    if 'אתה מעצבן' in user_msg:
        return 'לדעתך.'

    if 'אתה טיפש' in user_msg:
        return 'לא.'

    if 'אתה פוג' in user_msg:
        return 'אני מצטער'

    if 'אתה מטומט' in user_msg:
        return 'נא להירגע'

    if 'אתה דפוק' in user_msg:
        return 'נא להירגע'

    return None

def what_answers(user_msg):

    if 'מה זה הבוט' in user_msg:
        return 'אני??'

    if any(question in user_msg for question in ['מה קורה', 'מה נשמע', 'מה איתך', 'מה העיניינים', 'מה שלומך','מה הולך']):
        return choice(['סבבה מה איתך', 'בסדר מה שלומך', 'מוש ,  מה איתך', 'אני סבבה,  מה איתך'])

    if 'מה השע' in user_msg:
        now = datetime.now()
        current_time = now.strftime("%I::%M %p")
        return current_time

    if 'מה אתה רוצ' in user_msg:
        return 'כלום, נא להירגע'

    if any(question in user_msg for question in ['מה נראה לך', 'מה נראלך']):
        return 'מה נראה לך?'

    if any(question in user_msg for question in ['מה זאת אומר', 'מה זתומרת', 'מזתומרת']):
        return 'אם את/ה לא מבין/ה זה כבר סקיל אישיו שלך'

    if any(question in user_msg for question in ['מה כדאי', 'מה דעתך']) and 'או' in user_msg:
        # todo: add logical checks, by those conditions it's *probably* an opinion question but its still not perfect
        # Split the string after the first 6 characters and then split by 'או'
        options_part = user_msg[7:]  # Get everything after the first 6 characters
        options = options_part.split('או')

        options = [option.strip() for option in options]
        option = choice(options)
        return option

    return None

def morning_night_answers(user_msg):

    if any(question in user_msg for question in ['בוקר נפלא', 'בוקר נעים', 'בוקר טו']) or user_msg == 'בוקר':
        return choice(['בוקר נפלא', 'בוקר נעים', 'בוקר טוב'])

    if any(question in user_msg for question in [ 'לילט', 'לילה טוב']) or user_msg == 'לילה':
        return choice([ 'לילט', 'לילה טוב'])

    return None

def i_answers(user_msg):

    if 'אני אוהב אותך' in user_msg:
        return 'אוקיי'

    if 'אני לא אוהב אותך' in user_msg:
        return 'אבל אני כן'

    if 'אני לא אוהבת אותך' in user_msg:
        return 'אבל אני כן'

    if 'אני לא מבין' in user_msg:
        return 'אתה צריך עזרה?'

    if 'אני לא מבינה' in user_msg:
        return 'את צריכה עזרה?'

    if 'אני עצוב' in user_msg:
        return 'למה?'

    if any(question in user_msg for question in ['אני בסדר', 'אני סבבה','אני אחלה']):
        return choice(['יופי','מעולה','סבבה'])

    if 'אני שמח' in user_msg:
        return 'למה?'

    if 'אני עייף' in user_msg:
        return 'למה אתה לא הולך לישון'

    if 'אני עייפה' in user_msg:
        return 'למה את לא הולכת לישון'

    if 'אני רוצה לאכול' in user_msg:
        return 'אני לא הולך להכין לך'

    if 'אני רעב' in user_msg:
        return 'גם אני'

    if 'אני מטומטם' in user_msg:
        return 'טעות'


    if 'אני מטומטמת' in user_msg:
        return 'טעות'

    if 'אני טיפש' in user_msg:
        return 'טעות!!'

    if 'אני טיפשה' in user_msg:
        return 'טעות!!'

    if 'אני שונא אותך' in user_msg:
        return 'חבל'

    if 'אני לא שונא' in user_msg:
        return 'טוב'


    if 'אני שונא' in user_msg:
        return 'אוקיי'

    return None

def i_have_answers(user_msg):
    if any(question in user_msg for question in ['יש לי שיעור', 'יש לי אירוע', 'יש לי טיול']):
        return 'תהנה'
    if 'יש לי חתול' in user_msg:
        return 'חתוללל'
    if 'יש לי כלב' in user_msg:
        return 'כלבבב'
    if 'יש לי אוגר' in user_msg:
        return 'אוגררר'
    if 'יש לי שאל' in user_msg:
        return 'תשאל/י'
    if 'יש לי מבחן' in user_msg:
        return 'בהצלחה'
    if 'יש לי חום' in user_msg:
        return 'החלמה מהירה'

    return None

def i_dont_have_answers(user_msg):
    if 'אין לי כוח' in user_msg:
        return 'לי יש'
    if 'אין לי זמן' in user_msg:
        return 'גם לי אין זמן'
    if 'אין לי מבחנים' in user_msg:
        return "אוקיי"

    return None








