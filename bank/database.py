import mysql.connector as sql 

# #--dada base connection--
mydb = sql.connect(
    host = "localhost",
    user="root",
    password = "9090",
    database = "bank"
)
cursor = mydb.cursor()

# #-----for table creating----

def createCustomerTable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20),
                password VARCHAR(20),
                name VARCHAR (20),
                age INTEGER,
                city VARCHAR(20),
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN)
    ''')
mydb.commit()

if __name__ == "__main__":
    createCustomerTable()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result