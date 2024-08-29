# from user import User
#
# # Create a new user
# user1 = User('john_doe', 'john@test.ca', 'password123')
# print(user1)
#
# # Create another user and add as friend
# user2 = User('jane_doe', 'jane@test.ca', 'password1')
# print(user1.add_friend(user2))
# print(user1.friends)
#
# # Remove the friend
# print(user1.remove_friend(user2))
# print(user1.friends)

from user import UserManager

# Initialize the user manager
user_manager = UserManager()

# Register some users
user_manager.register_user("john_doe", "john@test.ca", "password123")
user_manager.register_user("jane_doe", "jane@test.ca", "password1")

# Retrieve and display a user
user = user_manager.get_user("john_doe")
print(user)

# Register a user with a taken username
user_manager.register_user("jane_doe", "test.ca", "31231")

# Delete a user
user_manager.delete_user("john_doe")

# Try to retrieve the deleted user
user = user_manager.get_user("john_doe")
print(user)  # This will print None
