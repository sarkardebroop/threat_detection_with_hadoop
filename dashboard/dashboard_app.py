import streamlit as st
import pandas as pd
from pyhive import hive  

USE_HIVE = True  
CSV_FILE_PATH = "detected_threats.csv"  
HIVE_QUERY = "SELECT * FROM threat_detection.detected_threats"

def load_data():
    if USE_HIVE:
        try:
            conn = hive.Connection(host='localhost', port=10000, username='hadoop')
            df = pd.read_sql(HIVE_QUERY, conn)
            return df
        except Exception as e:
            st.error(f"Error connecting to Hive: {e}")
            return pd.DataFrame()
    else:
        try:
            return pd.read_csv(CSV_FILE_PATH)
        except FileNotFoundError:
            st.warning("CSV file not found.")
            return pd.DataFrame()

def main():
    st.set_page_config(page_title="Threat Detection Dashboard", layout="wide")
    st.title("Threat Detection Dashboard")

    df = load_data()

    if df.empty:
        st.warning("No data")
        return

    st.markdown("### Summary Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric(" Total Threats", len(df))
    col2.metric(" Unique IPs", df['ip'].nunique())
    col3.metric(" Threat Types", df['threat_type'].nunique())

    st.divider()

    st.markdown("### Threat Type Distribution")
    threat_counts = df['threat_type'].value_counts()
    st.bar_chart(threat_counts)

    st.markdown("### Threats by IP Address")
    ip_counts = df['ip'].value_counts().head(10)
    st.bar_chart(ip_counts)

    st.markdown("### Raw Threat Log")
    st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
