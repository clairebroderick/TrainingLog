#Attempt at finished product

from StoringMembersDetails import StoreMembersDetails

from EnteringResults import EnterResults

from ComparingPerformance import CompareTimes

from SelectTeam import SelectTeam


print ("Welcome to the Training Log")
cont = "y"

while cont == "y":
    print ()
    print ("What would you like to access?")
    print ("1) Member Information")
    print ("2) Training Results")
    print ("3) Compare Training Results")
    print ("4) Select Team")
    print ("5) Exit Program")
    choice = input("Please enter 1, 2, 3 4 or 5\n")

    try:
        int(choice)


    except:
        print("Please make a valid selection!")
    
    else:
        choice = int(choice)
                
        if choice == 1:
            StoreMembersDetails()


        elif choice == 2:
            EnterResults()

        elif choice == 3:
            CompareTimes()

        elif choice == 4:
            SelectTeam()

        elif choice == 5:
            cont = "n"
            print ("Press any key to exit")
        
