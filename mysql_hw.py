import pymysql

db_host = "192.168.1.161"
db_port = 3306
db_user = "learn"
db_pass = "3tango11"
db_schema = "learn"

conn = pymysql.connect(host=db_host,
                       port=db_port,
                       user=db_user,
                       password=db_pass,
                       db=db_schema)
conn.autocommit(True)
cur = conn.cursor()

create_table_cmd = f"CREATE TABLE `{db_schema}`.`dogs` (" \
                   "`name` VARCHAR(40) NOT NULL," \
                   "`age` INT NOT NULL," \
                   "`breed` VARCHAR(30) NOT NULL);"

table_check_cmd = "SELECT COUNT(*)" \
                  "FROM information_schema.tables " \
                  f"WHERE table_schema = '{db_schema}' " \
                  "AND table_name = 'dogs';"

dog01 = {"name": "rexi", "age": 5, "breed": "rottweiler"}
dog02 = {"name": "mika", "age": 7, "breed": "golden-retriever"}
dog03 = {"name": "niki", "age": 9, "breed": "german-shepherd"}

dogs = [dog01, dog02, dog03]

cur.execute(table_check_cmd)
for row in cur:
    if row[0] <= 0:
        cur.execute(create_table_cmd)

# Insert new rows to dogs table
for dog in dogs:
    insert_dog = "INSERT INTO `%s`.`dogs` (name, age, breed) VALUES ('%s', '%s', '%s')" % \
                 (db_schema, dog["name"], dog["age"], dog["breed"])
    cur.execute(insert_dog)

# Update the second row
cur.execute(f"update `{db_schema}`.`dogs` set age = 2 where name = 'mika'")

# Delete the third row
cur.execute(f"delete from `{db_schema}`.`dogs` where name = 'niki'")

# Show all current items in database:
cur.execute(f"select * from `{db_schema}`.`dogs`")

for row in cur:
    print(row)

cur.close()
conn.close()



