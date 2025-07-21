import streamlit as st
import pandas as pd
import datetime
from main import run_all

st.set_page_config(page_title="Influencer Monitoring AI", layout="wide")
st.title("📊 Influencer Monitoring AI Dashboard")

st.markdown("""
Welcome to the AI Agent Hackathon project dashboard!
This tool monitors influencer content from **LinkedIn** and **YouTube**, summarizes it, and lets you analyze trends easily.
""")

st.markdown("---")

# Run button
if st.button("🚀 Run Agent Now"):
    with st.spinner("Running the monitoring pipeline..."):
        run_all()
    st.success("✅ Agent run completed!")

# Dummy summary data for display (replace with actual output from summarizer)
summary_data = [
    {"Platform": "YouTube", "Influencer": "Ali Abdaal", "Summary": "Tips on productivity using Notion", "Date": datetime.date.today()},
    {"Platform": "LinkedIn", "Influencer": "Naval Ravikant", "Summary": "Thoughts on building wealth in 2025", "Date": datetime.date.today()}
]
df = pd.DataFrame(summary_data)

st.subheader("📄 Latest Summaries")
st.dataframe(df, use_container_width=True)

# Download summary CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download as CSV",
    data=csv,
    file_name='influencer_summary.csv',
    mime='text/csv'
)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Team [Your Team Name] for the AI Agent Hackathon.")
