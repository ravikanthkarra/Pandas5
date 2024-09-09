import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = scores[['score']].sort_values('score', ascending=False)
    result['rank'] = result['score'].rank(method='dense', ascending=False)
    return result
