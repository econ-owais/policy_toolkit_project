try:
    import geopandas as gpd
    HAS_GPD = True
except ImportError:
    HAS_GPD = False

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from econ_policy_toolkit.api.worldbank import fetch_indicator

st.set_page_config(page_title='Econ Policy Toolkit', layout='wide')
st.title("Econ Policy Toolkit — Demo")

lang = st.sidebar.selectbox("Language / زبان", ["English", "اردو"])
if lang == "اردو":
    st.markdown("""<div dir='rtl'>خوش آمدید — یہ ایک ڈیمو ہے۔ نیچے آپ ورلڈ بینک انڈیکیٹر لوڈ کر سکتے ہیں۔</div>""", unsafe_allow_html=True)
else:
    st.markdown("""Welcome — this is a demo. Use the sidebar to load World Bank indicators (cached).""")

st.sidebar.header("World Bank indicator (cached)")
indicator = st.sidebar.text_input('Indicator code', value='SP.POP.TOTL')
start = st.sidebar.number_input('Start year', value=2000, min_value=1960, max_value=2025)
end = st.sidebar.number_input('End year', value=2020, min_value=1960, max_value=2025)
refresh = st.sidebar.checkbox('Refresh cache', value=False)

if st.sidebar.button('Load indicator'):
    with st.spinner('Fetching...'):
        try:
            df = fetch_indicator(indicator, start=start, end=end, refresh=refresh)
            st.success(f'Fetched {len(df)} rows (showing top 20)')
            st.dataframe(df.head(20))
            # quick aggregate and plot for a selected country
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
