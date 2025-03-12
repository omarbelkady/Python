# append, remove, sort, len

mymatrix=[
    [1,2,3,3,4,4,5],
    [48,42,13,4],
    [-7,9,81,21,22]
]
print(mymatrix)
mymatrix.append(33)
mymatrix.remove(42)
mymatrix[0][2]=4
print(mymatrix[1])
print(len(mymatrix))



def find_best_seat(seating):
    rows=len(seating)
    columns=len(seating[0])
    best_seat=None
    min_distance=float('inf')
    for i in range(rows):
        for j in range(columns):
            if(seating[i][j]==0):
                center_row = rows// 2
                center_col = columns // 2
                distance=abs(i-center_row)+abs(j-center_col)
                if(distance<min_distance):
                    min_distance=distance
                    best_seat=(i+1,j+1)
    return best_seat

def can_sit_group(seating, number_of_people):
    rows=len(seating)
    columns=len(seating[0])
    #iterate over the rows then columns
    for i in range(rows):
        consecutive=0
        for j in range(columns):
            if(seating[i][j]==0):
                consecutive+=1
                if(consecutive==number_of_people):
                    return[(i+1, j-number_of_people+2+k) for k in range(number_of_people)]
            else:
                consecutive = 0
    return "Full"


seating_configuration = (
    (1, 1, 0, 1, 1),
    (0, 0, 0, 1, 0),
    (1, 1, 1, 1, 1)
)

best_seat = find_best_seat(seating_configuration)
print("The best available seat in: row "+str(best_seat[0])+ "seat: "+str(best_seat[1]))
number_of_people=3
seating_result = can_sit_group(seating_configuration, number_of_people)
if(seating_result=="Full"):
    print("The theater is full")
else:
    print("The seats available for the group: "+str(seating_result))
