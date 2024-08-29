from user import UserManager

# Initialize the user manager
user_manager = UserManager()

# Register some users
user_john = user_manager.register_user("john_doe", "john@test.ca", "password123")
user_jane = user_manager.register_user("jane_doe", "jane@test.ca", "password1")

# Send a friend request from John to Jane
user_john.send_friend_request(user_jane)

# Jane accepts the friend request
user_jane.accept_friend_request(user_john)

# Remove friend
user_john.remove_friend(user_jane)

# Check friendship status
print(user_john.friends)
print(user_jane.friends)
