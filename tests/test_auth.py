from src.auth import hash_password

def test_hash_password():
    assert hash_password("hello") == "5d41402abc4b2a76b9719d911017c592"
