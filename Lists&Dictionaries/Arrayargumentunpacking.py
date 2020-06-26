def health_calculator(age, carrots_ate, cigs_smoked):
    answer=(100-age)+(carrots_ate*3.5)-(cigs_smoked*2)
    print(answer)
ramo_data=[27,20,0]
health_calculator(ramo_data[0],ramo_data[1],ramo_data[2])
#more efficient way to do this or unpacking an argument list
health_calculator(*ramo_data)
