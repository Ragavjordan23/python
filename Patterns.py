for count2 in range(0,8):
    for space in range(7,count2,-1):  
        print(" ", end = ' ')
    for num in range(count2,-1,-1):
        print(num, end = " ")
    for num in range(1,count2+1):
        print(num, end = ' ')
    print()
    
            # output:

#                 0
#               1 0 1
#             2 1 0 1 2
#           3 2 1 0 1 2 3
#         4 3 2 1 0 1 2 3 4 
#       5 4 3 2 1 0 1 2 3 4 5 
#     6 5 4 3 2 1 0 1 2 3 4 5 6 
#   7 6 5 4 3 2 1 0 1 2 3 4 5 6 7

no = int(input(" Enter count: "))
for row in range(1, no+1):
    print(" " *(row-1), str(row) *(no+1-row), end = ' ')
    print()  
    
    # output:
    
   # 1 1 1 1 1
   #   2 2 2 2
   #     3 3 3
   #       4 4
   #         5
