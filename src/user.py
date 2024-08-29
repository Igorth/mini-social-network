class User:
    user_count = 0  # Class attribute to generate unique users IDs

    def __init__(self, username, email, password):
        User.user_count += 1
        self.user_id = User.user_count
        self.username = username
        self.email = email
        self.password = password
        self.friends = []

    def __repr__(self):
        return f"User(id={self.user_id}, username={self.username}, email={self.email})"

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        return False

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            return True
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