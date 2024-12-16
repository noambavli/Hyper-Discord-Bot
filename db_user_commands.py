from os import getenv
from pymongo import MongoClient
import re
from os import getenv
from dotenv import load_dotenv

load_dotenv()

mongo_url = getenv('MONGO_URL')

if mongo_url is None:
    raise ValueError("MONGO_URL is not set in the environment variables.")

client = MongoClient(mongo_url)
db = client['BotCluster']

lists_collection = db['lists']
obsessives_collection = db['obsessives']

def db_commands(user_msg, username):
    try:
        if "db menu" in user_msg:
            menu = get_db_menu()
            if menu:
                return menu
        if "bot i am obsessed with you" in user_msg or "bot im obsessed with you" in user_msg:
            return obsessed(username)

        if "bot who is obsessed with you" == user_msg:
            return obsessives()

        if "bot i am not obsessed with you" in user_msg or "bot im not obsessed with you" in user_msg:
            return unobsessed(username)

        if 'bot create' in user_msg:
            list_name = extract_create_list_name(user_msg)
            if list_name:
                return create_list(list_name)

        if 'bot delete' in user_msg:
            list_name = extract_delete_list_name(user_msg)
            if list_name:
                return delete_list(list_name)

        if 'add' in user_msg and 'to' in user_msg:
            item, list_name = extract_add_item_and_list(user_msg)
            if list_name and item:
                return add_to_list(item, list_name)

        if 'delete' in user_msg and 'from' in user_msg:
            item, list_name = extract_delete_item_and_list(user_msg)
            if list_name and item:
                return delete_from_list(item, list_name)

        if "bot show" in user_msg:
            list_name = extract_list_name_show(user_msg)
            print(list_name)
            if list_name:
                return show(list_name)

    except Exception as e:
        return f"Error: {e}"

    return None

def get_db_menu():
    try:
        db_menu = """
        Database Menu:
        bot create list <list name>
        bot delete list <list name>
        add <item> to <list name>
        delete <item> from <list name>
        bot i am obsessed with you
        bot im not obsessed with you
        bot who is obsessed with you
        """
        return db_menu.strip()
    except Exception as e:
        return f"Error: {e}"

def extract_list_name_show(sentence):
    try:
        pattern = r'bot show (\S+)'

        match = re.search(pattern, sentence)

        if match:
            return match.group(1)
        else:
            return None
    except Exception as e:
        return f"Error: {e}"

def extract_add_item_and_list(sentence):
    try:
        pattern = r'bot add (.*?) to (.+)'

        match = re.search(pattern, sentence, re.IGNORECASE)

        if match:
            item = match.group(1).strip()
            listname = match.group(2).strip()
            return item, listname
        else:
            return None
    except Exception as e:
        return f"Error: {e}"

def extract_delete_item_and_list(sentence):
    try:
        pattern = r'bot delete (.+?) from (.+)'

        match = re.search(pattern, sentence)

        if match:
            item = match.group(1)
            listname = match.group(2)
            return item, listname
        else:
            return None
    except Exception as e:
        return f"Error: {e}"

def extract_create_list_name(sentence):
    try:
        pattern = r'bot create list (\S+)'

        match = re.search(pattern, sentence, re.IGNORECASE)
        if match:
            return match.group(1)

        return None
    except Exception as e:
        return f"Error: {e}"

def extract_delete_list_name(sentence):
    try:
        pattern = r'bot delete list (\S+)'

        match = re.search(pattern, sentence, re.IGNORECASE)

        if match:
            return match.group(1)

        return None
    except Exception as e:
        return f"Error: {e}"

def create_list(list_name):
    try:
        if not list_name:
            return None
        if lists_collection.find_one({'name': list_name}):
            return f"List '{list_name}' already exists."
        else:
            lists_collection.insert_one({'name': list_name, 'items': []})
            return f"{list_name} list created."
    except Exception as e:
        return f"Error: {e}"

def delete_list(list_name):
    try:
        if not list_name:
            return None

        existing_list = lists_collection.find_one({'name': list_name})
        if existing_list:
            lists_collection.delete_one({'name': list_name})
            return f"List '{list_name}' has been deleted."
        else:
            return f"List '{list_name}' does not exist."
    except Exception as e:
        return f"Error: {e}"

def add_to_list(data, list_name):
    try:
        list_doc = lists_collection.find_one({'name': list_name})
        if list_doc:
            lists_collection.update_one({'name': list_name}, {'$push': {'items': data}})
            return f"Added '{data}' to {list_name}."
        else:
            return f"List '{list_name}' does not exist."
    except Exception as e:
        return f"Error: {e}"

def delete_from_list(data, list_name):
    try:
        list_doc = lists_collection.find_one({'name': list_name})
        if list_doc:
            result = lists_collection.update_one(
                {'name': list_name},
                {'$pull': {'items': data}}
            )
            if int(result.modified_count) > 0:
                return f"deleted {data} from {list_name}."
            else:
                return f"Item '{data}' not found in {list_name}."
        else:
            return f"List '{list_name}' does not exist."
    except Exception as e:
        return f"Error: {e}"

def show(list_name):
    try:
        list_doc = lists_collection.find_one({'name': list_name})
        if list_doc:
            items = "\n".join(list_doc['items'])
            return  f"{list_name}:\n{items}"
        else:
            return f"List '{list_name}' does not exist."
    except Exception as e:
        return f"Error: {e}"

def obsessed(username):
    try:
        user = username
        result = obsessives_collection.find_one({'obsessed_with': 'bot', 'users': user})

        if result:
            return f"'{user}' is already in the obsessives."
        else:
            obsessives_collection.update_one(
                {'obsessed_with': 'bot'},
                {'$push': {'users': user}},
                upsert=True
            )
            return f"Added '{user}' to obsessives."
    except Exception as e:
        return f"Error: {e}"

def unobsessed(username):
    try:
        user = username
        result = obsessives_collection.update_one(
            {'obsessed_with': 'bot'},
            {'$pull': {'users': user}}
        )

        if result.modified_count > 0:
            return f"Removed '{user}' from obsessives."
        else:
            return f"'{user}' was not found in the obsessives."
    except Exception as e:
        return f"Error: {e}"

def obsessives():
    try:
        obsessives_doc = obsessives_collection.find_one({'obsessed_with': 'bot'})
        if obsessives_doc:
            users = ", ".join(obsessives_doc['users'])
            return f"Obsessives: {users}"
        else:
            return "No one is obsessed with me yet."
    except Exception as e:
        return f"Error: {e}"
