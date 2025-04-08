# import pandas as pd
# import streamlit as st

# # Sample PC data
# pcs = pd.DataFrame([
#     {"MAC Address": "00:1A:2B:3C:4D:01", "Host Name": "Host-1", "CPU Usage": "73%", "RAM Usage": "6.5 GB", "Disk Usage": "120 GB", "Total Power": "2.5 kWh", "CO2 Emission": "0.0004 kg"},
#     {"MAC Address": "00:1A:2B:3C:4D:02", "Host Name": "Host-2", "CPU Usage": "25%", "RAM Usage": "4.2 GB", "Disk Usage": "90 GB",  "Total Power": "1.8 kWh", "CO2 Emission": "0.0003 kg"},
#     {"MAC Address": "00:1A:2B:3C:4D:03", "Host Name": "Host-3", "CPU Usage": "89%", "RAM Usage": "7.9 GB", "Disk Usage": "140 GB", "Total Power": "3.1 kWh", "CO2 Emission": "0.0006 kg"},
#     {"MAC Address": "00:1A:2B:3C:4D:04", "Host Name": "Host-4", "CPU Usage": "64%", "RAM Usage": "5.3 GB", "Disk Usage": "100 GB", "Total Power": "2.2 kWh", "CO2 Emission": "0.00035 kg"},
# ])

# # Session state initialization
# def initialize_state():
#     if 'users' not in st.session_state:
#         st.session_state.users = {'admin': 'admin123'}
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
#     if 'current_user' not in st.session_state:
#         st.session_state.current_user = None


# admin_views/data.py

import streamlit as st
import pandas as pd

def initialize_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None

pcs = pd.DataFrame([
    {
        "MAC Address": "00:11:22:33:44:55",
        "Host Name": "PC-01",
        "CPU Usage": "45%",
        "RAM Usage": "60%",
        "Disk Usage": "70%",
        "Total Power": "80W",
        "CO2 Emission": "0.05kg"
    },
    {
        "MAC Address": "66:77:88:99:AA:BB",
        "Host Name": "PC-02",
        "CPU Usage": "50%",
        "RAM Usage": "70%",
        "Disk Usage": "65%",
        "Total Power": "75W",
        "CO2 Emission": "0.04kg"
    }
])
