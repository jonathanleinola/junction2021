import pandas as pd
import plotly.express as px

# Render the data
df1 = pd.read_csv("data/emission_per_eur.csv")
df2 = pd.read_csv("data/preprocessed/spend_data_combined.csv")


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
    bubble_size = df2.iloc[:,15]


    fig = px.scatter(df2, x="Quantity", y="SpendEUR",
                     size="total_CO2_for_purchase", color="CategoryL2",
                     hover_name="ProductName", hover_data=['ProductName', 'SpendEUR', 'Quantity',
                     'VendorCity', 'VendorCountry', 'CategoryL1', 'CategoryL2', 'VendorName'],
                     size_max=60, log_x=True)
    fig.update_traces(mode='markers', marker=dict(sizeref= 2.*max(bubble_size)/(100**2)))

    return fig

def plot4():



    fig = px.scatter(df3, x="SpendEUR", y="Quantity",
                     size="SpendEUR", color="ProductId",
                     hover_name="ProductId", size_max=60)

    return fig
