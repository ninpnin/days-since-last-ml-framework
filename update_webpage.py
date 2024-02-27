import pandas as pd
import datetime

df = pd.read_csv("data/frameworks_sorted.csv")
print(df)
df = df.tail(3).iloc[::-1]

ix = 1

d = {}
for _, row in df.iterrows():
    fullname = row["full_name"]
    created_at = row["created_at"]
    description = row["description"]
    print(ix, fullname, created_at, description)

    d[f"DESCRIPTION{ix}"] = description
    d[f"PROJECT{ix}"] = fullname
    d[f"LINK{ix}"] = f"https://github.com/{fullname}"

    # 2024-02-27T07:45:15Z
    d1 = datetime.datetime.strptime(created_at[:10], '%Y-%m-%d')
    diff = datetime.datetime.utcnow() - d1
    days = diff.days

    d[f"DAYS{ix}"] = str(days)
    ix += 1


print(d)

with open("index_template.html") as f:
    s = f.read()


for k, v in d.items():
    s = s.replace(k, v)

with open("index.html", "w") as f:
    f.write(s)
