#Compring all results

def DisplayAllTimes():
    
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

    print ("Cycle Times")
    for i in CycleResults:
        print (i, ":", CycleResults[i])

    print ()


    print ("Swim Times")
    for i in SwimResults:
        print (i, ":", SwimResults[i])

    print ()


    print ("Run Times")
    for i in RunResults:
        print (i, ":", RunResults[i])

    



    


    
