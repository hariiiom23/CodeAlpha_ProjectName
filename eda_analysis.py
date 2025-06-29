
import pandas as pd
from collections import Counter

# Step 1: Load the dataset
df = pd.read_csv("quotes.csv")

# Step 2: Explore structure
print("📊 DataFrame Info:")
print(df.info())

print("\n🔍 First 5 Rows:")
print(df.head())

# Step 3: Unique authors
print("\n🧠 Unique Authors Count:", df['Author'].nunique())
print("Authors:", df['Author'].unique())

# Step 4: Most frequent authors
print("\n🔥 Top Authors by Number of Quotes:")
print(df['Author'].value_counts())

# Step 5: Most common tags
all_tags = ", ".join(df['Tags']).split(", ")
tag_counts = Counter(all_tags)
print("\n🏷️ Top Tags:")
print(tag_counts.most_common(5))
