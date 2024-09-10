'''
        # 2. Secound Pattern
                *****
                *   *
                *   *
                *   *
                *****
'''
rows = int(input("Enter how many rows do you want: "))
col = int(input("Enter how many colums do you want: "))
print("Second Pattern\n")
for i in range(rows):
    for j in range(col):
        if i == 0 or i == rows-1 or j == 0 or j ==col-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()