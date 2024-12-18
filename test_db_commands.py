import time
from os import getenv

from dotenv import load_dotenv
load_dotenv()
import pymongo
import pytest
from unittest.mock import MagicMock, patch

from db_user_commands import db_commands, create_list, delete_list, add_to_list, delete_from_list, show, obsessed, \
    unobsessed, obsessives

@pytest.fixture
def mock_collections():
    with patch('db_user_commands.lists_collection') as mock_lists, patch(
            'db_user_commands.obsessives_collection') as mock_obsessives:
        yield mock_lists, mock_obsessives

def test_mongodb(mock_collections):
    client = pymongo.MongoClient(getenv("MONGO_URL"))
    assert client.admin.command("ping")["ok"] != 0.0

def test_create_list(mock_collections):
    result = db_commands("bot create list myList", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


# Test case for db_commands function - "delete list"
def test_delete_list(mock_collections):
    result = db_commands("bot delete list myList", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_add_to_list(mock_collections):
    result = db_commands("bot add item1 to myList", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_delete_from_list(mock_collections):
    result = db_commands("bot delete 'item1' from myList", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_show_list(mock_collections):
    result = db_commands("bot show myList", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_obsessed(mock_collections):
    result = db_commands("bot i am obsessed with you", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_unobsessed(mock_collections):
    result = db_commands("bot i am not obsessed with you", "user1")
    assert not result.startswith("Error"), f"Error: {result}"


def test_obsessives_list(mock_collections):
    result = db_commands("bot who is obsessed with you", "user1")
    assert not result.startswith("Error"), f"Error: {result}"

def test_logic_flow_obsessives(mock_collections):
    db_commands("bot i am obsessed with you", "user1")
    result = db_commands("bot who is obsessed with you", "user1")
    assert "user1" in result
