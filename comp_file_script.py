
import pandas as pd



# Read input file

df_prev =pd.read_excel('D:\Harish kemkar\SRE\Python  files\File_Project\Previous_date.xlsx')
df_cur =pd.read_excel('D:\Harish kemkar\SRE\Python  files\File_Project\Current_date.xlsx')

print(df_cur.shape[0])

print(df_prev.shape[0])
column_name_prev = list(df_prev.columns)
column_name_cur = list(df_cur.columns)

# Log details in file

Details = "Analysis of file comparison \n"
with open("details.txt",'w') as file:
    file.write(Details)

# To check columns in current and previous files

if (sorted(column_name_prev) == sorted(column_name_prev)):
    print("Same column in current and previous file")
    Details = "Same column in current and previous file"
    print(Details)
else:
    print("Columns are not equal ")
    Details = "Column Name Mismatch found"

# Log output in Details file
with open("details.txt",'a') as file:
    file.write(Details)

# Record count
Record_count = ""
Record_count_prev = len(df_prev)
Record_count_cur = len(df_cur)


# Log output in Details file
with open("details.txt",'a') as file:
    file.write("\n Record count of  previous file ")
    file.write(str(Record_count_prev))

    file.write("\n Record count of  current file ")
    file.write(str(Record_count_cur))

# %Change in record count

diff = Record_count_prev - Record_count_cur
diff = abs(diff)
greater = max(Record_count_prev,Record_count_cur)
percentage_change = (diff/greater) * 100

print(percentage_change)

# Log % Change in Details
with open("details.txt",'a') as file:
    file.write("\n Difference in record count ")
    file.write(str(diff))
    file.write("\nPercentage change  is ")
    file.write(str(percentage_change))

# Column specific details in current file


print(df_cur['Age'].max())
max_age = df_cur['Age'].max()

print(df_cur['Age'].min())
min_age = df_cur['Age'].min()

print(df_cur['Age'].mean())
avg_age = df_cur['Age'].mean()

print(df_cur['Gender'].value_counts())
print(df_cur['Country'].value_counts())

with open("details.txt",'a') as file:
    file.write("\n Column specific details in current file")
    file.write("\n Max Age is ")
    file.write(str(max_age))

    file.write("\n Min Age is ")
    file.write(str(min_age))

    file.write("\n Average Age is ")
    file.write(str(avg_age))
