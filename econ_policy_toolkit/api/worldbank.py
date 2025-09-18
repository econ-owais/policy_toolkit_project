
"""World Bank API connector with simple file caching.
Note: For large-scale production use, replace with a robust client and error handling.
"""
import requests, time, json, os
import pandas as pd
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / 'data' / 'cache'
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def fetch_indicator(indicator_code, countries='all', start=2000, end=2020, refresh=False):
    """Fetch indicator from World Bank API and return tidy DataFrame.
    Caches results in data/cache to avoid repeated HTTP calls during demos.
    """
    fname = CACHE_DIR / f"wb_{indicator_code}_{start}_{end}.json"
    if fname.exists() and not refresh:
        try:
            data = json.loads(fname.read_text(encoding='utf-8'))
            return _normalize_rows(data)
        except Exception:
            pass

    url = f'https://api.worldbank.org/v2/country/all/indicator/{indicator_code}'
    params = {'date': f'{start}:{end}', 'format':'json', 'per_page':10000}
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    # Save cache
    try:
        fname.write_text(json.dumps(data), encoding='utf-8')
    except Exception:
        pass
    return _normalize_rows(data)

def _normalize_rows(data):
    # data expected as [metadata, rows]
    rows = data[1] if isinstance(data, list) and len(data) > 1 else []
    df = pd.json_normalize(rows)
    if df.empty:
        return pd.DataFrame(columns=['country.value','country.id','date','value'])
    df = df.rename(columns={ 'country.value':'country', 'country.id':'country_code', 'date':'year'})
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df[['country','country_code','year','value']].sort_values(['country','year'])
