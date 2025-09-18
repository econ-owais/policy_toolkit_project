
import pandas as pd

def load_worldbank_indicator(indicator_code, countries=None, start_year=None, end_year=None):
    """Placeholder loader. Replace with real API call to World Bank or pandas-datareader.
    Returns a tidy pandas DataFrame with columns: country, year, value
    """
    # For now, return an empty frame with expected columns
    df = pd.DataFrame(columns=['country','year','value'])
    return df
