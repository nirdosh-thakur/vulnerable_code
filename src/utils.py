import hashlib

def run_python_code(code):
    eval(code)

def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()
