# import streamlit as st

# def login():
#     st.title("🔐 Admin Login")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in st.session_state.users and st.session_state.users[username] == password:
#             st.success("Login successful!")
#             st.session_state.logged_in = True
#             st.session_state.current_user = username
#             st.rerun()
#         else:
#             st.error("Invalid username or password")


# # import streamlit as st
# # import yaml
# # import streamlit_authenticator as stauth
# # from yaml.loader import SafeLoader

# # def login():
# #     with open('config.yaml') as file:
# #         config = yaml.load(file, Loader=SafeLoader)

# #     authenticator = stauth.Authenticate(
# #         config['credentials'],
# #         config['cookie']['name'],
# #         config['cookie']['key'],
# #         config['cookie']['expiry_days'],
# #         config['preauthorized']
# #     )

# #     name, authentication_status, username = authenticator.login("Login", "main")

# #     if authentication_status:
# #         st.session_state.logged_in = True
# #         st.session_state.current_user = username
# #         st.success(f"Welcome back, {name}!")
# #         st.rerun()
# #     elif authentication_status is False:
# #         st.error("Username or password is incorrect")
# #     elif authentication_status is None:
# #         st.warning("Please enter your username and password")


# # import streamlit_authenticator as stauth
# # import yaml
# # from yaml.loader import SafeLoader
# # import streamlit as st

# # def login():
# #     with open('config.yaml') as file:
# #         config = yaml.load(file, Loader=SafeLoader)

# #     authenticator = stauth.Authenticate(
# #         config['credentials'],
# #         config['cookie']['name'],
# #         config['cookie']['key'],
# #         config['cookie']['expiry_days'],
# #     )

# #     # name, authentication_status, username = authenticator.login("Login", "main")
# #     name, authentication_status, username = authenticator.login(location="main")


# #     if authentication_status:
# #         st.session_state.logged_in = True
# #         st.session_state.current_user = username
# #         st.success(f"Welcome {name}!")
# #     elif authentication_status is False:
# #         st.error("Username/password is incorrect")
# #     elif authentication_status is None:
# #         st.warning("Please enter your username and password")


# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
# import streamlit as st

# def login():
#     with open('config.yaml', 'r') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#     )

#     name, authentication_status, username = authenticator.login("Login", location="main")

#     if authentication_status:
#         st.session_state.logged_in = True
#         st.session_state.current_user = name
#     elif authentication_status is False:
#         st.error("Incorrect username or password")
#     elif authentication_status is None:
#         st.warning("Please enter your credentials")

#     return name, authentication_status, username


# # def login():
# #     with open('config.yaml') as file:
# #         config = yaml.load(file, Loader=SafeLoader)

# #     authenticator = stauth.Authenticate(
# #         config['credentials'],
# #         config['cookie']['name'],
# #         config['cookie']['key'],
# #         config['cookie']['expiry_days'],
# #     )

# #     # login_return = authenticator.login("Login", "main")  # old version style
# #     # if login_return:
# #     #     name, authentication_status, username = login_return

# #     #     if authentication_status:
# #     #         st.session_state.logged_in = True
# #     #         st.session_state.current_user = username
# #     #         st.success(f"Welcome {name}!")
# #     #     elif authentication_status is False:
# #     #         st.error("Username/password is incorrect")
# #     #     elif authentication_status is None:
# #     #         st.warning("Please enter your username and password")
# #     # else:
# #     #     st.warning("Login could not be processed.")
# #     login_return = authenticator.login(location="main")

# #     if login_return is not None:
# #         name, authentication_status, username = login_return

# #         if authentication_status:
# #             st.session_state.logged_in = True
# #             st.session_state.current_user = username
# #             st.success(f"Welcome {name}!")
# #         elif authentication_status is False:
# #             st.error("Username/password is incorrect")
# #         elif authentication_status is None:
# #             st.warning("Please enter your username and password")
# import streamlit as st
# from admin_views.data import initialize_state, pcs
# from admin_views.register import register
# import pandas as pd
# import smtplib
# from email.message import EmailMessage

# # 🔐 Always initialize session state first!
# initialize_state()

# # Email Configuration
# EMAIL_SENDER = "iffatkhanin@gmail.com"
# EMAIL_PASSWORD = "iffat@2002"  # ⚠️ Use Gmail App Password, not your main password
# employee_emails = [
#     "khaniffat1507@example.com",
#     "iffatkhanin2002@example.com"
# ]

