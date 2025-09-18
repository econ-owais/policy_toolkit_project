
import requests
import pandas as pd
import os

def worldbank_api_indicator(indicator_code, countries='all', start=2000, end=2020):
    """Simple World Bank API fetcher (no pagination robustness)."""
    base = 'http://api.worldbank.org/v2/country/all/indicator/{}'
    url = base.format(indicator_code)
    params = {'date': f'{start}:{end}', 'format':'json', 'per_page':1000}
    resp = requests.get(url, params=params, timeout=30)
    if resp.status_code != 200:
        raise ConnectionError(f'World Bank API error: {resp.status_code}')
    data = resp.json()
    # data[1] contains the rows (if successful)
    rows = data[1] if len(data) > 1 else []
    df = pd.json_normalize(rows)
    return df
