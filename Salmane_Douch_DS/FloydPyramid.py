def floyd_pyramid(rows):
    num=1
    for i in range(num, rows+1):
        for j in range(i):
            print(num, end=" ")
            num+=1
        print()
rows=int(input("Enter the number of rows"))
floyd_pyramid(rows)