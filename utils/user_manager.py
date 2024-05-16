import os

class UserManager:
    def __init__(self, user_file):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.user_file):
            return {}
        with open(self.user_file, 'r') as f:
            users = {}
            for line in f.readlines():
                username, password = line.strip().split(':')
                users[username] = password
            return users

    def register(self, username, password):
        if username in self.users:
            return False
        if len(username) < 4 or len(password) < 8:
            return False
        with open(self.user_file, 'a') as f:
            f.write(f"{username}:{password}\n")
        self.users[username] = password
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False