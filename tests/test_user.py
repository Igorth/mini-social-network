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
    return user_manager.register_user("jane_doe", "jane@test.ca", "password6456")


def test_user_registration(user_manager):
    user = user_manager.register_user("john_doe", "john@test.ca", "password123")
    assert user.username == "john_doe"
    assert user.email == "john@test.ca"


def test_send_friend_request(user1, user2):
    user1.send_friend_request(user2)
    assert user1 in user2.friend_requests


def test_accept_friend_request(user1, user2):
    user1.send_friend_request(user2)
    user2.accept_friend_request(user1)
    assert user1 in user2.friends
    assert user2 in user1.friends


def test_reject_friend_request(user1, user2):
    user1.send_friend_request(user2)
    user2.reject_friend_request(user1)
    assert user1 not in user2.friend_requests


def test_create_post(user1):
    post = user1.create_post("Hi, this is a post")
    assert post in user1.posts
    assert post.content == "Hi, this is a post"


def test_delete_post(user1):
    post = user1.create_post("Hi, this is a post")
    result = user1.delete_post(post.post_id)
    assert result is True
    assert post not in user1.posts
