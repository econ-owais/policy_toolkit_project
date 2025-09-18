import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from econ_policy_toolkit.api.worldbank import fetch_indicator

# Set Streamlit page configuration
st.set_page_config(page_title='Econ Policy Toolkit', layout='wide')

# ===== Polished header with project title and your name =====
st.markdown("""
<div style="padding:10px; border:1px solid #ddd; border-radius:5px; background-color:#f9f9f9;">
  <h2 style="margin:0; color:#333;">Econ Policy Toolkit — Demo</h2>
  <p style="margin:0; color:#666; font-size:14px;">Created by Owais Ali Shah</p>
</div>
<hr>
""", unsafe_allow_html=True)

# Main app title (optional, you can remove if redundant)
st.title("Econ Policy Toolkit — Demo")

# ===== Language selection =====
lang = st.sidebar.selectbox("Language / زبان", ["English", "اردو"])
if lang == "اردو":
    st.markdown("""<div dir='rtl'>خوش آمدید — یہ ایک ڈیمو ہے۔ نیچے آپ ورلڈ بینک انڈیکیٹر لوڈ کر سکتے ہیں۔</div>""", unsafe_allow_html=True)
else:
    st.markdown("""Welcome — this is a demo. Use the sidebar to load World Bank indicators (cached).""")

# ===== Sidebar inputs =====
st.sidebar.header("World Bank indicator (cached)")
indicator = st.sidebar.text_input('Indicator code', value='SP.POP.TOTL')
start = st.sidebar.number_input('Start year', value=2000, min_value=1960, max_value=2025)
end = st.sidebar.number_input('End year', value=2020, min_value=1960, max_value=2025)
refresh = st.sidebar.checkbox('Refresh cache', value=False)

# ===== Fetch and display indicator =====
if st.sidebar.button('Load indicator'):
    with st.spinner('Fetching...'):
        try:
            df = fetch_indicator(indicator, start=start, end=end, refresh=refresh)
            st.success(f'Fetched {len(df)} rows (showing top 20)')
            st.dataframe(df.head(20))

            # Quick aggregate and plot for a selected country
            country = st.selectbox('Select country', options=sorted(df['country'].dropna().unique())[:50])
            if country:
                series = df[df['country']==country].set_index('year')['value'].sort_index()
                fig, ax = plt.subplots(figsize=(8,3))
                series.plot(ax=ax)
                ax.set_title(f"{indicator} — {country}")
                ax.set_ylabel('Value')
                st.pyplot(fig)
        except Exception as e:
            st.error(f'Error fetching data: {e}')
