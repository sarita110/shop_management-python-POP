# importing in-built module datatime to generate unique bill each time
import datetime
# importing readData function of read_data file from shop_management package
from shop_management.read_data import readData

# purchaseLaptop function allows user to manage operaions of purchasing laptop
# displays purchasing details and prints bill after writing it in a file
# also allows to add new laptop details to the text file after purchasing
def purchaseLaptop():
    purchased_Laptops=[]
    purchaseCount = 0   
    # running the loop till user wants to sell laptops to customer
    while True:
        laptopsData = readData()
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

        isnewLaptop = False
        try:
            invoice = True
            ask= int(input("Enter 1 if you want to purchase laptop available with you or 2 if you want add a new one: "))
            
            # purchasing and adding laptop already available in the system
            if ask==1:
                try:
                    while True:
                        laptops_Number = int(input("\nEnter S.N. of the laptop you purchased from manufacturer: "))-1
                        if laptops_Number < 0 or laptops_Number > (len(laptopsData)-1):
                            print("\nYou are entering invalid S.N number.\n")
                            print("\nEnter valid S.N.  for the Laptop\n")
                        else: 
                            laptops_name = laptopsData[laptops_Number][0]
                            laptops_Brand = laptopsData[laptops_Number][1]
                            laptops_Price = laptopsData[laptops_Number][2]
                            available_laptops = laptopsData[laptops_Number][3]
                            laptops_Processor = laptopsData[laptops_Number][4]
                            laptops_Graphics = laptopsData[laptops_Number][5]
                            print("\nLaptop you choosed is : ", laptops_name)
                            print("Quantity of this laptop available with us : ", available_laptops)
                            print("Laptop Brand : ", laptops_Brand)
                            print("Laptop Processor : ", laptops_Processor)
                            print("Laptop Graphics : ", laptops_Graphics)
                            print("Cost price for 1 ", laptops_name," with discount of the day is: $", laptops_Price)
                            no_Of_Laptops = int(input("\nHow many of laptop "+laptops_name+" did you purchase?:-->"))
                            # selling number cannnot be 0 or less than 0
                            if no_Of_Laptops <= 0:
                                print("Please enter valid value, quantity should be more than 0.")
                            # cannot sell laptops more than the available laptops
                            else:
                                purchased_Laptops.append(laptopsData[laptops_Number])
                                purchased_Laptops[purchaseCount].append(no_Of_Laptops)
                                    # calculating the cost of the customer
                                amount= int(laptops_Price) * int(no_Of_Laptops)
                                print("\nPurchase Successful : Your cost of purchasing",no_Of_Laptops, laptops_name, "is: $", amount,"\n")
                                available_laptops = int(laptopsData[laptops_Number][3])+int(no_Of_Laptops)

                                file=open("laptop_details.txt","r")
                                quantity = file.read()
                                file.close()

                                file=open("laptop_details.txt","w")
                                quantity = quantity.replace(str(laptopsData[laptops_Number][3]), str(available_laptops))
                                file.write(quantity)   
                                file.close()
                                break
                except:
                    print("Error occured please try again")
            
            #This part is responsible for adding new laptop details while purchasing 
            elif ask==2:
                try:
                    isnewLaptop=True
                    while True:
                        print("Enter the details of new laptop that is not available with you that you want to purchase")
                        newLaptopName=input("Enter the name of the laptop you purchased: ")

                        laptopAlreadyExists=False

                        for m in range(len(laptopsData)):
                            newLaptopNameLowerCase=newLaptopName.lower()
                            if newLaptopNameLowerCase == laptopsData[m][0].lower():
                                print("\nThe new laptop you want to add already exists with you.")
                                laptopAlreadyExists=True
                            
                        if laptopAlreadyExists==False:
                            isnewLaptop=True    
                            lastIndexOfLaptop=len(laptopsData)-1
                            laptops_Number=lastIndexOfLaptop+1
                            new_laptop_data = []
                            new_laptop_data.append(newLaptopName)
                            new_laptop_data.append(input("Enter the brand of the laptop you purchased: "))
                            laptops_Price=float(input("Enter the price of the laptop you purchased: "))
                            new_laptop_data.append(laptops_Price)
                            no_Of_Laptops=int(input("How many laptops did you purchase: "))
                            new_laptop_data.append(no_Of_Laptops)
                            new_laptop_data.append(input("Enter the processor of the laptop you purchased: "))
                            new_laptop_data.append(input("Enter the graphics of the laptop you purchased: "))
                            laptopsData.append(new_laptop_data)

                            purchased_Laptops.append(laptopsData[laptops_Number])
                            purchased_Laptops[purchaseCount].append(no_Of_Laptops)
                            # calculating the cost of the customer
                            amount= int(laptops_Price) * int(no_Of_Laptops)
                            print("\nPurchase Successful : Your cost of purchasing",no_Of_Laptops, newLaptopName, "is: $", amount,"\n")

                            file=open("laptop_details.txt","w")
                            for laptopData in laptopsData: 
                                line = ','.join([str(elem) for elem in laptopData])
                                file.write(line + '\n')
                            file.close()
                            break
                except:
                    print("\nError occured please try again")     

            else:
                print("\nError occured enter option either 1 or 2")
                invoice = False

        except:
            print("\nError occured please try again with valid input")
            invoice = False
        
        # Exiting from loop of purchasing laptop only when user wants 
        if invoice==True:
            print("\n\nDo you want to look for Another Laptops??")
            try:
                confirm = input("Enter (Y/y) for yes or (N/n) for no: ")
                if confirm == "y" or confirm == "Y":
                    purchaseCount += 1
                elif confirm == "n" or confirm == "N":
                    break
                else:
                    print("-----------Please input only from the option provided--------")

            except:
                print("-----------Please input as instructed--------")
               

    from shop_management.purchasing_bill import purchasing_bill
    invoice_name=purchasing_bill(purchased_Laptops)
    # showing invoice in the shell
    file=open(invoice_name, "r")
    print(file.read())
    file.close()
    print("<---------------------You have successfully purchased laptops from the manufacturer---------------------->\n\n")
    
