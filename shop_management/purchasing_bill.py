import datetime 
def purchasing_bill(purchased_Laptops):  
    print("\n..................Generating Bill..................")

    name=str(input("Enter your Name: -->"))
    address= str(input("Enter your Address: -->"))
    
    while True:
     #asking contact and running loop until contact is a valid
        try:
            contact=int(input("Enter your Contact: --->"))
            check=str(contact)
            if (len(check)>10 )or(len(check)<10):
                print("<-----------Contact number should be of 10 numbers----------->")
            else:
                break
        except:
            print("<-----------Error occured try again with correct input----------->")
                     
    Now=datetime.datetime.now()
    Date=str(Now.date())
    Time=str(Now.time()).replace(":", "-")

    A_Total=0

# Bill is created in an unique text file each time
    invoice_name = name+"_PurchasedBill_"+Date+Time+'.txt'
    file = open(invoice_name, "w")

    file.write("\n                                      _________________________________________________________________________________________")
    file.write("\n                                      |                                 Pixel Technologies                                    |")                              
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    file.write("\n                                      |       Purchasing Bill                               purchased Date : "+"{:<17}".format(Date)+"|")
    file.write("\n                                      |                                                     purchased Time : "+"{:<17}".format(Time)+"|")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    file.write("\n                                      |  Distributor Name      : "+"{:<15}".format(name)+"                                              |")
    file.write("\n                                      |  Distributor Address   : "+"{:<15}".format(address)+"                                              |")
    file.write("\n                                      |  Distributor Contact   : "+"{:<15}".format(str(contact))+"                                              |")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    
    for items in range(len(purchased_Laptops)):
        file.write("\n                                      |"+" "*14+"Laptop name     :    "+"{:<39}".format(str(purchased_Laptops[items][0]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Brand           :    "+"{:<39}".format(str(purchased_Laptops[items][1]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Price           :    "+"{:<39}".format("$"+str(purchased_Laptops[items][2]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Processor       :    "+"{:<39}".format(str(purchased_Laptops[items][4]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Sold Quantity   :    "+"{:<39}".format(str(purchased_Laptops[items][6]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Graphics        :    "+"{:<39}".format(str(purchased_Laptops[items][5]))+" "*13+"|")
        Cost = ((purchased_Laptops[items][2]) *int(purchased_Laptops[items][6]))
        file.write("\n                                      |"+"{:^87}".format("Total Cost Till Now: $"+(str(Cost)))+"|")
        file.write("\n                                      |---------------------------------------------------------------------------------------|")
        A_Total += Cost
    vat_charge = 0.13*A_Total
    file.write("\n                                      |  Net amount ie, total amount without VAT charge: $"+"{:<10}".format(str(A_Total))+"                          |")
    file.write("\n                                      |  VAT is 13% of net amount: $"+"{:<20}".format(str(vat_charge))+"                                      |")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    Grand_Total = int(A_Total)+int(vat_charge)
    file.write("\n                                      |  Grand Total(including VAT): $"+"{:<20}".format(str(Grand_Total))+"                                    |")
    file.write("\n                                      |_______________________________________________________________________________________|\n")
    file.close()
    return invoice_name