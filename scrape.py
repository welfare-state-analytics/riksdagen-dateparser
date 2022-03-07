import json
import pandas as pd
from pathlib import Path
import progressbar

rows = []
json_files = Path("./data").glob("*.json")
for fpath in progressbar.progressbar(list(json_files)):
    with open(fpath, encoding='utf-8-sig') as f:
        data = json.load(f)

    year = data["dokumentstatus"]["dokument"]["rm"]
    pid = data["dokumentstatus"]["dokument"]["nummer"]
    date = data["dokumentstatus"]["dokument"]["datum"]

    rows.append([year, pid, date])

df = pd.DataFrame(rows, columns=["year", "id", "date"])
df = df.sort_values(["date"])
print(df)

df.to_csv("scraped_dates.csv", index=False)