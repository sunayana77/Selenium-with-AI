import os

class Credentials:
    EMAIL = os.getenv("USER_EMAIL", "your_email")  # Fetch from environment variable
    PASSWORD = os.getenv("USER_PASSWORD", "your_password")  # Fetch from environment variable

    @staticmethod
    def get_credentials():
        return Credentials.EMAIL, Credentials.PASSWORD
