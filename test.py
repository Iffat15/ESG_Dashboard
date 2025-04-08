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
