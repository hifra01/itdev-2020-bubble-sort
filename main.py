import csv

def read_file(fpath):
    arr = []
    with open(fpath) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        if header != None:
            for row in reader:
                if len(row) > 0:
                    arr.append(row)
    return arr

def sort_data(arr):
    max = len(arr) - 1
    for x in range(max,0,-1):
        for y in range(x):
            cmp1 = str(arr[y][0]) + " " + str(arr[y][1])
            cmp2 = cmp1 = str(arr[y+1][0]) + " " + str(arr[y+1][1])
            if arr[y] > arr[y+1]:
                temp=arr[y+1]
                arr[y+1]=arr[y]
                arr[y]=temp
    return arr

def show_data(arr):
    for row in arr:
        full_name = str(row[0]) + " " + str(row[1])
        email = row[2]
        gender = row[3]
        print("{}\t\t{}\t\t{}".format(full_name, email, gender))

show_data(sort_data(read_file('IT-Dev.csv')))