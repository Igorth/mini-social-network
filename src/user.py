import bcrypt
from src.post import Post


class User:
    user_count = 0  # Class attribute to generate unique users IDs

    def __init__(self, username: str, email: str, password: str):
        User.user_count += 1
        self.user_id = User.user_count
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        self.friends = []
        self.friend_requests = []
        self.posts = []

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def add_friend(self, friend: 'User'):
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        return False

    def remove_friend(self, friend: 'User') -> bool:
        if friend in self.friends:
            self.friends.remove(friend)
            friend.friends.remove(self)
            print(f"{friend.username} has been removed from your friends list.")
            return True
        else:
            print(f"{friend.username} is not in your friends list.")
            return False

    def send_friend_request(self, other_user: 'User'):
        if other_user not in self.friend_requests and other_user not in self.friends:
            other_user.friend_requests.append(self)
            print(f"Friend request sent to {other_user.username}")
        else:
            print(f"Cannot send friend request to {other_user.username}")

    def accept_friend_request(self, other_user: 'User'):
        if other_user in self.friend_requests:
            self.friends.append(other_user)
            other_user.friends.append(self)
            self.friend_requests.remove(other_user)
            print(f"Friend request from {other_user.username} accepted.")
        else:
            print(f"No friend request from {other_user.username} to accepted.")

    def reject_friend_request(self, other_user: 'User'):
        if other_user in self.friend_requests:
            self.friend_requests.remove(other_user)
            print(f"Friend request from {other_user.username} rejected.")
        else:
            print(f"No friend request from {other_user.username} to rejected.")

    def __repr__(self):
        return f"User(id={self.user_id}, username={self.username}, email={self.email})"

    def create_post(self, content: str) -> Post:
        new_post = Post(author=self, content=content)
        self.posts.append(new_post)
        print(f"Post created: {new_post}")
        return new_post

    def view_posts(self):
        for post in self.posts:
            print(post)

    def delete_post(self, post_id: int) -> bool:
        post_to_delete = next((post for post in self.posts if post.post_id == post_id), None)
        if post_to_delete:
            self.posts.remove(post_to_delete)
            print(f"Post deleted: {post_to_delete}")
            return True
        else:
            print(f"No post found with ID {post_id}")
            return False


class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        if username in self.users:
            print(f"Username '{username}' is already registered.")
            return None
        user = User(username, email, password)
        self.users[username] = user
        print(f"User '{username}' registered successfully.")
        return user

    def get_user(self, username):
        return self.users.get(username)

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            print(f"User '{username}' logged in successfully.")
            return user
        else:
            print("Invalid username or password.")
            return None
