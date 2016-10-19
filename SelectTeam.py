#Import Swim, Cycle and Run Lists

def SelectTeam():
    import pickle

    #Import run results list
   

    file = open("SwimResults.txt", "rb")
    RunResults = pickle.load(file)
    file.close()
    

    #Calculate the averages and append to a list

    names = []
    averages = []

    for i in RunResults:
        #append names to list
        names.append(i)
        #append average to list in same order as names list
        averages.append(sum(RunResults[i])/len(RunResults[i]))

    print (names)
    print (averages)



    #Calculate 3 Lowest Scores

    count = 1

    #Repeat the steps 3 times
    for i in range (3): 

        LowestTime = 5000 #No runners should have a time as large as 5000
        

        for i in averages:
               
            #Compare each time against Lowest Time
            
            if i < LowestTime:
                LowestTime = i

            #MemberName

            index = averages.index(LowestTime)

        
        print ("Team Member", count, " is:", names[index], "with a time of: ", LowestTime)
        count += 1
        
        #Remove member with lowest Score
        names.pop(index)
        averages.pop(index)



  








     


