from user import UserManager

# Initialize the user manager
user_manager = UserManager()

# Register some users
user_john = user_manager.register_user("john_doe", "john@test.ca", "password123")
user_jane = user_manager.register_user("jane_doe", "jane@test.ca", "password1")

# Create posts
post_1 = user_john.create_post("This is John's post")
post_2 = user_jane.create_post("This is Jane's post")
post_3 = user_jane.create_post("This is Jane's post")

# View posts
print("\nJohn's posts:")
user_john.view_posts()

print("\nJane's posts:")
user_jane.view_posts()
