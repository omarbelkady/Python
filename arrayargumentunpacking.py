def health_calculator(age, apples_ate, cigs_smoked):
    answer=(100-age)+(apples_ate*3.5)-(cigs_smoked*2)
    print(answer)
bucks_data=[27,20,0]
health_calculator(bucks_data[0],bucks_data[1],bucks_data[2])
#more efficient way to do this or unpacking an argument list
health_calculator(*bucks_data)
