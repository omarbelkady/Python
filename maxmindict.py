
stocks={'GOOG':491.24,
        'FB':2141.45,
        'YAHOO':321.29,
        'AMZN':312.21,
        'AAPL':149.34
}
#maximum
a=max(zip(stocks.values(),stocks.keys()))
#sorted alphabetically
b=sorted(zip(stocks.values(),stocks.keys()))
#minimum
c=min(zip(stocks.values(),stocks.keys()))
print(a)
print(b)
print(c)
