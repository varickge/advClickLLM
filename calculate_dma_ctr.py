import pandas as pd

# Load data
data = pd.read_csv('./data/data.csv')

# Calculate clicks and impressions for each DMA
dma_results = data.groupby('mm_dma')['tag'].agg(['count', lambda x: (x.str.contains('click')).sum()]).rename(columns={'count': 'impressions', '<lambda_0>': 'clicks'})

# Calculate CTR for each DMA
dma_results['CTR'] = dma_results['clicks'] / dma_results['impressions']

# Sort DMAs by CTR in descending order
ordered_dma_results = dma_results.sort_values('CTR', ascending=False).reset_index()

# Display top 10 DMAs in ordered list of (DMA, CTR)
top_10_dmas = ordered_dma_results.head(10)
print(top_10_dmas[['mm_dma', 'CTR']])
