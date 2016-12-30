import pandas as pd
import json

out = []
ret = []

def return_drop():
    df = pd.read_csv('customer_dim.csv')
    for e in df.CTM_ID:
        out.append(e)
    out.sort()

    for f in out:
        ret.append({"id": f})
    return json.dumps(ret)
