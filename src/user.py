class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.friends = []

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

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
