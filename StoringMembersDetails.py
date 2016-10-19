
#Storing Members Details

def StoreMembersDetails():
        import pickle

        def PickleNewList():
            #Pickle the new list
                file = open("members.txt", "wb")
                pickle.dump(Members, file)
                file.close()

        cont = "y"

        while cont == "y":

            #Menu
            print ("What would you like to do?")
            print ("1) Add a new member")
            print ("2) Retrieve member details")
            print ("3) Edit a members details")
            choice = input("Please enter 1,2 or 3 to enter your selection\n")

            try:
                int(choice)

            except:
                print ("Error! Please make make a valid selection")

            else:
                choice = int(choice)
                if choice == 1:
                        #Add new member-------------------------------------
                        print ()
                        Name = input ("Please enter your name\n")
                        DOB = input ("Please enter your date of birth\n")
                        Phone = input ("Please enter your phone number\n")

                        print("Name: ", Name)
                        print("Date of Birth:", DOB)
                        print("Phone Number: ", Phone)

                        DetailsCorrect = input ("Do you want to save this user? Yes(y) No(n)\n")

                        if DetailsCorrect == "n":
                            print("________________________")
                            Name = input ("Please enter your name\n")
                            DOB = input ("Please enter your date of birth. dd/mm/yyy\n")
                            Phone = input ("Please enter your phone number\n")
                            

                        elif DetailsCorrect == "y":
                            print ("Details Saved")
                            #Add new data to the New User List
                            NewUser = []
                            NewUser.append(Name)
                            NewUser.append(DOB)
                            NewUser.append(Phone)
                            

                        #Import data and append new member
                            file = open ("members.txt", "rb")
                            Members = pickle.load(file)
                            file.close()
                            Members.append(NewUser)
                            

                        #Pickle the new list
                            file = open("members.txt", "wb")
                            pickle.dump(Members, file)
                            file.close()

                        #Add new file to Swim,Cycle, and Run Results lists

                            file = open("CycleResults.txt", "rb")
                            CycleResults = pickle.load(file)
                            file.close()

                            file = open("SwimResults.txt", "rb")
                            RunResults = pickle.load(file)
                            file.close()

                            file = open("RunResults.txt", "rb")
                            SwimResults = pickle.load(file)
                            file.close()

                            CycleResults[Name] = []
                            SwimResults[Name] = []
                            RunResults[Name] = []

                            #Pickle the new lists
                            file = open("CycleResults.txt", "wb")
                            pickle.dump(CycleResults, file)
                            file.close()

                            file = open("SwimResults.txt", "wb")
                            pickle.dump(SwimResults, file)
                            file.close()

                            file = open("RunResults.txt", "wb")
                            pickle.dump(RunResults, file)
                            file.close()



                        else:
                            DetailsCorrect = input ("Do you want to save this user? Yes(y) No(n)\n")

                        cont == input ("Do you want to continue? y/n \n")
                    

                        
                        
                      
                elif choice ==2:
                    # Recall member details-------------------------------
                    

                    #Import data 
                    file = open ("members.txt", "rb")
                    Members = pickle.load(file)
                    file.close()

                    
                #Print List of names on database
                    count = 0
                    for i in range(0,(len(Members))):
                        print ("Record", count, ":", Members[i][0])
                        count +=1

                #Recall Details
                    MemberSelection = int(input ("Whoes details would you like to recall? Please enter number:\n"))
                    
                    print()
                    print ("Member Details")
                    print ("Name:", Members[MemberSelection][0])
                    print ("Date of Birth:", Members[MemberSelection][1])
                    print ("Phone Number:", Members[MemberSelection][2])
                    
                           
                    #cont == input ("Do you want to continue? y/n \n")
                        
                elif choice == 3:
                    
                    #Edit members details---------------------------------
                    #Import data 
                    file = open ("members.txt", "rb")
                    Members = pickle.load(file)
                    file.close()

                    
                #Print List of names on database
                    count = 0
                    for i in range(0,(len(Members))):
                        print ("Record", count, ":", Members[i][0])
                        count +=1

                    MemberSelection = int(input ("Whoes details would you like to change? Please enter record number:\n"))


                    #Improvement --> Ensure that the selection is in range
                    if MemberSelection < len(Members): #Checks selection in in the range of available accounts

                
                            print()
                            print ("Member Details")
                            print ("1) Name:", Members[MemberSelection][0])
                            print ("2) Date of Birth:", Members[MemberSelection][1])
                            print ("3) Phone Number:", Members[MemberSelection][2])

                            ChangeSelection = int(input("What details would you like to change? 1/2/3 \n"))

                            if ChangeSelection in range(1,3): #checks that the user selects a valid option



                                    if ChangeSelection == 1:
                                        NewName = input ("Please enter new name: \n")
                                        Members[MemberSelection][0] = NewName
                                        print (Members[MemberSelection])
                                        PickleNewList()

                                    elif ChangeSelection == 2:
                                        NewDOB = input ("Please enter new Date of Birth: \n")
                                        Members[MemberSelection][1] = NewDOB
                                        print (Members[MemberSelection])
                                        PickleNewList()

                                    elif ChangeSelection == 3:
                                        NewPhone = input ("Please enter new Phone Number: \n")
                                        Members[MemberSelection][2] = NewPhone
                                        print (Members[MemberSelection])
                                        PickleNewList()

                            else:
                                    print("Invalid Option")

                    else:
                            print("Invalid Option")

                                



                cont = input ("Do you want to continue? n - will return to main menu) y/n \n")


              














