stocks={
    'GOOG':434,#Google
    'AAPL':325,#Apple
    'FB':54,#Facebook
    'AMZN':623,#Amazon
    'F':32,#Ford
    'MSFT':549#Microsoft
}
zip(stocks)#getting a parallel list ends up with (434,'GOOG')
a=min(zip(stocks.values(),stocks.keys()))
#print(a,stocks.keys())
print(a)
