import pandas as pd

df = pd.read_csv('data/wingmag-data-130k-v2.csv.zip')
summary_df = df. groupby('country').agg({'title': 'count', 'points': 'mean'}).round(1)
summary_df = summary_df.rename(colums ={'title': 'count'}).reset_index()
summary_df = summary_df.sort_values('count', ascending=False)
summary_df.to_cvs('data/reviews-per-country.cvs', index=False)


