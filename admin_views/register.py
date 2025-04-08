# # import streamlit as st

# # def register():
# #     st.title("📝 Register New Admin")

# #     new_username = st.text_input("New Username")
# #     new_password = st.text_input("New Password", type="password")

# #     if st.button("Register"):
# #         if new_username in st.session_state.users:
# #             st.warning("Username already exists!")
# #         else:
# #             st.session_state.users[new_username] = new_password
# #             st.success("Registration successful! Please login.")
# #             st.experimental_rerun()
# import streamlit as st

# def register():
#     st.title("📝 Register New Admin")

#     # Initialize the session state for users
#     if "users" not in st.session_state:
#         st.session_state.users = {}

#     new_username = st.text_input("New Username")
#     new_password = st.text_input("New Password", type="password")

#     if st.button("Register"):
#         if new_username in st.session_state.users:
#             st.warning("Username already exists!")
#         else:
#             st.session_state.users[new_username] = new_password
#             st.success("Registration successful! Please login.")
#             st.rerun()
# import streamlit as st
# import yaml
# import os
# import streamlit_authenticator as stauth
# from yaml.loader import SafeLoader

# CONFIG_PATH = "config.yaml"

# def load_config():
#     if os.path.exists(CONFIG_PATH):
#         with open(CONFIG_PATH, "r") as file:
#             return yaml.load(file, Loader=SafeLoader)
#     else:
#         return {
#             "credentials": {"usernames": {}},
#             "cookie": {
#                 "expiry_days": 1,
#                 "key": "some_signature_key",
#                 "name": "esg_dashboard_cookie"
#             },
#             "preauthorized": {"emails": []}
#         }

# def save_config(config):
#     with open(CONFIG_PATH, "w") as file:
#         yaml.dump(config, file, default_flow_style=False)

# def register():
#     st.title("📝 Register New User")

#     username = st.text_input("Username")
#     name = st.text_input("Full Name")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Register"):
#         if not (username and name and email and password):
#             st.warning("Please fill in all fields.")
#             return

#         config = load_config()

#         if username in config['credentials']['usernames']:
#             st.error("Username already exists.")
#             return

#         hashed_password = stauth.Hasher([password]).generate()[0]

#         config['credentials']['usernames'][username] = {
#             "name": name,
#             "email": email,
#             "password": hashed_password
#         }

#         config['preauthorized']['emails'].append(email)

#         save_config(config)

#         st.success("User registered successfully! You can now log in.")


# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# def register():
#     st.subheader("Register a new user")

#     with open('config.yaml', 'r') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#     )

#     try:
#         if authenticator.register_user("Register"):
#             with open('config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success("User registered successfully! Please restart the app.")
#     except Exception as e:
#         st.error(f"Registration failed: {e}")


# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# def register():
#     st.subheader("Register a new user")

#     with open('config.yaml', 'r') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#     )

#     try:
#         # Specify the location as "main" or "sidebar"
#         if authenticator.register_user():
#             with open('config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success("User registered successfully! Please restart the app.")
#     except Exception as e:
#         st.error(f"Registration failed: {e}")


# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# def register():
#     st.subheader("Register a new user")

#     # Load the config
#     with open('config.yaml', 'r') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     # Initialize authenticator
#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#     )

#     try:
#         # Register user and get updated config
#         new_config = authenticator.register_user()  # Optional flag

#         if new_config:
#             st.success("User registered successfully! Please restart the app.")
#     except Exception as e:
#         st.error(f"Registration failed: {e}")


# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# def register():
#     st.subheader("Register a new user")

#     # Load the config
#     with open('config.yaml', 'r') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     if not isinstance(config, dict):
#         st.error("Invalid config format. Please check config.yaml.")
#         return

#     # Initialize authenticator
#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#     )

#     try:
#         # Register user and get updated config
#         new_config = authenticator.register_user()  # Optional flag

#         if new_config:
#             with open('config.yaml', 'w') as file:
#                 yaml.safe_dump(new_config, file, default_flow_style=False)
#             st.success("User registered successfully! Please restart the app.")
#     except Exception as e:
#         st.error(f"Registration failed: {e}")

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt

def register():
    st.subheader("Register a new user")

    # Load the config
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=SafeLoader)

    if not isinstance(config, dict):
        st.error("Invalid config format. Please check config.yaml.")
        return

    # Default values
    default_email = "admin@example.com"
    default_username = "admin"
    default_name = "Admin User"
    default_password = "admin123"

    # Registration form
    with st.form("Register", clear_on_submit=False):
        email = st.text_input("Email", value=default_email)
        username = st.text_input("Username", value=default_username)
        name = st.text_input("Full Name", value=default_name)
        password = st.text_input("Password", type="password", value=default_password)
        submitted = st.form_submit_button("Register")

    if submitted:
        # Hash the password
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Update config
        if 'credentials' not in config:
            config['credentials'] = {'usernames': {}}
        if 'usernames' not in config['credentials']:
            config['credentials']['usernames'] = {}

        config['credentials']['usernames'][username] = {
            'email': email,
            'name': name,
            'password': hashed_pw
        }

        # Save updated config
        with open('config.yaml', 'w') as file:
            yaml.safe_dump(config, file, default_flow_style=False)

        st.success("User registered successfully! Please restart the app.")
