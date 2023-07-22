import random as r

matrix = list()
rows = list()
columns = list()
total_columns = list()
total_rows = list()

# Assigning random values of rows and columns 
def generate_nos():
    global rows,columns
    while True:
        if len(rows)==10 and len(columns)==10:
            break 
        no1 = r.randint(10,99)
        no2 = r.randint(10,99)
        if(no1  in rows) or (no1 in columns) or (no2  in rows) or (no2 in columns) :
            no1 = r.randint(10,99)
            no2 = r.randint(10,99)
        else:
            rows.append(no1)
            columns.append(no2)

# Addition of matrix values
def generate_matrix():
    global matrix
    for i in rows :
        a = []
        for j in columns :
            temp = i+j
            a.append(temp)
        matrix.append(a)    

# # Printing the values
def print_matrix():
    generate_matrix()
    print('\t',end=" ")
    for i in columns:
        print(i,end="  ")
        
    print('\n')

    for j in range(len(rows)) :
        print(rows[j],end="\t")
        for k in matrix[j] :
            print(k,end="  ")
        print()

    total_addition()
    print(f'\nTotal row values are : {str(total_rows)}')
    print(f'Total column values are : {str(total_columns)}')

# Whole matrix traversal
def matrix_travesal():
    generate_matrix()
    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            print(f'Matrix [{i}][{j}] : {matrix[i][j]}')

# Sum of rows and columns 
def total_addition():
    global total_columns,total_rows
    for i in range(len(matrix)):
        row = matrix[i]
        total_rows.append(sum(row))

    for j in range(10):
        temp=[]
        for i in range(10):
            value =matrix[i][j]
            temp.append(value)
        total_columns.append(sum(temp))


generate_nos()
# matrix_travesal()
print(f'Random row values are : {str(rows)}')
print(f'Random column values are : {str(columns)}\n')
print_matrix()
