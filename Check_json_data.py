#!/usr/bin/env python
# coding: utf-8

# In[26]:


'''to check json data is correct or not in postgress table and give
wrong json all column details as output with jupyter code 
Here's an example of how you can check if JSON data in a PostgreSQL table is valid,
and return all columns of rows with invalid JSON data,
using Python with psycopg2 library in a Jupyter Notebook:'''


import psycopg2
import json

conn = psycopg2.connect(
    host="corover-postgres-test.chohyljzbmzb.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="corover_test",
    password="CoroverAWS"
)

cursor = conn.cursor()

cursor.execute("SELECT * from  npci_test.bot")

rows = cursor.fetchall()

invalid_json_rows = []
for row in rows:
    try:
        json.loads(row[9])
    except ValueError:
        invalid_json_rows.append(row)

if invalid_json_rows:
    print("Rows with invalid JSON data:")
    for row in invalid_json_rows:
        print(row)
else:
    print("All JSON data is valid")

cursor.close()
conn.close()


# In[ ]:


'''
In this example, the psycopg2 and json libraries are used to connect to the PostgreSQL database and parse JSON data.
The conn object is used to connect to the database and the cursor object is used to execute the SQL commands.

The SELECT statement is used to retrieve all the rows in the table. 
The fetchall method of the cursor object is then used to retrieve all the rows returned by the query.

For each row, the json.loads function from the json library is used to parse the value in the column
specified by column_index_with_json_data as JSON. If the JSON data is not valid, the ValueError exception is
raised and the row is added to the list invalid_json_rows.

If the list invalid_json_rows is not empty, it means that there are rows with invalid JSON data,
and these rows are printed. If the list is empty, it means that all the JSON data is valid and the message
"All JSON data is valid" is printed.

Note that the specifics may vary depending on the specific PostgreSQL version you are using and the psycopg2
version you are using.



'''


# In[34]:


import psycopg2
import json
import csv

conn = psycopg2.connect(
    host="corover-postgres-test.chohyljzbmzb.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="corover_test",
    password="CoroverAWS"
)

cursor = conn.cursor()

cursor.execute("SELECT * from  npci_test.bot")

rows = cursor.fetchall()

invalid_json_rows = []
for row in rows:
    try:
        json.loads(row[9])
    except ValueError:
        invalid_json_rows.append(row)

if invalid_json_rows:
    rows = invalid_json_rows
    filename = "invalid_json_data.csv"
else:
    filename = "valid_json_data.csv"

'''with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)'''
    
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow([row[0],row[8]]) 

cursor.close()
conn.close()


# In[ ]:


'''In this updated code, we loop through each column of each row,
instead of just checking the ninth column, and use json.loads to parse the JSON data.
If the JSON data is invalid, we add the entire row to a list of invalid_json_rows and break out of the inner loop.
At the end, if there are any invalid JSON data, we print the entire rows with invalid data, otherwise 
we print a message indicating that all JSON data is valid.
'''


# In[33]:


import psycopg2
import json

conn = psycopg2.connect(
    host="corover-postgres-test.chohyljzbmzb.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="corover_test",
    password="CoroverAWS"
)

cursor = conn.cursor()

cursor.execute("SELECT * from  npci_test.bot")

rows = cursor.fetchall()

invalid_json_rows = []
for row in rows:
    for i in range(len(row)):
        try:
            json.loads(row[i])
        except ValueError:
            invalid_json_rows.append(row)
            break

if invalid_json_rows:
    print("Rows with invalid JSON data:")
    for row in invalid_json_rows:
        print(row)
else:
    print("All JSON data is valid")

cursor.close()
conn.close()


# In[ ]:




