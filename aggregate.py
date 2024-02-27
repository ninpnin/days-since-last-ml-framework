import pandas as pd
from pathlib import Path
import json

columns = ["name", "full_name", "description", "created_at"]
rows = []
for p in Path("data").glob("results*.json"):
    with p.open() as f:
        d = json.load(f)
    
    for item in d["items"]:
        print(item.keys())

        row = []
        for col in columns:
            value = item[col]
            if type(value) == str:
                value = value[:500]
                value = value.encode("ascii", errors="ignore").decode()
            row.append(value)

        rows.append(row)


df = pd.DataFrame(rows, columns=columns)
df = df.sort_values("created_at", ascending=False)
print(df)

df.to_csv("data/aggregated_results.csv", index=False)

sample = df.sample(n=100)
sample["framework"] = ""
sample = sample[["framework", "description"]]

sample.to_csv("data/sample.csv", index=False)
