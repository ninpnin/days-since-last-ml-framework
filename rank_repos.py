import pandas as pd
from transformers import pipeline
import progressbar
classifier = pipeline("text-classification", model="./ml-framework")

df = pd.read_csv("data/aggregated_results.csv")

descriptions = list(df["description"])
descriptions = [item if type(item) == str else "" for item in descriptions]

classes_dict = []
for ix in progressbar.progressbar(range(0, len(descriptions), 16)):
    x = descriptions[ix:ix+16]

    #classes_dict = classes_dict + x
    classes_dict += classifier(x)

assert len(classes_dict) == len(descriptions), f"{len(classes_dict)} classes_dict {len(descriptions)}"

classes = [item["label"] for item in classes_dict]

df["is_framework"] = classes

print(df)
df = df[df["is_framework"] == "yes"]
df = df.sort_values("created_at")
print(df)

df.to_csv("data/frameworks_sorted.csv", index=False)
