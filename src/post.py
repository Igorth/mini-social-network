import datetime


class Post:
    post_count = 0

    def __init__(self, author, content):
        Post.post_count += 1
        self.post_id = Post.post_count
        self.author = author
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return f"Post(id={self.post_id}, author={self.author.username}, content={self.content}, timestamp={self.timestamp}"
