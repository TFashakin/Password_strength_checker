import re
import sqlite3
#create pwd db
def create_password_db():
    common_passwords = [
        "123456", "123456789", "qwerty", "password", "12345", "12345678", "111111", "123123", "abc123", "1234567",
        "password1", "123", "1234567890", "1234", "000000", "iloveyou", "123321", "qwertyuiop", "admin", "654321",
        "welcome", "1q2w3e4r", "1qaz2wsx", "qazwsx", "sunshine", "letmein", "monkey", "dragon", "passw0rd", "shadow",
        "superman", "password123", "batman", "trustno1", "football", "zaq1zaq1", "master", "baseball", "hello", 
        "freedom", "whatever", "charlie", "asdfghjkl", "jordan23", "robert", "michael", "ninja", "mustang", "access",
        "tigger"
    ]
    #initializing  the database

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS common_passwords (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      password TEXT UNIQUE)''')
    
    for pwd in common_passwords:
        try:
            cursor.execute("INSERT INTO common_passwords (password) VALUES (?)", (pwd,))
        except sqlite3.IntegrityError:
            pass
    
    conn.commit()
    conn.close()

def password_strength_score(password, cursor):
    score = 0
    
    if len(password) >= 8:
        score += 1
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    
    if re.search(r'\d', password):
        score += 1
    
    if re.search(r'[@$!%*?&#]', password):
        score += 1
    
    cursor.execute("SELECT * FROM common_passwords WHERE password=?", (password,))
    if cursor.fetchone():
        score = 0
    
    return score

def check_password_strength(password, cursor):
    strength = "Weak"
    score = password_strength_score(password, cursor)

    if score == 4:
        strength = "Very Strong"
    elif score == 3:
        strength = "Strong"
    elif score == 2:
        strength = "Moderate"
    
    return strength, score

def run_password_checker():
    create_password_db()

    print("Welcome to the Password Strength Checker App!")
    print("You can use this tool to check the strength of your passwords.")
    print("After each check, you'll be asked if you'd like to try again.")
    print("Let's get started!")

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    while True:
        password = input("\nPlease enter a password to check its strength: ")

        strength, score = check_password_strength(password, cursor)
        print(f"Your password strength is: {strength}, with a score of {score}")

        try_again = input("\nWould you like to check another password? (yes/no): ").strip().lower()

        if try_again != 'yes':
            print("Thank you for using the Password Strength Checker. Goodbye!")
            break
    
    conn.close()

run_password_checker()
