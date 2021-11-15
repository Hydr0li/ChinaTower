import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import datetime
import math

df = pd.read_excel('预付电费明细.xlsx')
df = df.sort_values(['站点编码','电表ID', '购电起始日期'], ascending=[False, False, True])
df = df.reset_index()
df['时间不连续'] = 0
df['读数不连续'] = 0
start_date = df['购电起始日期'].isna()
end_date = df['购电截止日期'].isna()
start_reading = df['购电起始读数'].isna()
end_reading = df['购电截止读数'].isna()
for row in df.index:
    if start_date[row] == True:
        df['时间不连续'][row] = 1
    if end_date[row] == True:
        df['时间不连续'][row] = 1
    if start_reading[row] == True:
        df['读数不连续'][row] = 1
    if end_reading[row] == True:
        df['读数不连续'][row] = 1
df['购电起始日期'] = df['购电起始日期'].fillna(0)
df['购电截止日期'] = df['购电截止日期'].fillna(0)
df['购电起始日期'] = df['购电起始日期'].values.astype('datetime64[D]')
df['购电截止日期'] = df['购电截止日期'].values.astype('datetime64[D]')
for row in range(len(df)-1):
    if df['电表ID'][row] == df['电表ID'][row+1]:
        reading_delta = df['购电起始读数'][row+1] - df['购电截止读数'][row]
        time_delta = (df['购电起始日期'][row+1] - df['购电截止日期'][row]).days
        if reading_delta != 0:
            df['读数不连续'][row+1] = 1
        if time_delta > 1:
            df['时间不连续'][row+1] = 1
df['站点编码'] = df['站点编码'].astype('str')
df.to_excel('1_连续性测试.xlsx')
