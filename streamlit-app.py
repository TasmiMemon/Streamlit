import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

def main():

    st.title("Learning charts")

    df = pd.read_csv(r'C:\Users\asus\Downloads\Masked_Excel_DB.csv')

    st.write(df.head())

    st.subheader('Style vs ATC')
    sty_atc = pd.DataFrame({'style': list(df['style'].unique()),
                            'ATC_quantity': df.groupby(['style', 'customer'])['ATC_quantity'].sum(),
                            },
                           columns=['Amazon', 'Flipkart'])

    chart = alt.Chart(df).mark_bar().encode(
        x='style',
        y='ATC_quantity',
        color='customer'
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader('Operator vs ATC')
    emp_atc = pd.DataFrame({'emp_name': list(df['emp_name'].unique()),
                            'ATC_quantity': df.groupby(['emp_name', 'customer'])['ATC_quantity'].sum(),
                            },
                           columns=['Flipkart', 'Amazon'])

    bchart = alt.Chart(df).mark_bar().encode(
        x='emp_name',
        y='ATC_quantity',
        color='customer'
    )
    st.altair_chart(bchart, use_container_width=True)

    st.header('Line chart')
    st.subheader('stock vs ATC')

    stock_atc = pd.DataFrame({
        'stock': df.current_stock,
        'ATC_quantity': df.ATC_quantity
    })

    lchart = alt.Chart(df).mark_line().encode(
        x='current_stock',
        y='ATC_quantity'
    )
    st.altair_chart(lchart, use_container_width=True)

    st.header('Pie Chart')
    st.subheader('Towel_type vs ATC')

    labels = df['Towel_type'].unique()
    sizes = df.groupby(['Towel_type'])['ATC_quantity'].sum()

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    st.header('Donut chart')
    st.subheader('Operator vs ATC')

    labels1 = ['Alex', 'Charles', 'Jack', 'John', 'Kevin', 'Micheal', 'Thomas', 'Robert']
    sizes1 = df.groupby(['emp_name'])['ATC_quantity'].sum()

    plt.pie(sizes1, labels=labels1, autopct="%1.1f%%", shadow=False, startangle=90)
    plt.axis('equal')

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig2 = plt.gcf()
    fig2.gca().add_artist(centre_circle)

    st.pyplot(fig2)