# def send_emails(form_link):
#     subject = "Kindly Fill the Employee Feedback Form"
#     body = f"Dear Employee,\n\nPlease take a moment to fill out this short feedback form:\n{form_link}\n\nThank you!"
    
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
#         for email in employee_emails:
#             msg = EmailMessage()
#             msg.set_content(body)
#             msg['Subject'] = subject
#             msg['From'] = EMAIL_SENDER
#             msg['To'] = email
#             server.send_message(msg)

#         server.quit()
#         return True
#     except Exception as e:
#         st.error(f"Error sending emails: {e}")
#         return False

# def login():
#     st.title("🔐 Admin Login")
#     username = st.text_input("Username", key="login_username")
#     password = st.text_input("Password", type="password", key="login_password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin123":
#             st.session_state.logged_in = True
#             st.session_state.current_user = username
#             st.success("Login successful!")
#             st.experimental_rerun()
#         else:
#             st.error("Invalid credentials")

# def admin_dashboard():
#     st.title("🛠️ Admin Dashboard")
#     st.markdown(f"👋 Welcome, **{st.session_state.current_user}**!")

#     st.markdown("### 🖥️ All PCs Overview")
#     st.dataframe(pcs[['MAC Address', 'Host Name', 'CPU Usage', 'RAM Usage', 'Disk Usage']])

#     selected_mac = st.selectbox("Select a PC (by MAC Address) to view full details:", pcs["MAC Address"], key="mac_select")

#     if selected_mac:
#         pc = pcs[pcs["MAC Address"] == selected_mac].iloc[0]
#         st.markdown("### 📋 PC Details")
#         st.markdown(
#             f"""
#             <div style="background-color: #f0f0f5; padding: 20px; border-radius: 10px; font-size: 16px;">
#                 <b>MAC Address:</b> {pc["MAC Address"]}<br>
#                 <b>Host Name:</b> {pc["Host Name"]}<br>
#                 <b>CPU Usage:</b> {pc["CPU Usage"]}<br>
#                 <b>RAM Usage:</b> {pc["RAM Usage"]}<br>
#                 <b>Disk Usage:</b> {pc["Disk Usage"]}<br>
#                 <b>Total Power:</b> {pc["Total Power"]}<br>
#                 <b>CO₂ Emission:</b> {pc["CO2 Emission"]}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     st.markdown("---")
#     st.markdown("### 📨 Send Review Form to Employees")
#     form_link = st.text_input("Enter Google Form link")

#     if st.button("Send Review Form"):
#         if form_link.strip() == "":
#             st.warning("Please enter a valid form link.")
#         else:
#             if send_emails(form_link):
#                 st.success("Emails sent successfully!")

#     if st.button("Logout"):
#         st.session_state.logged_in = False
#         st.session_state.current_user = None
#         st.experimental_rerun()

# # ✅ Ensure session state is initialized before accessing any keys
# if st.session_state.logged_in:
#     admin_dashboard()
# else:
#     menu = ["Login", "Register"]
#     choice = st.sidebar.selectbox("Menu", menu,key="sidebar_menu")

#     if choice == "Login":
#         login()
#     elif choice == "Register":
#         register()



# import streamlit as st

# def login(key_prefix="default"):
#     st.title("Login")

#     username = st.text_input("Username", key=f"{key_prefix}_username")
#     password = st.text_input("Password", type="password", key=f"{key_prefix}_password")

#     login_button = st.button("Login", key=f"{key_prefix}_login_btn")

#     if login_button:
#         if username == "admin" and password == "admin123":  # example logic
#             st.success("Login successful!")
#             st.session_state[f"{key_prefix}_logged_in"] = True
#         else:
#             st.error("Invalid credentials")

#     # Optional: return login status and username
#     return st.session_state.get(f"{key_prefix}_logged_in", False), username



# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# def login():
#     # Load the config
#     with open('config.yaml') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     # Create authenticator object
#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days']
#     )

#     name, auth_status, username = authenticator.login("Login","main")

#     if auth_status:
#         st.success(f"Welcome {name}!")
#     elif auth_status is False:
#         st.error("Invalid credentials")
#     elif auth_status is None:
#         st.warning("Please enter your credentials")
#     return auth_status, username