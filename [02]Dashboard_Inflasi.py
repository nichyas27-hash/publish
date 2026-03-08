import pandas as pd
import streamlit as st
import plotly.express as px
from st_aggrid import GridOptionsBuilder, AgGrid
from streamlit_option_menu import option_menu
from pathlib import Path

st.set_page_config(
    page_title='Dashboard Inflasi Kota Surabaya',
    layout='wide',
    page_icon='bar-chart'
)
import streamlit as st
from pathlib import Path

css_path = Path(__file__).parent / "style.css"
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
df = pd.read_excel(
    'C:/Users/Lenovo/Desktop/BearLearn/[03] KERJA PRAKTIK/[02]Data_Awal/[02]Series Inflasi Kota Surabaya 2025/[02]Inflasi Kota Surabaya 2025.xlsx',
    sheet_name='Inflasi',
)
df_yoy = pd.read_excel(
    'C:/Users/Lenovo/Desktop/BearLearn/[03] KERJA PRAKTIK/[02]Data_Awal/[02]Series Inflasi Kota Surabaya 2025/[02]Inflasi Kota Surabaya 2025.xlsx',
    sheet_name='y-o-y',
)
yoy = pd.read_excel(
    'C:/Users/Lenovo/Desktop/BearLearn/[03] KERJA PRAKTIK/[02]Data_Awal/[02]Series Inflasi Kota Surabaya 2025/[02]Inflasi Kota Surabaya 2025.xlsx',
    sheet_name='YoY',
)
df_mom = pd.read_excel(
    'C:/Users/Lenovo/Desktop/BearLearn/[03] KERJA PRAKTIK/[02]Data_Awal/[02]Series Inflasi Kota Surabaya 2025/[02]Inflasi Kota Surabaya 2025.xlsx',
    sheet_name='m-o-m',
)
mom = pd.read_excel(
    'C:/Users/Lenovo/Desktop/BearLearn/[03] KERJA PRAKTIK/[02]Data_Awal/[02]Series Inflasi Kota Surabaya 2025/[02]Inflasi Kota Surabaya 2025.xlsx',
    sheet_name='MoM',
)
yoy['Tahun'] = pd.to_datetime(yoy['Tahun'])
mom['Bulan'] = pd.to_datetime(mom['Bulan'])

fig1 = px.line(
    yoy,
    x='Tahun',
    y='Nilai',
    template='ggplot2',
)
fig2 = px.line(
    mom, 
    x='Bulan',
    y='Nilai',
    template='seaborn'
)
st.title('DASHBOARD INFLASI KOTA SURABAYA')
with st.container():
    col1, col2, col3 = st.columns([1,1,1])
    col1.metric('Inflasi (Desember 2025)', '2.96%')
    col2.metric('Inflasi M-o-M', '0.80%', '+0.59')
    col3.metric('Inflasi Y-o-Y (per Januari)', '0.91%', '-1.49')

with st.container():
    with st.sidebar:
        selected = option_menu(
            'Menu',['Dashboard', 'Tabel Statistik'],
            menu_icon='house',
            icons=['bar-chart', 'table'],
            default_index=0,
        )
if selected == 'Dashboard':
    st.subheader('Tren Inflasi Y-o-Y', anchor='yoy')
    st.plotly_chart(
        fig1, 
        use_container_width=True,
        theme='streamlit',
    )
    st.subheader('Tren Inflasi M-o-M', anchor='mom')
    st.plotly_chart(
        fig2,
        use_container_width=True,
        theme='streamlit',
    )
if selected == 'Tabel Statistik':
    with st.container():
        st.subheader('Tabel Inflasi Kota Surabaya', anchor='tabel0')
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(
            filter=True,
            sortable=True,
            editable=True,
            enableGroupRow=True,
            enableValue=True,
            enablePivot=True,
        )
        gb.configure_side_bar(
            filters_panel=True,
            columns_panel=True,
        )
        gridoption = gb.build()
        AgGrid(df, gridoption, enable_enterprise_modules=True)
    with st.container():
        tab1, tab2 = st.tabs(['Tabel Inflasi Inflasi Y-o-Y', 'Tabel Inflasi M-o-M'])
        with tab1: 
            st.subheader('Tabel Inflasi Y-o-Y', anchor='tabel1')
            gb1 = GridOptionsBuilder.from_dataframe(df_yoy)
            gb1.configure_default_column(
                filter=True,
                sortable=True,
                editable=True,
                enableGroupRow=True,
                enableValue=True,
                enablePivot=True,
            )
            gb1.configure_side_bar(
                filters_panel=True,
                columns_panel=True,
            )
            gridoption1 = gb1.build()
            AgGrid(df_yoy, gridoption1, enable_enterprise_modules=True)
        with tab2: 
            st.subheader('Tabel Inflasi M-o-M', anchor='tabel2')
            gb2 = GridOptionsBuilder.from_dataframe(df_mom)
            gb2.configure_default_column(
                filter=True,
                sortable=True,
                editable=True,
                enableGroupRow=True,
                enableValue=True,
                enablePivot=True,
            ) 
            gb2.configure_side_bar(
                filters_panel=True,
                columns_panel=True,
            )
            gridoption2 = gb2.build()
            AgGrid(df_mom, gridoption2, enable_enterprise_modules=True)

with st.container():
    st.markdown(
    """
    <div style='text-align:center; background-color:#c45824; padding:10px; border-radius: 5px'>
    <div style='display:flex; justify-content:space-around; position:relative; top:10px'>
        <p style='color:#fffbee'> © 2026 Dashboard Inflasi Kota Surabaya </p>
        <p style='color:#fffbee'> Referensi Badan Pusat Statistik Kota Surabaya </p> 
    </div>
    <div style='display:flex; justify-content:space-around'>
        <p style='color:#fffbee'> Powered by Streamlit </p>
        <p style='color:#fffbee'> Created by Jaya Perkasa </p>
    </div>

    """, unsafe_allow_html=True)



