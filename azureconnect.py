# =============================================================================
# Import Resources
# =============================================================================
import mysql.connector
from mysql.connector import errorcode
import os 
import pandas as pd
import textwrap
import pyodbc
# =============================================================================
# Update Directory
# =============================================================================
current_directory = os.chdir(r"C:\Users\dozs1\Desktop\ESD Term 7\Capstone\Capstone data")
current_directory

# =============================================================================
# Connection to azure db
# =============================================================================
#specifying driver
driver = '{ODBC Driver 18 for SQL Server}'
#specify server name and database name

server_name = "steeg-capstone"
database_name = "STEEG-Capstone"

#Create Server URL
server = '{server_name}.database.windows.net,1433'.format(server_name = server_name)

#Define username and password
username = 'steeg-capstone'
password = 'Opshub2022'


#Create full connection string
connection_string = textwrap.dedent("""
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
""".format(
    driver = driver,
    server = server,
    database = database_name,
    username = username,
    password = password
    ))
                        
# =============================================================================
# Create PYODBC connection object
# =============================================================================

cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

#Create a new cursor object from connection

crsr: pyodbc.Cursor = cnxn.cursor()

#Test query
select_sql = "SHOW TABLES"

#Execute the query
crsr.execute(select_sql)
#Grab data
print( crsr.fetchall())

#Close connection
#cnxn.close()
# =============================================================================
# Test Queries
# =============================================================================


# =============================================================================
# sql = "SHOW TABLES"
# all_tables = pd.read_sql_query(sql,connection_string)
# =============================================================================

