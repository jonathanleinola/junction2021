import pandas as pd
import plotly.express as px

# Render the data
df1 = pd.read_csv("data/emission_per_eur.csv")

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
