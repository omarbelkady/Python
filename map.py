income=[10,30,75]
def triple_money(dollars):
	return dollars*3
#map(functionName,listyouwanttoitteratethrough)
a=map(triple_money,income)
new_income=list(a)
print(new_income)
