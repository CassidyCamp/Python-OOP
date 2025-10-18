class User:
    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active
        
        
user = User("daler", "random@email.com", False)
user = User("Samandar", "random@email.com", True)