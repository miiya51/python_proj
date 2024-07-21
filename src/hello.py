import os
from dotenv import load_dotenv

# .envファイルの内容を読みこむ
load_dotenv()

class Hello:
    def __init__(self):
        self.greeting = "Hello, World!"

    def say(self):
        print(self.greeting)