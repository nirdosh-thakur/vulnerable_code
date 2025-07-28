# 🐍 Sample Python Vulnerable App

This is a simple and intentionally vulnerable Python application meant for educational and testing purposes.

---

## 📦 What It Does

- Stores user info in a SQLite database (`db.py`)
- Creates and loads user profiles using `pickle` (`auth.py`)
- Hashes passwords using `MD5` (`auth.py`, `util.py`)
- Executes raw Python code using `eval()` (`util.py`)

---

## ⚠️ Vulnerabilities

1. **Hardcoded API Key**
   - File: `config.py`
   - `API_KEY` is stored in plain text.

2. **Insecure Deserialization**
   - File: `auth.py`
   - Uses `pickle.load()` on user-controlled input.

3. **Weak Password Hashing**
   - Files: `auth.py`, `util.py`
   - Uses `MD5`, which is outdated and insecure.

4. **SQL Injection**
   - File: `db.py`
   - Constructs SQL query using unsanitized user input.

5. **Arbitrary Code Execution**
   - File: `util.py`
   - Uses `eval()` on user-supplied code.

---

## ⚠️ Disclaimer

This code is for educational use **only**. Do not use in production.
