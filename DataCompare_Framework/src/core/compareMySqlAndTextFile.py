import datacompy
import pandas as pd
import mysql.connector
from pandas import DataFrame

from src.connections import mysql,Text


class CompareData:
        SQL_Query: DataFrame = pd.read_sql_query(
            '''SELECT diseaseId,diseaseName
           FROM ngo.disease''', mysql.mySqlConnector.conn)

        df = pd.DataFrame(SQL_Query, columns=['diseaseId', 'diseaseName'])

        df1 = pd.read_csv(Text.TextFileConnector.textfile)

        compare = datacompy.Compare(
            df, df1,
            join_columns='diseaseID',  # You can also specify a list of columns eg ['policyID','statecode']
            abs_tol=0,  # Optional, defaults to 0
            rel_tol=0,  # Optional, defaults to 0
            df1_name='Original',  # Optional, defaults to 'df1'
            df2_name='New'  # Optional, defaults to 'df2'
        )
        print(compare.report())
