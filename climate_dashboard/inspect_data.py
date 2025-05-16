import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    return pd, px


@app.cell
def _(pd):
    df = pd.read_csv("climate_dashboard/data/realistic_ocean_climate_dataset.csv")
    df.Date = pd.to_datetime(df.Date)
    df
    return (df,)


@app.cell
def _(df):
    df.Date.max()
    print(f"Minimum date is {df.Date.min()}, maximum date is {df.Date.max()}")
    return


@app.cell
def _(df, px):
    _df = df[df.Date.dt.year == 2015]

    _df = _df.groupby(["Location"]).aggregate({"Species Observed": "mean", "pH Level": "mean",  "Latitude": "first", "Longitude": "first", "Location": "first"})

    fig = px.scatter_geo(_df,
                         lat="Latitude",
                         lon="Longitude",
                         size="Species Observed",
                         text="Location",
                         title="Number of Species observed in 2015")
    fig.show()
    return


@app.cell
def _(df, px):
    _df = df[df.Location == "Red Sea"]

    _fig = px.line(df, x="Date", y="SST (°C)", title='Temperature evolution by Location', color="Location")

    _fig.show()
    return


if __name__ == "__main__":
    app.run()
