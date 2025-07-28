import hashlib
import pickle
import os

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def create_user_profile(username):
    profile = {"username": username, "theme": "light"}
    with open(f"profiles/{username}.pkl", "wb") as f:
        pickle.dump(profile, f)

def load_user_profile(username):
    path = f"profiles/{username}.pkl"
    if os.path.exists(path):
        with open(path, "rb") as f:
            profile = pickle.load(f)
            print(f"Loaded profile for {username}: {profile}")
    else:
        print("Profile not found.")
