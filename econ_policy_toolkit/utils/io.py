
import pandas as pd

def to_stata(df, path, convert_dates=True):
    df.to_stata(path, write_index=False)

def save_geojson(gdf, path):
    gdf.to_file(path, driver='GeoJSON')
