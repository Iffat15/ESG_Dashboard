import streamlit_authenticator as stauth

passwords = "Admin@123"  # Replace with your desired password
hashed_password = stauth.Hasher().hash(passwords)

print("Your hashed password is:")
print(hashed_password)