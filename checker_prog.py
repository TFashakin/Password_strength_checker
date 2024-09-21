import re

def password_strength_score(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
        
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    
    if re.search(r'\d', password):
        score += 1
        
    if re.search(r'[@$!%*?&#]', password):
        score += 1
        
    common_passwords = ["password", "12345678", "qwertyuiop", "123456", "admin", "123456789", "1234", "12345", "Aa123456", "123123", "111111", "Password","admin123","P@ssw0rd","root","Pass@123","ubnt", "1q2w3e4r", "qwerty"]
    if password in common_passwords:
        score = 0
        
    return score

def password_score_message(score):
    if score == 4:
        return  "Strong password"
    elif score == 3:
        return "Good password"
    else:
        return "Weak Password"
    
if __name__ == "__main__":
    password = input("Enter your password: ")
    score =  password_strength_score(password)
    print(password_score_message(score))
    
#<|eom_id|><|start_header_id|>assistant<|end_header_id|> verify ai input

