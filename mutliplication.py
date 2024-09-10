# write a program using for 
# 1*1=1
# 1*2=2
# 1*3=3
# '
# '
# 1*10=10
number = int(input("Enter which Table you want: "))
table_range = int(input("Enter for range you want: "))
for i in range(table_range+1):
    print(number, "*", i, "=" , number*i)

# OUTPUT:
'''
Enter which Table you want: 7
Enter for range you want: 10
7 * 0 = 0
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
'''