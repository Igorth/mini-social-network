from user import User

# Create a new user
user1 = User('john_doe', 'john@test.ca', 'password123')
print(user1)

# Create another user and add as friend
user2 = User('jane_doe', 'jane@test.ca', 'password1')
print(user1.add_friend(user2))
print(user1.friends)

# Remove the friend
print(user1.remove_friend(user2))
print(user1.friends)
