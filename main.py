from shop_management.options import display_options

def display_homepage():
    print("\n")                                                                                                                                        
    print("\t\t    ▒█░░░ ░█▀▀█ ▒█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█   ▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀█ ▒█▀▀█") 
    print("\t\t    ▒█░░░ ▒█▄▄█ ▒█▄▄█ ░▒█░░ ▒█░░▒█ ▒█▄▄█   ░▀▀▀▄▄ ▒█▀▀█ ▒█░░▒█ ▒█▄▄█") 
    print("\t\t    ▒█▄▄█ ▒█░▒█ ▒█░░░ ░▒█░░ ▒█▄▄▄█ ▒█░░░   ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█░░░") 
    print("\n")
    print("▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀   ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▄▀█") 
    print("▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░▄▄ ▒█▀▀▀ ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░   ░▀▀▀▄▄ ▒█▄▄▄█ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▒█▒█") 
    print("▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▒█░░   ▒█▄▄▄█ ░░▒█░░ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░░▒█")
    print("\n")

# Entry point of the system
def main():
    display_homepage()
    display_options()

# The main function is executed when the script is run directly
if __name__=="__main__":
    main()