import pandas as pd
import quandl

df = quandl.get("XNSE/STRTECH")

print(df.head())
#
# df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
#
# df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
#
# df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#
# df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
#
# print(df.head())