from collections import Counter

text= "(According to Marx), competition forces capitalist firms" \
    "to invest their profits in labour-saving machinery," \
    "for if they do not do this their efficiency will drop, and" \
    "they will be forced out of business. However, if labour-saving machinery " \
    "is installed, there will be a fall in employment, and hence a rise " \
    "in the number of the unemployed. As unemployment rises, wages " \
    "(if not already at subsistence level) will tend to fall – " \
    "for those who still have jobs will be forced by the capitalists" \
    "to accept lower wages under threat of being replaced by the “reserve army”" \
    "of the unemployed. Yet according to Marx, a fall in employment also meant a" \
    "fall in profits, because the value of what is produced depends on the number of man-hours involved" \
    "in producing it. This fall in profits before long leads to a crisis."
#print(text)
#counter is a library that has a built-in function that counts words in a string
words=text.split()#converts the string to a list
print(words)
counter=Counter(words)
print(counter)
#most_common function is a function that calculates most common word
top_three=counter.most_common(4)
print(top_three)
