#This file is just to try and get somethings working
import pandas as pd

def main():
    file = pd.ExcelFile("SMTH.xlsx") #opens excell file. TODO: add real path and file name
    df1 = file.parse(0) #reads in sheet 1 into z dataframe (df1)

    df.loc[:, 'A'] #selects column A

main()
