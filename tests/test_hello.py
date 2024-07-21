import os
from src.hello import Hello

def test_hello():
    hello = Hello()
    assert hello.greeting == "Hello, World!"
    assert os.environ.get("TEST") == "aaa"