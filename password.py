import string
import random
import streamlit as st
import re

def generate_password(length):
    chracters = string.digits + string.ascii_letters + "!@#$%^&"
    return "".join(random.choice(chracters) for i in range(length)) 

# function to check password
def check_password_strength(password):
    score = 0
    common_passwords = ["12345678","abc123","pak123456","karachi123","password"]
    if password in common_passwords:
        return "🤞This password is weak choose a strong password"
    
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("♦ Password should be atleast 8 chracters long.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("♦ Includes both uppercase and lowercase letters.")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("♦ Add atleast one number(0-9).")
    
    if re.search(r"[!@#$%^&]",password):
        score += 1
    else:
        feedback.append("♦ Include atleast one special chracter (!@#$%^&).")

    if score == 4:
        return "✔ Strong password","strong"
    elif score == 3:
        return "Moderate password, Add more features","Moderate"
    else:
        return "\n".join(feedback),"Weak"
    
    # password strength cheacker
    

check_password = st.text_input("Enter your password",type = "password")
if st.button("Check Strength"):
    if check_password:
        result, strength = check_password_strength(check_password)
        if strength == "strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
        else: 
            st.error("Weak password : improve it using these tips:")
            for tip in result.split("\n"):
               st.write(tip)
    else:
        st.warning("Please enter a password")
        
    





# Streamlit UI
# st.title("Random Password Generator")

password_length = st.number_input("Enter the length of password",min_value=8,max_value=20,value=10)
if st.button("Generate Passsword"):
    password = generate_password(password_length)
    st.success(f"{password}")
    