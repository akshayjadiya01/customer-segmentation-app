# 🛍️ Customer Segmentation Web App

A **Streamlit-based web application** that segments mall customers into clusters using **KMeans Clustering**. This helps businesses identify distinct customer groups based on their **age**, **annual income**, and **spending behavior**.

---

## 📊 Project Features

- 📂 Upload customer dataset (CSV)
- 🧠 KMeans clustering on Age, Income, and Spending Score
- 🎯 Interactive slider to choose number of clusters
- 📈 Visualize clusters with Seaborn scatter plot
- 💾 Download the segmented customer data
- ✅ Built with Python, Streamlit, Pandas, Scikit-learn, Seaborn, Matplotlib

---

## 📁 Dataset Used

**Mall_Customers.csv**  
Contains 200 mall customers with these features:
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

---

## 🚀 How to Run the App Locally

```bash
# Clone this repository
git clone https://github.com/yourusername/customer-segmentation-app.git
cd customer-segmentation-app

# Install dependencies
pip install streamlit pandas seaborn matplotlib scikit-learn

# Run the app
streamlit run app.py
