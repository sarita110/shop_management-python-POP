import datetime 
def selling_bill(sold_Laptops):
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

    # Bill is written in a new txt file each time
    invoice_name = name+"_SoldBill_"+Date+"_"+Time+'.txt'
    file = open(invoice_name, "w")

    file.write("\n                                      _________________________________________________________________________________________")
    file.write("\n                                      |                                 Pixel Technologies                                    |")                              
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    file.write("\n                                      |       Selling Bill                                       sold Date : "+"{:<17}".format(Date)+"|")
    file.write("\n                                      |                                                          sold Time : "+"{:<17}".format(Time)+"|")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    file.write("\n                                      |  Customer Name      : "+"{:<15}".format(name)+"                                                 |")
    file.write("\n                                      |  Customer Address   : "+"{:<15}".format(address)+"                                                 |")
    file.write("\n                                      |  Customer Contact   : "+"{:<15}".format(str(contact))+"                                                 |")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    for items in range(len(sold_Laptops)):
        file.write("\n                                      |"+" "*14+"Laptop name     :    "+"{:<39}".format(str(sold_Laptops[items][0]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Brand           :    "+"{:<39}".format(str(sold_Laptops[items][1]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Price           :    "+"{:<39}".format("$"+str(sold_Laptops[items][2]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Processor       :    "+"{:<39}".format(str(sold_Laptops[items][4]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Sold Quantity   :    "+"{:<39}".format(str(sold_Laptops[items][6]))+" "*13+"|")
        file.write("\n                                      |"+" "*14+"Graphics        :    "+"{:<39}".format(str(sold_Laptops[items][5]))+" "*13+"|")
        Cost = ((sold_Laptops[items][2]) *int(sold_Laptops[items][6]))
        file.write("\n                                      |"+"{:^87}".format("Total Cost Till Now: $"+(str(Cost)))+"|")
        file.write("\n                                      |---------------------------------------------------------------------------------------|")
        A_Total += Cost
    shipping_charge = 20
    file.write("\n                                      |  Net amount ie, total amount without shipping charge: $"+"{:<10}".format(str(A_Total))+"                     |")
    file.write("\n                                      |  Fixed Shipping Charge: $"+"{:<15}".format(str(shipping_charge))+"                                              |")
    file.write("\n                                      |---------------------------------------------------------------------------------------|")
    Grand_Total = int(A_Total)+int(shipping_charge)
    file.write("\n                                      |  Grand Total(including shipping): $"+"{:<15}".format(str(Grand_Total))+"                                    |")
    file.write("\n                                      |_______________________________________________________________________________________|\n")
    file.close()
    return invoice_name