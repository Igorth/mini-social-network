import pytest
from src.user import User, UserManager


@pytest.fixture
def user_manager():
    return UserManager()


@pytest.fixture
def user1(user_manager):
    return user_manager.register_user("john_doe", "john@test.ca", "password123")


@pytest.fixture
def user2(user_manager):
    return user_manager.register_user("jane_doe", "jane@test.ca", "password456")


def test_send_message(user1, user2):
    message = user1.send_message(user2, "How are you Jane?")
    assert message.content == "How are you Jane?"
    assert message.sender == user1
    assert message.receiver == user2
    assert message in user2.get_messages()


def test_receive_message(user1, user2):
    user1.send_message(user2, "Again here")
    assert len(user2.get_messages()) == 1
    assert user2.get_messages()[0].content == "Again here"
