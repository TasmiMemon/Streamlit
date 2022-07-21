import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Sales Dashboard',
                   layout='wide')

df = pd.read_csv(r'C:\Users\asus\Downloads\Masked_Excel_DB.csv')

# ----SIDEBAR----
st.sidebar.header('Please filter here:')
shift = st.sidebar.multiselect(
    'Select the shift:',
    options=df['shift'].unique(),
    default=df['shift'].unique()
)

customer = st.sidebar.multiselect(
    'Select the customer:',
    options=df['customer'].unique(),
    default=df['customer'].unique()
)

towel_type = st.sidebar.multiselect(
    'Select the type of towel:',
    options=df['Towel_type'].unique(),
    default=df['Towel_type'].unique()
)

df_selection = df.query(
    "shift == @shift & customer == @customer & Towel_type == @towel_type"
)

# ----MAINPAGE----
st.title(":bar_chart: Sales Dashboard")
st.markdown('##')

st.subheader("Data Table")
st.dataframe(df_selection)

# BAR CHART'S
emp_atc = (
    df_selection.groupby(by=['emp_name']).sum()[['ATC_quantity']].sort_values(by="ATC_quantity")
)

fig_sales = px.bar(
    emp_atc,
    x='ATC_quantity',
    y=emp_atc.index,
    orientation='h',
    title='<b>ATC vs Operator</b>',
    color_discrete_sequence=['#008388'] * len('ATC_quantity'),
    template='plotly_white',
)

style_atc = (
    df_selection.groupby(by=['style']).sum()[['ATC_quantity']].sort_values(by="ATC_quantity")
)

fig_sales_sa = px.bar(
    style_atc,
    y='ATC_quantity',
    x=style_atc.index,
    orientation='v',
    title='<b>ATC vs Style</b>',
    color_discrete_sequence=['#008388'] * len('ATC_quantity'),
    template='plotly_white',
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_sales, use_container_width=True)
right_column.plotly_chart(fig_sales_sa, use_container_width=True)

# LINE CHART
line_chart = px.line(df_selection, x='ztime', y='ATC_quantity', color='emp_name')

# SUNBURST
sunfig = px.sunburst(df_selection, path=['customer', 'Towel_type', 'style', 'emp_name'], values='ATC_quantity', color='style', color_discrete_map={'Amazon':'black', 'Bath':'darkblue'})

left_column, right_column = st.columns(2)
left_column.plotly_chart(line_chart, use_container_width=True)
right_column.plotly_chart(sunfig, use_container_width=True)
