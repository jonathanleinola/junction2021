from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px
from render_plots import *

st.set_page_config(layout="wide")
"""
# Lead to Sustainable Future with Sievo
"""

left_col, right_col = st.columns(2)

left_col.header("CO2 emissions for each product")
left_col.write(plot2())

right_col.header("CO2 equivalent kg per 1 euro spent")
right_col.write(plot4())


left_col.header("Five most polluting processes")
left_col.write(plot1())

right_col.header("Emissions on a map")
right_col.write(plot3())