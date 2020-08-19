#Selection Sort: check 2 adjacent elements
my_numbers=[2,5,2,6,5,6,8,3,7,2]
for i in range(len(my_numbers)):
    min_index=i
    #start from the subsequent index
    for j in range(i+1,len(my_numbers)):
        if(my_numbers[j]<my_numbers[min_index]):
                min_index = j
    #swap the numbers
    my_numbers[i],my_numbers[min_index]=my_numbers[min_index],my_numbers[i]

print(my_numbers)
