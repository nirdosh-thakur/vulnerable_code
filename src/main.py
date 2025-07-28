from src.db import create_db, add_user, get_user_by_id
from src.auth import create_user_profile, load_user_profile, hash_password
from src.config import API_KEY

def main():
    print("User Service Starting...")
    print(f"Using API key: {API_KEY[:5]}***")

    create_db()

    add_user("alice", 30)
    add_user("bob", 22)

    user = get_user_by_id("1")
    print("User 1:", user)

    create_user_profile("alice")
    load_user_profile("alice")

    print("Password hash:", hash_password("pass123"))

if __name__ == "__main__":
    main()
