import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime
from pandas.api.types import CategoricalDtype
import calendar

df = pd.read_csv("processed_clean_df.csv")

st.set_page_config("Heat Map", layout="wide")

st.title("Heat Map")

st.subheader("Data Table")
st.dataframe(df)

hmp = df.copy()
hmp["date"] = hmp['date'].astype("datetime64[ns]")
hmp["T_time"] = hmp['T_time'].astype("datetime64[ns]")
hmp["Hour"] = hmp["T_time"].dt.hour
hmp["Weekday"] = hmp["date"].dt.day_name()
hmp['Weekday'] = hmp['Weekday'].astype("category")
st.dataframe(hmp)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hmp1 = CategoricalDtype(categories=weekdays, ordered=True)
hmp['Weekday'] = hmp['Weekday'].astype(hmp1)
heat_map = (hmp.groupby('Weekday').Hour.value_counts().unstack().fillna(0))
heat_map.T
fig, ax = plt.subplots()
sns.heatmap(heat_map.T, cmap="Reds", linewidth=1, fmt=".0f", ax=ax)
st.write(fig)
