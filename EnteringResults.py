    #Practice for entering Results

def EnterResults():
    import pickle

    #Import results lists

    file = open("CycleResults.txt", "rb")
    CycleResults = pickle.load(file)
    file.close()

    file = open("SwimResults.txt", "rb")
    RunResults = pickle.load(file)
    file.close()

    file = open("RunResults.txt", "rb")
    SwimResults = pickle.load(file)
    file.close()



    cont = "y"

    while cont == "y":
        print()
        print("What would you like to do?")
        print("1) Add new results")
        print("2) Recall Results")
        choice = input("Ener 1 or 2\n")

        try:
            int(choice)
        except:
            print("Error. Please make a valid selection.")

        else:
            choice = int(choice)
            
            

            if choice == 1: 

                #Find location of name in lists

                name = input ("Please enter your name: \n")

                if name in CycleResults:
                    
                    CycleTimesList = CycleResults[name]
                    RunTimesList = RunResults[name]
                    SwimTimesList = SwimResults[name]

                
                    

                    print ("Please enter your training results below")
                    print()
                    CycleTime = int(input("Please enter you cycle time in minutes: "))
                    RunTime = int(input("Please enter you run time in minutes: \t"))
                    SwimTime = int(input("Please enter you swim time in minutes: \t"))

                    save = input("Would you like to save these results? y/n \n ")

                    if save == "y":
                        CycleTimesList.append(CycleTime)
                        RunTimesList.append(RunTime)
                        SwimTimesList.append(SwimTime)

                        print()
                        print(CycleTimesList)
                        print(RunTimesList)
                        print(SwimTimesList)
                        
                        CycleResults[name] = CycleTimesList
                        RunResults[name] = RunTimesList
                        SwimResults[name] = SwimTimesList

                           
                        print ("Results Saved")

                else:
                    print("Name not in list")

                    
                    #Pickle the New Lists
                    
                    
                    file = open("CycleResults.txt", "wb")
                    pickle.dump(CycleResults, file)
                    file.close()

                    
                    file = open("SwimResults.txt", "wb")
                    pickle.dump(SwimResults, file)
                    file.close()

                    
                    file = open("RunResults.txt", "wb")
                    pickle.dump(RunResults, file)
                    file.close()

                cont = input("Would you like to continue? y/n")


            elif choice == 2:
                name = input ("Please enter your name: \n")

                if name in CycleResults:
                    print ("Your Cycle times are: ", CycleResults[name])
                    print ("Your Run times are: ", RunResults[name])
                    print ("Your Swim times are: ", SwimResults[name])

                cont = input("Would you like to continue? (n to retuen to main menu) y/n")
                        
                    
                



