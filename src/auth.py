import bcrypt
import json
import os
from pathlib import Path

def hash_password(password):
    """Hash the provided password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def create_user_data(username):
    """Create a new user data file with the given username."""
    user_data = {"username": username, "theme": "light"}
    profiles_dir = Path("profiles")
    profiles_dir.mkdir(exist_ok=True)
    profile_path = profiles_dir / f"{username}.json"
    with profile_path.open("w") as f:
        json.dump(user_data, f)

def load_user_data(username):
    """Load user data from the file with the given username."""
    profiles_dir = Path("profiles")
    profile_path = profiles_dir / f"{username}.json"
    if profile_path.exists():
        try:
            with profile_path.open("r") as f:
                user_data = json.load(f)
            print(f"Loaded user data for {username}: {user_data}")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading user data for {username}: {e}")
    else:
        print(f"User data not found for {username}.")