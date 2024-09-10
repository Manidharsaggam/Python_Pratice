# practice patterns
'''     1. Square pattern
            * * * * *
            * * * * *
            * * * * *
            * * * * *
            * * * * *
'''
rows = int(input("Enter how many rows do you want: "))
col = int(input("Enter how many colums do you want: "))
print("Square Pattern\n")
for i in range(rows):
    for j in range(col):
        print("*",end='')
        if j != col-1:
            print(' ',end='')
    print()


