import pandas as pd

data = {
    "Name" : ["Dinesh", "Denanath", "Ponmudi", "Divya"],
    "Age" : [19, 18, 18, 18],
    "Marks" : [80, 82, 79, 86]
}

df = pd.DataFrame(data)

print(df)
