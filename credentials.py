import os

class Credentials:
    EMAIL = os.getenv("USER_EMAIL", "poudelsunayana@gmail.com")  # Fetch from environment variable
    PASSWORD = os.getenv("USER_PASSWORD", "Susuna123@")  # Fetch from environment variable

    @staticmethod
    def get_credentials():
        return Credentials.EMAIL, Credentials.PASSWORD
