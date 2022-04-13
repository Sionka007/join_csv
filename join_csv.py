import pandas as pd

# load path
file_path1=input('file_path: ')
file_path2=input('file_path: ')


# reading two csv files
data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)

join_type=input("enter join_type: left, right or inner ")

column_name=input('type column_name: ')

# using merge function
def join(data1, data2, join_type, column_name):
    output1 = pd.merge(data1, data2, how=join_type, on=column_name)
    print(output1)

join(data1, data2, join_type, column_name)

input('Press Enter to close program')

