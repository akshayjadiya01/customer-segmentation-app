# Streamlit app for customer segmentation
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Customer Segmentation App", layout="centered")

st.title("🛍️ Mall Customer Segmentation")
st.markdown("Upload a customer dataset and discover natural customer groups using KMeans clustering.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.replace(' ', '_')

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # Features
    features = ['Age', 'Annual_Income_(k$)', 'Spending_Score_(1-100)']

    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # Choose number of clusters
    k = st.slider("Select number of clusters", 2, 10, 5)

    # KMeans clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    st.subheader("🧠 Cluster Averages")
    st.dataframe(df.groupby('Cluster')[features].mean())

    # Cluster plot
    st.subheader("📊 Clustering Visualization")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x='Annual_Income_(k$)',
        y='Spending_Score_(1-100)',
        hue='Cluster',
        palette='Set2',
        data=df,
        s=100,
        ax=ax
    )
    st.pyplot(fig)

    # Download segmented file
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Segmented Data", data=csv, file_name="segmented_customers.csv", mime='text/csv')

else:
    st.info("👈 Upload a dataset to get started.")
