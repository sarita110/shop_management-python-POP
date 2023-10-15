import datetime
from shop_management.read_data import readData


# sellLaptop function allows user to manage operations of selling laptops
# displays purchasing details and prints bill after writing it in a file
# also alerts user when trying to sell more than available
def sellLaptop():
    sold_Laptops=[]
    sellCount = 0  
    while True:
        laptopsData = readData()
        # running the loop till user wants to sell laptops to customer
        for m in range(len(laptopsData)):
            laptopsData[m][3] = str(laptopsData[m][3])
            laptopsData[m][2] = str(laptopsData[m][2])
        print("\n")
        print("\t\t\t{:^37}".format("Pixel Technologies"))
        print("\t\t\t{:^37}".format("Laptops available at the moment"))
        print("\t\t\t"+"-"*37)
        print("\t\t\t|S.N  | Name \t        | Quantity  |")
        print("\t\t\t"+"-"*37)
        for i in range(len(laptopsData)):
            each_laptop = laptopsData[i]
            print("\t\t\t|", end="")
            print(str(i+1).ljust(5), each_laptop[0].ljust(16),
                each_laptop[3].ljust(10), sep="| ", end="")
            print("|")
        print("\t\t\t"+"-"*37)

        for m in range(len(laptopsData)):
            laptopsData[m][3] = int(laptopsData[m][3])
            laptopsData[m][2] = laptopsData[m][2].replace("$","")
            laptopsData[m][2] = float(laptopsData[m][2])

        # asking S.N and running loop until S.N is a valid'
        while True:
            laptops_Number = int(input("\nEnter S.N. of the laptop you want to Sell:---> "))-1
            if laptops_Number < 0 or laptops_Number > (len(laptopsData)-1):
                print("\n<-----------Please enter valid S.N number  for the laptop----------->\n")
            elif (laptopsData[laptops_Number][3] == 0):
                print("\n<-----------No stock available for this laptop----------->")
                print("<-----------Please choose another laptop----------->")
            else: 
                break
                         

        # storing laptops information to their respective variable
        laptops_name = laptopsData[laptops_Number][0]
        laptops_Brand = laptopsData[laptops_Number][1]
        laptops_Price = laptopsData[laptops_Number][2]
        available_laptops = laptopsData[laptops_Number][3]
        laptops_Processor = laptopsData[laptops_Number][4]
        laptops_Graphics = laptopsData[laptops_Number][5]
        print("\n\t\t\t|"+"-"*50+"|")
        print("\t\t\t|  "+"Laptop you choosed is : ".ljust(30), "|", str(laptops_name).ljust(15),"|")
        print("\t\t\t|  "+"Stock available :".ljust(30), "|", str(available_laptops).ljust(15),"|")
        print("\t\t\t|  "+"Laptop Brand :".ljust(30), "|", str(laptops_Brand).ljust(15),"|")
        print("\t\t\t|  "+"Laptop Processor :".ljust(30), "|", str(laptops_Processor).ljust(15),"|")
        print("\t\t\t|  "+"Laptop Graphics :".ljust(30), "|", str(laptops_Graphics).ljust(15),"|")
        print("\t\t\t|"+"-"*50+"|")
        print("\n\t\tCost price for 1 ", laptops_name," with discount of the day is: $", laptops_Price)
        

        while True:
            try:
                # asking user the number of laptops to buy
                no_Of_Laptops = int(input("\nHow many of laptop"+laptops_name+" you want to sell?:---> "))
                # selling number cannnot be 0 or less than 0
                if no_Of_Laptops <= 0:
                    print("\n<-----------Please enter valid value, quantity should be more than 0.----------->")
                # cannot sell laptops more than the available laptops
                elif no_Of_Laptops > available_laptops:
                    print("\n<-----------It exceeds the available stock number for ", laptops_name,"that is availabe stock with us : ", available_laptops, "----------->")
                else:
                    sold_Laptops.append(laptopsData[laptops_Number])
                    sold_Laptops[sellCount].append(no_Of_Laptops)
                        # calculating the cost of the customer
                    amount= int(laptops_Price) * int(no_Of_Laptops)
                    print("\n..................Sell Successful : Your cost of buying",no_Of_Laptops, laptops_name, "is: $", amount,"..................\n")
        
                    available_laptops = int(laptopsData[laptops_Number][3])-int(no_Of_Laptops)
                    file=open("laptop_details.txt","r")
                    quantity = file.read()
                    file.close()
                    quantity = quantity.replace(str(laptopsData[laptops_Number][3]), str(available_laptops))
                    file=open("laptop_details.txt","w")
                    file.write(quantity)    
                    file.close()
                    break

            except:
                print("<-----------Error occured, try again with correct input!!----------->")

        # Exiting from loop of selling laptop only when user wants 
        while True:
            print("\n\nDo you want to look for Another Laptops as???")
            confirm = input("Enter (Y/y) for yes or (N/n) for no:---> ")
            
            if confirm in ["y", "Y", "n", "N"]:
                break

            else:
                print("<-----------Please enter input as Invalid----------->")

        if confirm == "y" or confirm == "Y":
            sellCount += 1

        elif confirm == "n" or confirm == "N":
            break
    

    from shop_management.selling_bill import selling_bill
    invoice_name=selling_bill(sold_Laptops)
    # showing invoice in the shell
    file=open(invoice_name, "r")
    print(file.read())
    file.close()
    print("<---------------------You have successfully sold laptops to the customer---------------------->\n\n")
    
