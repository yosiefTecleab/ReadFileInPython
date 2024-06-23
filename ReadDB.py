import pyodbc
from datetime import datetime

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = " "
database = "Test1"

# query = "INSERT INTO pivot_tb VALUES(sales_date,customer_id,amount);"


# query='SELECT * FROM [dbo].[Countries]'

cnxn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";Trusted_Connection=yes"
)
cursor = cnxn.cursor()

with open("Input_original_data.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        sales_date_2 = line.split(",")[0]
        #sales_date=datetime.strptime(sales_date_2, "%d %b %y").strftime("%d-%b-%y")
        # sales_date=Convert(DATETIME, line.split(",")[0], 101)
        customer_id = line.split(",")[1]
        amount = line.split(",")[2]
        cursor.execute(
            "INSERT INTO pivot_tb (sales_date,customer_id,amount) VALUES (?,?,?)",
            # "Convert(DATETIME, " + sales_date + ", 101)",
            # (sales_date[:2] + "-" + sales_date[3:6] + "-" + sales_date[7:9]),
            # "2017-08-25",
            # "01-Jan-2021",
            "05-Jun-19",
            #sales_date,
            # str(sales_date),
            # "CAST(" + sales_date + " as date)",
            # "TRY_CONVERT(DATETIME, " + sales_date + ",105)",
            # "TRY_PARSE(" + sales_date + ")",
            # sales_date='01-Jan-2021'
            # "CONVERT(datetime2(0)," + '01-Jan-2021' + ",23)",
            # "TRY_convert(datetime2(0),'01-Jan-2021',23)",
            customer_id,
            amount,
        )
        cnxn.commit()
        #print(sales_date[:2] + "-" + sales_date[3:6] + "-" + sales_date[7:9])

f.close()

""" from datetime import datetime

date_2 = datetime.strptime("25 Jan 2021", "%d %b %Y").strftime("%d-%b-%y")
# date = datetime.strptime("2020-07-26", "%Y-%m-%d")

print(date_2) """
