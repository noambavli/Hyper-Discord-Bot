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



def db_commands(user_msg,username):

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
        item ,list_name = extract_add_item_and_list(user_msg)
        if list_name and item:
            return add_to_list(item,list_name)

    if 'delete' in user_msg and 'from' in user_msg:
        item ,list_name = extract_delete_item_and_list(user_msg)
        if list_name and item:
            return delete_from_list(item,list_name)

    if "bot show" in user_msg:
        list_name = extract_list_name_show(user_msg)
        print(list_name)
        if list_name:
            return show(list_name)

    return None


def get_db_menu():
    # Assuming you have some content for your db menu
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

def extract_list_name_show(sentence):
    pattern = r'bot show (\S+)'

    match = re.search(pattern, sentence)

    if match:
        return match.group(1)
    else:
        return None


def extract_add_item_and_list(sentence):
    # Define regex pattern to match 'bot add <item> to <listname>'
    pattern = r'bot add (.*?) to (.+)'

    match = re.search(pattern, sentence, re.IGNORECASE)

    if match:
        item = match.group(1).strip()  # Strip whitespace from item
        listname = match.group(2).strip()  # Strip whitespace from listname
        return item, listname
    else:
        return None


def extract_delete_item_and_list(sentence):
    # Define regex pattern to match 'bot delete <item> from <listname>'
    pattern = r'bot delete (.+?) from (.+)'

    match = re.search(pattern, sentence)

    if match:
        item = match.group(1)
        listname = match.group(2)
        return item, listname
    else:
        return None


def extract_create_list_name(sentence):
    # Define the regex pattern to match 'bot create list <listname>'
    pattern = r'bot create list (\S+)'

    match = re.search(pattern, sentence, re.IGNORECASE)
    if match:
        return match.group(1)

    return None

def extract_delete_list_name(sentence):
    # Define the regex pattern to match 'bot create list <listname>'
    pattern = r'bot delete list (\S+)'

    match = re.search(pattern, sentence, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


def create_list(list_name):
    if not list_name:
        return None
    if lists_collection.find_one({'name': list_name}):
        return f"List '{list_name}' already exists."
    else:
        lists_collection.insert_one({'name': list_name, 'items': []})
        return f"{list_name} list created."


def delete_list(list_name):
    if not list_name:
        return None

    # Check if the list exists
    existing_list = lists_collection.find_one({'name': list_name})
    if existing_list:
        # Delete the list from the collection
        lists_collection.delete_one({'name': list_name})
        return f"List '{list_name}' has been deleted."
    else:
        return f"List '{list_name}' does not exist."


def add_to_list(data, list_name):
    list_doc = lists_collection.find_one({'name': list_name})
    if list_doc:
        lists_collection.update_one({'name': list_name}, {'$push': {'items': data}})
        return f"Added '{data}' to {list_name}."
    else:
        return f"List '{list_name}' does not exist."

def delete_from_list(data, list_name):
    list_doc = lists_collection.find_one({'name': list_name})
    if list_doc:
        # Use $pull to delete the item from the list
        result = lists_collection.update_one(
            {'name': list_name},
            {'$pull': {'items': data}}
        )
        # Check if any document was modified
        if result.modified_count > 0:
            return f"deleted '{data}' from {list_name}."
        else:
            return f"Item '{data}' not found in {list_name}."
    else:
        return f"List '{list_name}' does not exist."


def show(list_name):
    list_doc = lists_collection.find_one({'name': list_name})
    if list_doc:
        items = "\n".join(list_doc['items'])
        return  f"{list_name}:\n{items}"
    else:
        return f"List '{list_name}' does not exist."

def obsessed(username):
    user = username
    # Check if the user is already in the collection
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

def unobsessed(username):
    user = username
    # Update the document to pull the user from the users array
    result = obsessives_collection.update_one(
        {'obsessed_with': 'bot'},
        {'$pull': {'users': user}}
    )

    if result.modified_count > 0:
        return f"Removed '{user}' from obsessives."
    else:
        return f"'{user}' was not found in the obsessives."

def obsessives():
    obsessives_doc = obsessives_collection.find_one({'obsessed_with': 'bot'})
    if obsessives_doc:
        users = ", ".join(obsessives_doc['users'])
        return f"Obsessives: {users}"
    else:
        return "No one is obsessed with me yet."