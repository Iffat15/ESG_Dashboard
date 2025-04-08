import streamlit as st
import pandas as pd
from admin_views.data import pcs, initialize_state
# from admin_views.login import login
# from admin_views.register import register

# Setup
initialize_state()

def admin_dashboard():
    st.title("🛠️ Admin Dashboard")
    st.markdown(f"👋 Welcome, **{st.session_state.current_user}**!")

    st.markdown("### 🖥️ All PCs Overview")
    st.dataframe(pcs[['MAC Address', 'Host Name', 'CPU Usage', 'RAM Usage', 'Disk Usage']])

    selected_mac = st.selectbox("Select a PC (by MAC Address) to view full details:", pcs["MAC Address"])

    if selected_mac:
        pc = pcs[pcs["MAC Address"] == selected_mac].iloc[0]
        st.markdown("### 📋 PC Details")
        st.markdown(
            f"""
            <div style="background-color: #f0f0f5; padding: 20px; border-radius: 10px; font-size: 16px;">
                <b>MAC Address:</b> {pc["MAC Address"]}<br>
                <b>Host Name:</b> {pc["Host Name"]}<br>
                <b>CPU Usage:</b> {pc["CPU Usage"]}<br>
                <b>RAM Usage:</b> {pc["RAM Usage"]}<br>
                <b>Disk Usage:</b> {pc["Disk Usage"]}<br>
                <b>Total Power:</b> {pc["Total Power"]}<br>
                <b>CO₂ Emission:</b> {pc["CO2 Emission"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.experimental_rerun()


# Main Router
# menu = ["Login", "Register"]
# if not st.session_state.logged_in:
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "Login":
#         login()
#     elif choice == "Register":
#         register()
# else:
    # admin_dashboard()


# # import streamlit as st
# # import pandas as pd
# # import smtplib
# # from email.message import EmailMessage
# # from admin_views.data import pcs, initialize_state
# # from admin_views.login import login
# # from admin_views.register import register

# # # Setup
# # # initialize_state()


# # def initialize_state():
# #     if 'logged_in' not in st.session_state:
# #         st.session_state.logged_in = False
# #     if 'current_user' not in st.session_state:
# #         st.session_state.current_user = None


# # # Email Configuration
# # EMAIL_SENDER = "iffatkhanin@gmail.com"
# # EMAIL_PASSWORD = "iffat@2002"  # Use Gmail App Password
# # employee_emails = [
# #     "khaniffat1507@example.com",
# #     "iffatkhanin2002@example.com"
# # ]

# # def send_emails(form_link):
# #     subject = "Kindly Fill the Employee Feedback Form"
# #     body = f"Dear Employee,\n\nPlease take a moment to fill out this short feedback form:\n{form_link}\n\nThank you!"
    
# #     try:
# #         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# #         server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
# #         for email in employee_emails:
# #             msg = EmailMessage()
# #             msg.set_content(body)
# #             msg['Subject'] = subject
# #             msg['From'] = EMAIL_SENDER
# #             msg['To'] = email
# #             server.send_message(msg)

# #         server.quit()
# #         return True
# #     except Exception as e:
# #         st.error(f"Error sending emails: {e}")
# #         return False

# # def admin_dashboard():
# #     st.title("🛠️ Admin Dashboard")
# #     st.markdown(f"👋 Welcome, **{st.session_state.current_user}**!")

# #     st.markdown("### 🖥️ All PCs Overview")
# #     st.dataframe(pcs[['MAC Address', 'Host Name', 'CPU Usage', 'RAM Usage', 'Disk Usage']])

# #     selected_mac = st.selectbox("Select a PC (by MAC Address) to view full details:", pcs["MAC Address"])

# #     if selected_mac:
# #         pc = pcs[pcs["MAC Address"] == selected_mac].iloc[0]
# #         st.markdown("### 📋 PC Details")
# #         st.markdown(
# #             f"""
# #             <div style="background-color: #f0f0f5; padding: 20px; border-radius: 10px; font-size: 16px;">
# #                 <b>MAC Address:</b> {pc["MAC Address"]}<br>
# #                 <b>Host Name:</b> {pc["Host Name"]}<br>
# #                 <b>CPU Usage:</b> {pc["CPU Usage"]}<br>
# #                 <b>RAM Usage:</b> {pc["RAM Usage"]}<br>
# #                 <b>Disk Usage:</b> {pc["Disk Usage"]}<br>
# #                 <b>Total Power:</b> {pc["Total Power"]}<br>
# #                 <b>CO₂ Emission:</b> {pc["CO2 Emission"]}
# #             </div>
# #             """,
# #             unsafe_allow_html=True
# #         )

# #     st.markdown("---")
# #     st.markdown("### 📨 Send Review Form to Employees")
# #     form_link = st.text_input("Enter Google Form link")

# #     if st.button("Send Review Form"):
# #         if form_link.strip() == "":
# #             st.warning("Please enter a valid form link.")
# #         else:
# #             if send_emails(form_link):
# #                 st.success("Emails sent successfully!")

# #     if st.button("Logout"):
# #         st.session_state.logged_in = False
# #         st.session_state.current_user = None
# #         st.experimental_rerun()

# # # Main Router
# # menu = ["Login", "Register"]
# # if not st.session_state.logged_in:
# #     choice = st.sidebar.selectbox("Menu", menu)

# #     if choice == "Login":
# #         login()
# #     elif choice == "Register":
# #         register()
# # else:
# #     admin_dashboard()

# import streamlit as st
# from admin_views.login import login

# logged_in, user = login(key_prefix="admin_page")

# if logged_in:
#     st.sidebar.success(f"Welcome, {user}")
#     # render rest of your admin dashboard here
# else:
#     st.warning("Please log in to continue.")
# import streamlit as st
# from admin_views.login import login
# from admin_views.register import register  # Make sure this file exists

# # Sidebar menu to switch between Login and Register
# menu = ["Login", "Register"]
# choice = st.sidebar.selectbox("Select Option", menu)

# if choice == "Login":
#     logged_in, user = login()

#     if logged_in:
#         st.sidebar.success(f"Welcome, {user}")
#         st.title("Admin Dash")
#         # render rest of your admin dashboard here
#     else:
#         st.warning("Please log in to continue.")

# elif choice == "Register":
#     register()
import streamlit as st
import pandas as pd
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")  # Replace with your URI
db = client["ESG"]
collection = db["Social_Score"]

st.title("📤 Admin CSV Uploader")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV into DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Uploaded CSV")
    st.dataframe(df)

    if st.button("Append to MongoDB"):
        # Convert DataFrame to dictionary and insert into MongoDB
        data = df.to_dict(orient="records")
        result = collection.insert_many(data)
        st.success(f"✅ Uploaded {len(result.inserted_ids)} records to MongoDB!")
