# Create sample_data.py
import pandas as pd

sample_articles = [
    {"text": "Stock market surges on positive economic news", "sentiment": "positive"},
    {"text": "Company faces major scandal and losses", "sentiment": "negative"},
    {"text": "Technology breakthrough announced by researchers", "sentiment": "positive"},
    {"text": "Market crash wipes out billions in value", "sentiment": "negative"},
    {"text": "New policy could boost economic growth", "sentiment": "positive"},
    # Add 10-20 more examples
]

df = pd.DataFrame(sample_articles)
df.to_csv('data/test_articles.csv', index=False)
print("✅ Test data created")
