import pandas as pd
prices=[[16,27,33],[42,95,96],[23,35,58],[50,18,39],[32,67,98],[24,67,22],[23,35,58],[50,18,39]]
dataframe = pd.DataFrame(prices)
print(dataframe)
headers_dataframe = pd.DataFrame(prices,columns=['jan','feb','march'])
print(headers_dataframe)
print(headers_dataframe['jan'][3])
print(headers_dataframe.head()) #prints 1st 5 rows
print(headers_dataframe.tail()) #prints last 5 rows
print(headers_dataframe.head(3))
print(headers_dataframe.tail(3))




import quandl

dataset = quandl.get('FINRA/FORF_TLLTD')

print(dataset)
print(dataset['ShortVolume'])

for i in range(4):
    print(dataset['ShortVolume'][i])

df=quandl.get('WIKI/GOOGL')
print(df)
print(df.head())

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume',]]
print(df.head())