
import geopandas as gpd
from shapely.geometry import Point

def to_geodataframe(df, lon='longitude', lat='latitude', crs='EPSG:4326'):
    df = df.copy()
    df['geometry'] = df.apply(lambda r: Point(r[lon], r[lat]), axis=1)
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs=crs)
    return gdf

def example_choropleth(gdf, key, value_col):
    """Return a GeoDataFrame aggregated by `key` with mean of `value_col` (example)."""
    agg = gdf.dissolve(by=key, aggfunc={value_col: 'mean'})
    return agg
