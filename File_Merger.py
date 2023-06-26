#All code written by Edward A, eia1@st-andrews.ac.uk
# This program will merge flat files (e.g. csv, txt, ascii) that are of the same format
# e.g. same number of rows, columns, header, and same delimiter
# an example format is:

# x   y   y2
# 1   1   2
# 2   2   4
# 3   3   6
# 4   4   8
 

print("ImportingPackages")
import os
from os.path import isfile, join
import numpy as np
import pandas as pd

def MergeFile():
    print("\nPlese enter the full path to a folder containing all the files you would like to merge")
    print("An exmaple of a format is C:\\Users\\Documents\\FolderToBeMerged")
    folderPathway = input("Enter here: ")

    print("\nPlease enter the file type you are trying to merge including the period, e.g. '.csv', '.asc', '.txt', etc")
    fileType = input("Enter file type: ")

    print("\nPlease enter the separator between the data values, e.g. ',' for a csv") 
    delimeter = input("Enter delimeter: ")

    print("\nPlease enter the number of dependent variables in each file, e.g. for just a single y value enter 1")
    numY = int(input("Enter the number of dependent variables: "))

    print("\nIf there is extra data at the start of each file please enter the number of rows of this data, if nothing enter '0'")
    numRowsHeader = int(input("Enter number of rows: "))

    print("\nIf there is extra data at the end of each file please enter the number of rows of this data, if nothing enter '0'")
    numRowsFooter = int(input("Enter number of rows: "))

    transpose = False
    while True:
        print("\nWould you like to transpose the merged data?")
        transposeTxt = input("Please enter 'Y' or 'N': ")

        if(transposeTxt.upper() == "N"):
            transpose = False
            break;
        elif (transposeTxt.upper() == "Y"):
            transpose = True
            break;
        else:
            print("Please only enter \"Y\" or \"N\"")



    print("\nPlease enter the name you would like for the merged file")
    fileName = input("Enter the file name: ")


    try:
        paths = os.listdir(folderPathway)
    except:
        print("\nError with FilePathway, ensure that you entered it properly")
        return()

    #get list of the file pathways
    files = []
    for x in paths:
        if(isfile(join(folderPathway,x))):
            if(x.endswith(fileType)):
                files.append(x)

    if(len(files)==0):
        print("\nCouldn't find any files, please ensure that you entered the pathway and file type properly")
        return()


    print("\nReading in Files")


    data = []

    #gets the data from the files
    for x in files:
        if numRowsHeader == 0:
            rawdata = pd.read_csv((folderPathway+"/"+x), sep=delimeter, header=None, engine='python', skipfooter=numRowsFooter)
        else:
            rawdata = pd.read_csv((folderPathway+"/"+x), sep=delimeter, header=None, engine = 'python', skiprows=numRowsHeader, skipfooter=numRowsFooter, on_bad_lines='skip')
        data.append(rawdata.to_numpy())

    print("Read in Files")

    dataConcate = data[0][:,1:numY+1]

    #checks that the number of dependent variables is acceptable
    if( numY+1 >len(data[0][:,0])):
        print("\nThe value entered for number of dependent variables is too large")
        return()
    elif (numY<1):
        print("\nThe value entered for number of dependent variables is too small")
        return()

    print("Begining to Merge")

    #merges all of the data in the files
    for i in range(1,len(data)):
        dataTemp = data[i][:,1:numY+1]
        if(len(dataConcate) == len(dataTemp)):
            dataConcate = np.column_stack((dataConcate,dataTemp))
        else:
            print("\nEnsure that all sets of data are the same length")
            return


    #creates a header from the file names    
    header = []
    if numY > 1:
        for x in files:
            header.append(x)
            for i in range(1,numY):
                header += [""]
    else:
        header += files
    
    #creates a new data frame with all of the merged data
    df = pd.DataFrame(dataConcate, columns = header, index = data[0][:,0])

    #creates the file path for the csv with the merged data
    fileName +=".csv"
    filePath = os.path.join(folderPathway,fileName)

    #transposes the data
    if transpose:
        df = df.transpose()
    
    #writes the merged data to a csv
    df.to_csv(filePath)

    print("Files successfully Merged")
    return()
#end def MergeFile

#Main, calling will run merge file
def Main():
    print("\n This program will merge flat files (e.g. csv, txt, ascii) that are of the same format"
            + "\n e.g. same number of rows, columns, header, and same delimiter"
            + "\n An example format is:"
            + "\n x   y   y2"
            + "\n 1   1   2"
            + "\n 2   2   4"
            + "\n 3   3   6"
            + "\n 4   4   8")
    MergeFile()

    while(True):
        print("\nAre you finished merging files?")
        stop = input("Please enter 'Y' or 'N': ")

        if(stop.upper() == "Y"):
            return
        #end if

        MergeFile()
    #end while
#end Main

Main()