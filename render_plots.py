import pandas as pd
import plotly.express as px

# Render the data
df1 = pd.read_csv("data/emission_per_eur.csv")
df2 = pd.read_csv("data/preprocessed/raw_materials_example.csv")
df3 = pd.read_csv("data/preprocessed/test.csv")


def plot1():
    fig = px.bar(df1, y='CO2eq_kg', x='Process', width=1000, height=1200)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
    #fig.show()
    return fig

def plot2():
    fig = px.scatter(df1, x="CO2eq_kg", y="Process",
                 width=1000, height=1200)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    return fig

def plot3():
    bubble_size = []
    bubble_size = df2.iloc[:, 2]


    fig = px.scatter(df2, x="SpendEUR", y="Quantity/kg",
                     size="CO2eq_kg", color="CategoryL2",
                     hover_name="ProductName", hover_data=['ProductName', 'SpendEUR', 'Quantity', 'UOM',
                     'VendorCity', 'VendorCountry', 'CategoryL1', 'CategoryL2', 'CO2eq_kg_per_euro',
                     'VendorName','CO2eq_kg', 'Euro/kg'], log_x=True, log_y=True, size_max=60)
    fig.update_traces(mode='markers', marker=dict(sizeref= 2.*max(bubble_size)/(1000**2), line_width=2))

    return fig

def plot4():



    fig = px.scatter(df3, x="SpendEUR", y="Quantity",
                     size="SpendEUR", color="ProductId",
                     hover_name="ProductId", size_max=60)

    return fig
