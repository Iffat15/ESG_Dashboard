import streamlit as st
import pandas as pd
import plotly.express as px
import requests
# Set page title and layout
st.set_page_config(page_title="Green IT Dashboard", layout="wide")


st.markdown("""
    <style>
        .css-1d391kg {display: none}  /* Sidebar */
        .css-h5rgaw {display: none}  /* Sidebar content */
    </style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;  /* Decrease this value to reduce top spacing */
        }
    </style>
    """,
    unsafe_allow_html=True
)
with st.container():
    col1, col2, col3,col4,col5 = st.columns([2, 4, 3,1,1])  # Adjusted widths for better spacing

    # Logo Section
    with col1:
        st.markdown(
            """
            <h3 style='margin-bottom: 0px; font-weight: 800;'>
                <span style='color: black;'>Tech</span>
                <span style='color: red;'>Mahindra</span>
            </h3>
            """,
            unsafe_allow_html=True
        )
    
    # Title Section
    with col2:
        st.markdown(
            "<h3 style='color: red; margin-bottom: 0px;'>Green IT Dashboard</h3>",
            unsafe_allow_html=True
        )

    # Search Bar + Icons Section
    with col3:
            search_query = st.text_input("", placeholder="Search...", label_visibility="collapsed")
    with col4:
        st.markdown(
            """
            <div style='text-align: center;'>
                <a href="#alerts" style="text-decoration: none; font-size: 24px;">🔔</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    # with col5:
    #             st.markdown("<div style='text-align: center;'>👤</div>", unsafe_allow_html=True)
    with col5:
        st.markdown(
            """
            <div style='text-align: center;'>
                <a href="/admin" target="_self" style='text-decoration: none; font-size: 24px;'>👤</a>
            </div>
            """,
            unsafe_allow_html=True
        )


# Function to create a colored block
def colored_block(title, value, color):
    st.markdown(
        f"""
        <div style="
            background-color: {color}; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center;
            color: white;
            font-size: 20px;
            font-weight: bold;">
            {title}<br> <span style="font-size: 28px;">{value}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Title
st.markdown("<h1 style='text-align: center; color: red;'>Tech Mahindra Green IT Dashboard</h1>", unsafe_allow_html=True)

# Metrics Section
col1, col2, col3, col4 = st.columns(4)
with col1:
    colored_block("Hosts", "27", "#4CAF50")  # Green
with col2:
    colored_block("Total Energy Consumption", "16.6304 kWh", "#2196F3")  # Blue
with col3:
    colored_block("Total CO2 Emission", "0.0031 kg CO2", "#FF9800")  # Orange
with col4:
    colored_block("Critical Hosts", "4", "#F44336")  # Red

# Resource Usage Section
st.markdown("### Resource Usage")
col5, col6, col7, col8 = st.columns(4)
with col5:
    colored_block("CPU", "747.70", "#673AB7")  # Purple
with col6:
    colored_block("Disk", "76.00", "#3F51B5")  # Indigo
with col7:
    colored_block("RAM", "6907.10", "#009688")  # Teal
with col8:
    colored_block("Network", "958834.00", "#FF5722")  # Deep Orange

# Alerts Section
# st.markdown("### Alerts")
st.markdown('<h3 id="alerts">Alerts</h3>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="background-color: #E53935; padding: 15px; border-radius: 10px; color: white; font-size: 18px;">
        ⚠ e257na4Ad9: Disk issue detected
    </div>
    """,
    unsafe_allow_html=True
)

# Sample Data for Energy Consumption
energy_data = pd.DataFrame({
    "Host": [f"Host-{i}" for i in range(1, 8)],
    "Energy Consumption (kWh)": [5.2, 4.8, 3.6, 6.1, 7.3, 2.9, 4.5]
})

# Energy Consumption Bar Chart
st.markdown("### Energy Consumption")
fig_energy = px.bar(energy_data, x="Energy Consumption (kWh)", y="Host", orientation='h', color="Energy Consumption (kWh)", color_continuous_scale="greens")
st.plotly_chart(fig_energy, use_container_width=True)

# Sample Data for CO2 Emission
co2_data = pd.DataFrame({
    "Host": [f"Host-{i}" for i in range(1, 5)],
    "CO2 Emission (kg CO2)": [0.0021, 0.0018, 0.0027, 0.0015]
})

# CO2 Emission Bar Chart
st.markdown("### CO2 Emission")
fig_co2 = px.bar(co2_data, x="CO2 Emission (kg CO2)", y="Host", orientation='h', color="CO2 Emission (kg CO2)", color_continuous_scale="blues")
st.plotly_chart(fig_co2, use_container_width=True)


st.title("📰 News on Sustainable Development")



API_TOKEN = "afc04c45a9cc8098742d02b8b9f5d423"  # Replace this with your actual API key
BASE_URL = "https://gnews.io/api/v4/search"


# query = st.text_input("Search News", value="sustainable development OR ESG")
params = {
    "q": "sustainability",
    "lang": "en",
    "max": 9,
    "token": API_TOKEN
}


# Fetch data
response = requests.get(BASE_URL, params=params)


# Fetch data
response = requests.get(BASE_URL, params=params)

# Debug output
# st.write("🔗 Final Request URL:", response.url)
# st.write("⚠️ Status Code:", response.status_code)

# try:
#     st.write("📦 Raw Response:", response.json())
# except Exception as e:
#     st.error(f"Error parsing JSON: {e}")


# if response.status_code == 200:
#     articles = response.json().get("articles", [])
#     cols = st.columns(3)

#     for idx, article in enumerate(articles):
#         with cols[idx % 3]:
#             st.image(article["image"] or "https://via.placeholder.com/400", use_container_width=True)
#             st.subheader(article["title"])
#             st.caption(f"{article['source']['name']} | {article['publishedAt'][:10]}")
#             st.write(article["description"] or "No description available.")
#             st.markdown(f"[Read More]({article['url']})", unsafe_allow_html=True)
# else:
#     st.error("Failed to fetch news. Please check your API token or internet connection.")

import streamlit.components.v1 as components
if response.status_code == 200:
    articles = response.json().get("articles", [])

    html_content = """
    <style>
    .scrolling-wrapper {
        overflow-x: auto;
        display: flex;
        flex-wrap: nowrap;
        gap: 20px;
        padding-bottom: 1rem;
    }
    .card {
        flex: 0 0 auto;
        width: 300px;
        background-color: #f9f9f9;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 1rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .card h4 {
        font-size: 1rem;
        margin: 0 0 0.3rem 0;
        height: 3rem;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    .card p {
        font-size: 0.9rem;
        color: #333;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        margin-bottom: 0.5rem;
    }
    .card a {
        text-decoration: none;
        color: #0066cc;
        font-weight: bold;
    }
    </style>
    <div class="scrolling-wrapper">
    """

    for article in articles:
        image_url = article["image"] or "https://via.placeholder.com/300x200"
        title = article["title"]
        description = article["description"] or "No description available."
        source = article["source"]["name"]
        date = article["publishedAt"][:10]
        url = article["url"]

        html_content += f"""
        <div class="card">
            <img src="{image_url}" alt="news image">
            <h4>{title}</h4>
            <p><i>{source} | {date}</i></p>
            <p>{description[:120]}...</p>
            <a href="{url}" target="_blank">Read more</a>
        </div>
        """

    html_content += "</div>"

    components.html(html_content, height=480, scrolling=True)

else:
    st.error("Failed to fetch news. Please check your API token or internet connection.")