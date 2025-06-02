import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
# write headline
st.title ("Worldwide Analysis of Quality of Life and Economic Factors")
st.header("This app enables you to explore the relationships between poverty, life expectancy, and GDP across various countries and years. Use the panels to select options and interact with the data.")

tab1,tab2,tab3=st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])


with tab3:
    st.subheader("Data Explorer")
    st.write("Global data for selected time range")
    # Load the CSV using pandas
    df = pd.read_csv('https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv')

    # Display in Streamlit

    st.dataframe(df)
    countries = sorted(df['country'].unique())
    selected_countries = st.multiselect("Select countries", countries, default=countries[:3])
    years = sorted(df['year'].unique())
    selected_years = st.slider("Select year range", min_value=min(years), max_value=max(years), value=(min(years), max(years)))
    if selected_countries:
        filtered_df = df[
           (df['country'].isin(selected_countries)) &
           (df['year'].between(selected_years[0], selected_years[1]))
        ]
        st.dataframe(filtered_df)
        st.download_button("Download data", filtered_df.to_csv(index=False), file_name="filtered_data.csv")
    else:
        st.warning("Please select at least one country")


