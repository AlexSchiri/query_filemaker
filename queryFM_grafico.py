import pyodbc
from datetime import date, timedelta
import matplotlib.pyplot as plt

for d in pyodbc.drivers():
    print(d)
    
con_str = 'DSN=**name_dns**;UID=**user**;PWD=**pwd**'
converted_date = str((date.today() - timedelta(days=10)).strftime("%d-%m-%Y"))
print(converted_date)
#la data di oggi non ha l'anno
today_date = str(date.today().strftime("%d-%m"))
connection = pyodbc.connect(con_str)
#your query. If fields have spaces code in this way:
query = "SELECT  \"POS TEMP PER RIEP\", COUNT(\"POS TEMP PER RIEP\") "
print("Query: " + query)
cursor =connection.cursor()
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)


x = [row[1] for row in rows]
labels = [row[0] for row in rows]
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(x, labels=labels, autopct='%.1f%%')
ax.set_title('Title')
plt.tight_layout()
plt.show()

