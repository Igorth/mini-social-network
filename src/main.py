from user import UserManager

# Initialize the user manager
user_manager = UserManager()

# Register some users
user_john = user_manager.register_user("john_doe", "john@test.ca", "password123")
user_jane = user_manager.register_user("jane_doe", "jane@test.ca", "password1")
user_larry = user_manager.register_user("larryK", "larry@test.ca", "password345")

# Send a friend request from John to Jane
user_john.send_friend_request(user_jane)
user_john.send_friend_request(user_larry)

# Jane accepts the friend request
user_jane.accept_friend_request(user_john)

# Larry accepts the friend request
user_larry.accept_friend_request(user_john)

# Attempt to reject a non-existent friend request
user_john.reject_friend_request(user_larry)

print(user_john.friends)
print(user_larry.friends)
