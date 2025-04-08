# import pickle
# from pathlib import Path
# from streamlit_authenticator.utilities.hasher import Hasher

# names = ["Peter Parker", "Rebecca Miller"]
# usernames = ["pparker", "rmiller"]
# passwords = ["abc123", "def456"]

# # ✅ Updated for v0.4.2
# hashed_passwords = Hasher(passwords).generate()

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("wb") as file:
#     pickle.dump(hashed_passwords, file)



import pickle
from pathlib import Path
from streamlit_authenticator.utilities.hasher import Hasher

# Define your users and passwords
passwords = ["abc123", "def456"]

# Hash the passwords
hasher = Hasher()
hashed_passwords = hasher.generate(passwords)

# Save to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("✅ Passwords hashed and saved!")
