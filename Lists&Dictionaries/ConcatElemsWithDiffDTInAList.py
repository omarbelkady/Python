some_text = "this is some random text"
deleting_spaces = " "

#Placing the elements within a list 
print(some_text.split(deleting_spaces))

#Join Method to output the array items out as a full string of text
some_text_p2 = ['this', 'is', 'dummy', 'text']
print(deleting_spaces.join(some_text_p2))
print("\n USING JOIN METHOD: \n")
print("/".join(some_text_p2))

#mixed data
my_data = ['6342', 56837, '2-56837', 746867]
#use a list comprehension to output the list as a string converting each list element to a string
print(" ".join(str(elem) for elem in my_data))

#the expression above is called a generator expression
