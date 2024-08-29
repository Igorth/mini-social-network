from user import UserManager

# Initialize the user manager
user_manager = UserManager()

# Register some users
user_manager.register_user("john_doe", "john@test.ca", "password123")
user_manager.register_user("jane_doe", "jane@test.ca", "password1")

# Attempt to log in with correct credentials
user = user_manager.login_user("john_doe", "password123")
print(user)

# Attempt to log in with incorrect credentials
user = user_manager.login_user("john_doe", "wrong_password")
print(user)

# Attempt to log in with a non-existing username
user = user_manager.login_user("non_existing_username", "password1")
print(user)