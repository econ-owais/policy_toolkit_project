
import pandas as pd
import statsmodels.formula.api as smf

def diff_in_diff(df, outcome, treat_col, time_col, group_col, covariates=None, post_time=None, cluster_col=None):
    """Run a canonical difference-in-differences OLS with a DID interaction term.
    Returns a fitted results object (statsmodels).
    - df: pandas DataFrame
    - outcome: name of dependent variable
    - treat_col: binary treatment indicator column name
    - time_col: time column (numeric or datetime)
    - group_col: unit identifier for clustering
    - covariates: list of additional covariate column names
    - post_time: explicit threshold time for 'post' indicator (optional)
    """
    df = df.copy()
    if post_time is None:
        # infer the earliest time where treat==1 as post threshold
        try:
            post_time = df.loc[df[treat_col]==1, time_col].min()
        except Exception:
            post_time = None
    if post_time is None:
        raise ValueError('post_time could not be inferred; provide post_time parameter.')

    df['post'] = (df[time_col] >= post_time).astype(int)
    df['did'] = df[treat_col] * df['post']
    formula = f"{outcome} ~ {treat_col} + post + did"
    if covariates:
        formula += ' + ' + ' + '.join(covariates)
    model = smf.ols(formula, data=df)
    if cluster_col:
        res = model.fit(cov_type='cluster', cov_kwds={'groups': df[cluster_col]})
    else:
        res = model.fit()
    return res
