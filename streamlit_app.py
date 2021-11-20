from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

from render_plots import *


"""
# Grandma's JaGucci
"""
st.sidebar.header('Insert some fancy title')
menu = st.sidebar.radio(
    "",
    ("H1", "H2", "H3", 'H4', "H5", "H6"),
)

if menu == "H1":
    st.write(plot1())
elif menu == "H2":
    st.write(plot2())
elif menu == "H3":
    st.write(plot3())
elif menu == "H4":
    st.write(plot4())
