import re
import hashlib

password=input("Enter your password:")

def check_strength(password):
    strength=0
    if len(password)>= 8:
        strength +=1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search ("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*()_+=-]", password):
        strength +=1
    return strength
         
    

score = check_strength(password)

if score <=2:
    print("Password Strength:WEAK")
elif score==3 or score==4:
    print("Password Strength:MEDIUM")
else:
    print("Password Strength:STRONG")

hashed_password =hashlib.sha256(password.encode()).hexdigest()
print("Hashed Passowrd:", hashed_password)
