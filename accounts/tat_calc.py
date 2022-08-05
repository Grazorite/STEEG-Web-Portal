import mysql.connector
from mysql.connector import errorcode
import os 
import pandas as pd
import textwrap
import pyodbc
import datetime as dt
import numpy as np
import time



def call_function():
    print("TAT Calculation Done")
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
# =============================================================================
# Retrieve tables into df
# =============================================================================
#Test query
select_sql = "SELECT * FROM [dbo].[MainTable]"
main = pd.read_sql_query(select_sql,cnxn)
select_sql = "SELECT * FROM [dbo].[jobUpdateStart]"
jobUpdateStart = pd.read_sql_query(select_sql,cnxn)
select_sql = "SELECT * FROM [dbo].[jobUpdateEnd]"
jobUpdateEnd = pd.read_sql_query(select_sql,cnxn)
select_sql = "SELECT * FROM [dbo].[jobUpdateComplete]"
jobComplete = pd.read_sql_query(select_sql,cnxn)
select_sql = "SELECT * FROM [dbo].[ReportGeneration]"
ReportDF = pd.read_sql_query(select_sql,cnxn)


#Execute the query
crsr.execute(select_sql)

#Grab data
#print(crsr.fetchall())


# =============================================================================
# TAT Calc Function Part 1
# =============================================================================
def generateDateList(jobId):
    dates = [] # list of dates from starting date
    jobDone = [] # 1 if job was done on that day, 0 if nothing done
    endDate = dt.datetime.now().date() 
    startDatedf = main[main['SERVICE_ORDER'] == jobId]
    startDatedf.reset_index(inplace=True, drop=True)
    startDate = startDatedf['MAL_START'][0]
    datePointer = startDate
    jobUpdateStartdf = jobUpdateStart[jobUpdateStart['SERVICE_ORDER'] == jobId]
    jobUpdateStartdf.reset_index(inplace=True, drop=True)
    jobUpdateEnddf = jobUpdateEnd[jobUpdateEnd['SERVICE_ORDER'] == jobId]
    jobUpdateEnddf.reset_index(inplace=True, drop=True)
    JobCompletedf = jobComplete[jobComplete['SERVICE_ORDER'] == jobId]
    JobCompletedf.reset_index(inplace=True, drop=True)
    eachJob = [] # list of tuples (list) of each job start and end
    COD = []

    if len(jobUpdateStartdf) == len(jobUpdateEnddf): ## there may be a complete
        if len(jobUpdateStartdf) == 0:
            if len(JobCompletedf) != 0:
                eachJob.append([startDate, JobCompletedf['mal_end_date'][0]])
            else:
                eachJob.append([startDate, endDate])
        elif len(jobUpdateStartdf) != 0:
            if len(JobCompletedf) != 0:
                eachJob.append([jobUpdateEnddf['end_date_actual'].iloc[-1],JobCompletedf['mal_end_date'][0]])
                
            else:
                eachJob.append([startDate,endDate])
                                
        for i in range(len(jobUpdateStartdf)):
            eachJob.append([jobUpdateStartdf['start_date_actual'][i], jobUpdateEnddf['end_date_actual'][i]]) 
            COD.append(jobUpdateEnddf['Cause_of_Delay'][i])
    
    else: # wont have a complete
        for j in range(len(jobUpdateStartdf)-1):
            eachJob.append([jobUpdateStartdf['start_date_actual'][j], jobUpdateEnddf['end_date_actual'][j]])  
            COD.append(jobUpdateEnddf['Cause_of_Delay'][j])
        #eachJob.append([jobUpdateStartdf['startdate_actual'][len(jobUpdateStartdf)-1].date(), endDate])
    
    if len(JobCompletedf) != 0:
        endDate = JobCompletedf['mal_end_date'][0]
    else:
        endDate = endDate
  
    while datePointer <= endDate : #This maybe wrong wtf
        doJob = 1
        for i in range(len(eachJob)):
            if datePointer >= eachJob[i][0] and datePointer <= eachJob[i][1]:
                if eachJob[i][1] == endDate:
                    doJob = 1
                #elif eachJob[i][1] == doneDate: #This logic is what i need but idk how to imput
                #    break
                else:
                    doJob = 0
            else:
                doJob = 1
        dates.append(datePointer)
        jobDone.append(doJob)
        datePointer += dt.timedelta(days=1)
        
    #print(eachJob)
    
    outputdict = {'dates':dates, 'jobDone': jobDone, 'updatedates': eachJob,'causeofdelay':COD}
    # outputdf = pd.DataFrame(outputdict)
    # print(outputdf)
    # print(sum(outputdf['jobDone']))
    return outputdict
    
    #print(outputdict)

