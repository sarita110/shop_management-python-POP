# This function shows the options to perform different operations through the system
def display_options():
    run=True
    while run:
        print("\t\t       ","-"*51)
        print("\t\t\t| Select one of the options below to proceed      |")
        print("\t\t       ","-"*51)
        print("\t\t\t| Enter 1:  To display available laptops          |")
        print("\t\t\t| Enter 2:  To sell laptops to customers          |")
        print("\t\t\t| Enter 3:  To purchase laptops from manufacturer |")
        print("\t\t\t| Enter 99: To exit from the system               |")
        print("\t\t       ","-"*51)

        # try-except to handle any exception that might crash the program
        try:
            option=int(input("\nEnter your option:--->"))
            if option==1:
                #importing show_stock function from read.py
                from shop_management.display_laptop import displayLaptop
                displayLaptop()

            elif option==2:
                #importing sold_laptops function from sold_laptops.py
                from shop_management.sell_laptop import sellLaptop
                sellLaptop()

            elif option==3:
                #importing Buying_Laptops function from buying_laptops.py
                from shop_management.purchase_laptop import purchaseLaptop
                purchaseLaptop()
        
            elif option==99:
                #Thanks message
                print("\n")
                print("\t\t ▀▀█▀▀ ▒█░▒█ ░█▀▀█ ▒█▄░▒█ ▒█░▄▀   ▒█░░▒█ ▒█▀▀▀█ ▒█░▒█   █ █") 
                print("\t\t ░▒█░░ ▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ ▒█▀▄░   ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█   ▀ ▀")
                print("\t\t ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█   ░░▒█░░ ▒█▄▄▄█ ░▀▄▄▀   ▄ ▄")

                #breaking the loop to exit or stop the program 
                run=False

            else:
                print("\n","!"*23,"Please enter the options from 1 to 3 or press 99 to exit.","!"*23,"\n")
                display_options()
                
        except:
            print("\n","!"*30,"Error occured please try again","!"*30,"\n")
            display_options()