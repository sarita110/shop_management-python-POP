# readData function reads laptop details from text file and adds them into 2D array
def readData():
    # file is opened in read mode
    file=open("laptop_details.txt","r")
    raw_data=file.readlines()
    file.close()
    dataList=[]
    
    for i in range(len(raw_data)):
        # strip("\n") is used to remove the newline character (\n) at the end of the line.
        # split(",") is used to split the line into a list of fields, using a comma (,) as the separator.
        dataList.append(raw_data[i].strip("\n").split(","))

    # converting string into int and float   
    for m in range(len(dataList)):
        dataList[m][3] = int(dataList[m][3])
        dataList[m][2] = dataList[m][2].replace("$","")
        dataList[m][2] = float(dataList[m][2])

    return dataList

