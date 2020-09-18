import pytest
import pandas as pd
from fuzzywuzzy import fuzz

def detect_duplicates(df):
  """Return the cleaned dataframe from duplicates and the percentage of duplicates
  found
  :param1 : the dataframe
  """
  #The three criteria we choose to detect a duplicate
  df1=df["given_name"]
  df2=df["surname"]
  df3=df["phone_number"]
  #A list containing the row index of the duplicates
  dup_idx = []
  #Copy of the dataframe so we can compare it to the original
  df_clear=df.copy()




  for i in range(len(df1.values)-1):

      for j in range(i+1,len(df1.values)):

          if fuzz.token_sort_ratio(df1.values[i], df1.values[j]) >= 75 and fuzz.token_sort_ratio(df2.values[i], df2.values[j]) >= 75 and  df3.values[i]==df3.values[j]:

              dup_idx.append(df1.index[j])

  df_clear = df.drop(df.index[dup_idx])
  percentage = round((len(dup_idx)/len(df))*100,2)


  return  percentage,df_clear





df=pd.read_csv("df_patient_dup.csv",index_col=0)
df = df.reset_index()


def test_detect_duplicates():

    assert detect_duplicates(df)!=(0,df)
