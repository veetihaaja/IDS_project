import json
import datetime
import pandas as pd

data = json.load(open('archive.json'))

time = data['timestamps']
DTtime = [datetime.datetime.fromtimestamp(ts) for ts in time]
temp1 = data['temperature1']
temp1 = [round(t, 2) for t in temp1]

temp2 = data['temperature2']
temp2 = [round(t, 2) for t in temp2]

df = pd.DataFrame({
    'Time': DTtime,
    'Temperature 1 (left pan)': temp1,
    'Temperature 2 (right pan)': temp2
})

df.to_csv('processed_data.csv', index=False)