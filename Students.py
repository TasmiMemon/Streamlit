import pandas as pd
import streamlit as st

stud = {
    "Name": ['Priyansh', 'Jay', 'Parshwa', 'Pratik', 'Parth', 'Pavitra', 'Gayatree', 'Yash', 'Soumya', 'Fatema'],
    "Marks": [87, 67, 90, 78, 94, 69, 80, 65, 98, 87],
    "Age": [21, 21, 20, 21, 22, 22, 21, 22, 21, 21],
    "City": ["Vadodara", "Vadodara", "Porbandar", "Ankleshwar", "Vadodara", "Rajkot", "Jamnagar", "Vadodara", "Kolkata",
             "Vadodara"]
}
st.set_page_config("Students' Marks")
df = pd.DataFrame(stud)

st.subheader("Students' Marks")

def colorr(val):
    y = df["Marks"].max()
    return ['background-color: yellow']*len(val) if val.Marks == y else ["background_color: white"]*len(val)

st.dataframe(df.style.apply(colorr, axis=1))
