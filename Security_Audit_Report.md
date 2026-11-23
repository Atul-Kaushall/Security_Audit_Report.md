# Secure Coding Review & Vulnerability Audit Report

**Target Application:** Python User Authentication & Database Module (`vulnerable_app.py`)  
**Audit Method:** Manual Static Code Analysis  

---

## Executive Summary
A manual source code review was conducted on `vulnerable_app.py`. Three critical/high-severity security vulnerabilities were identified that expose the application to unauthorized database access, credential compromise, and secret leakage. All issues have been remediated in `secure_app.py`.

---

## Findings & Remediation

### 1. SQL Injection (Critical)
- **Location:** `get_user_data()` — Line 9
- **Issue:** User input (`username`) is directly interpolated into the SQL query string using an f-string. An attacker can input `' OR '1'='1` to dump the entire `users` table.
- **Remediation:** Replaced string formatting with parameterized queries (`?` placeholders) so the database driver treats user input strictly as data, not executable SQL commands.

### 2. Weak Password Hashing Algorithm (High)
- **Location:** `hash_password()` — Line 15
- **Issue:** Passwords are hashed using `MD5` without a salt. MD5 is cryptographically broken and vulnerable to collision and rainbow-table attacks.
- **Remediation:** Replaced `hashlib.md5` with `bcrypt`, which automatically generates a unique cryptographically secure salt per password and enforces key stretching.

### 3. Hardcoded Credentials / API Key (High)
- **Location:** Global Scope — Line 18
- **Issue:** `API_SECRET_KEY` is hardcoded directly in source control, exposing it to anyone with repository access.
- **Remediation:** Removed the hardcoded string and configured the application to retrieve `API_SECRET_KEY` securely at runtime via `os.environ.get()`.