fulloutput = {} # key is service ord, value is output dict   
for k in range(len(main)):
    
    
    fulloutput[str(main.loc[k, 'SERVICE_ORDER'])] = generateDateList(main.loc[k, 'SERVICE_ORDER'])
    #print(fulloutput)
    
    
#INSERT BREAK ON UPDATECOMPLETE?
# =============================================================================
# TAT CALC FUNCTION PART 2: Changing to DF, extract ATAT values 
# =============================================================================
svc_ord = [] 
sum_working_days = [] 
date_pairs = [] 
date_diffs = [] 
cod = []
for x in list(fulloutput.keys()): 
#     svc_ord = x 
#     sum_working_days = sum(fulloutput[x]['jobDone']) 
#     date_pairs = fulloutput[x]['updatedates'] 
#     #print(date_pairs) 
#     date_diffs = [(i[1]-i[0]).days for i in date_pairs] 
    #print(x) 
    #print(len([fulloutput[x]['updatedates']])) 
    #print(len([[(i[1]-i[0]).days for i in fulloutput[x]['updatedates']]])) 
    svc_ord.append(x) 
    cod.append(fulloutput[x]['causeofdelay'])
    sum_working_days.append(sum(fulloutput[x]['jobDone'])) 
    date_pairs.append(fulloutput[x]['updatedates']) 
    date_diffs.append([(i[1]-i[0]).days for i in fulloutput[x]['updatedates']]) 
 
     
    #entry = {"Service_ORD": svc_ord, "Sum-working-days": sum_working_days, "Date-Pairs": [date_pairs], "Date-Diffs": [date_diffs]} 
    #pd.DataFrame(entry) 
tatoutput_df = pd.DataFrame({"SERVICE_ORD": svc_ord, "Actual TAT": sum_working_days, "Cause of Delay periods": date_pairs, "Length of Delay": date_diffs, "Cause of Delay": cod})
tatoutput_df['SERVICE_ORDER'] = tatoutput_df['SERVICE_ORD'].astype(float)
# =============================================================================
# Function to create report section, ATTRIBUTE COD VALUES Forming combined tables
# =============================================================================

def countCOD(x):
    COD = ['A/W SPARE', 'A/W FACILITY', 'A/W OTHER JOB', 'INST', 'OTH',
       'AWAIT UNIT ACCEPT', 'MULTIPLE FAULTS']
    #testdf2 = pd.DataFrame(columns = COD)
    col1 = x['Length of Delay']
    col2 = x['Cause of Delay']
    total = []
    for i in range(len(x.index)):
        temp=[0,0,0,0,0,0,0]
        for j in range(len(col2[i])):
            temp[COD.index(col2[i][j])] += col1[i][j+1]
        total.append(temp)
        
        #print(temp)
    #testdf2.append(temp)
    #print(total)
    return pd.DataFrame(data =np.array(total),columns = COD, index = x['SERVICE_ORD'])
    #return (np.array(total))
cod_matrix = countCOD(tatoutput_df)  
cod_matrix['SERVICE_ORDER'] = cod_matrix.index.astype(float)
#testdf4 = pd.concat([main,cod_matrix],axis = 1)
combined_df = pd.merge(pd.merge(main,cod_matrix,on='SERVICE_ORDER'),tatoutput_df,on='SERVICE_ORDER')
#testdf3 = pd.DataFrame(data = cod_matrix,columns = COD, dtype = int , index = x['Service ORDER'])
