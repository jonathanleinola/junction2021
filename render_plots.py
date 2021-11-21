import pandas as pd
import plotly.express as px
import streamlit as st

from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3

# Render the data
df1 = pd.read_csv("data/emission_per_eur.csv")
df2 = pd.read_csv("data/preprocessed/spend_data_combined.csv")
df4 = pd.read_csv("data/preprocessed/spend_data_combined.csv")

def plot4():
    fig = px.bar(df4, y='CO2eq_kg', x='CategoryL2')
    fig.update_layout(barmode='overlay', xaxis={'categoryorder':'max ascending'})
    
    return fig

def plot3():
    df3 = pd.read_csv("data/preprocessed/spend_data_combined.csv")
    df3['VendorCountry'] = df3.VendorCountry.apply(lambda x: country_name_to_country_alpha3(country_alpha2_to_country_name(x.split()[0])))
    df3 = df3[df3["SpendEUR"] >= 0]
    df3["SpendEUR"] = df3["SpendEUR"].astype(int)
    fig = px.scatter_geo(df3, locations="VendorCountry", color ="VendorCountry",
                        hover_name="CategoryL2", size="SpendEUR", hover_data=['SpendEUR', 'Quantity',
                     'VendorCity', 'VendorCountry', 'CategoryL1', 'ProductName', 'VendorName'],
                        projection="natural earth")

    return fig

def plot2():
    bubble_size = []
    bubble_size = df2.iloc[:, 10]


    fig = px.scatter(df2, x="Quantity", y="SpendEUR",
                     size="total_CO2_for_purchase", color="CategoryL2",
                     hover_name="ProductName", hover_data=['SpendEUR', 'Quantity',
                     'VendorCity', 'VendorCountry', 'CategoryL1', 'CategoryL2', 'VendorName'],
                     size_max=100, log_x=True)
    fig.update_traces(mode='markers', marker=dict(sizeref= 2.*max(bubble_size)/(100**2)))

    return fig

def plot1():
    fig = px.pie(df1.nsmallest(5, ["CO2eq_kg"]), values='CO2eq_kg', names='Process', width=1000, height=500)
    return fig
