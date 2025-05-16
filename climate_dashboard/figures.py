from dataclasses import dataclass
from typing import Self
import pandas as pd
import plotly.express as px

@dataclass
class DataTransformer:
    df: pd.DataFrame
    @classmethod
    def get_data(cls, path: str):
        df = pd.read_csv(path)
        df.Date = pd.to_datetime(df.Date)
        return cls(df)
    def yearly_aggregation(self, year: int):
        df = self.df[self.df.Date.dt.year == year]
        df = self.df.groupby(["Location"]).aggregate({
            "Species Observed": "mean", 
            "pH Level": "mean",  
            "Latitude": "first", 
            "Longitude": "first", 
            "Location": "first"
            })
        return df

def bubble_map_species_by_year(year: int):
    data_path = "data/realistic_ocean_climate_dataset.csv"
    transformer = DataTransformer.get_data(data_path)
    df = transformer.yearly_aggregation(year)

    fig = px.scatter_geo(df,
                     lat="Latitude",
                     lon="Longitude",
                     size="Species Observed",
                     text="Location",
                     title=f"Number of Species observed in {year}")
    return fig