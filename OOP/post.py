class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def change_password(self, new_password):
        self.password = new_password
    
    def get_post_info(self):
        print(f"Post: {self.message}. Written by {self.author}")