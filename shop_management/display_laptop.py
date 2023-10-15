# importing readData function from read_data file of shop_management package
from shop_management.read_data import readData

# display function displays available laptop detail in a tabular format 
def displayLaptop():
    dataList=readData()

    # converting the values with different datatypes into string 
    for m in range(len(dataList)):
        dataList[m][3] = str(dataList[m][3])
        dataList[m][2] = str(dataList[m][2])

    print("\n")
    print("{:^91}".format("\t\tPixel Technologies: Available Laptops"))
    print("\t\t"+"-"*91)
    print("\t\t| S.N | Name \t\t|  Brand \t  |  Price \t    |  Quantity |  GPU\t          |")
    print("\t\t"+"-"*91)
    for i in range(len(dataList)):
        each_laptop= dataList[i]
        print("\t\t|",end="")
        print(str(i+1).ljust(5), each_laptop[0].ljust(16), each_laptop[1].ljust(16), each_laptop[2].ljust(16), each_laptop[3].ljust(10), each_laptop[4].ljust(16), sep="| ",end="")
        print("|")
    print("\t\t"+"-"*91) 
    print("\n")
    print("Enter any key to return to option section:--> ")
    input()

