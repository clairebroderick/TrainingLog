#Import Swim, Cycle and Run Lists

def CompareTimes():
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



        



    #Average Cycle Times
    print("+++++++++++++++++++++++++++++++++++++")
    print ("Comparison of CYCLE TIMES in mph:")
    print ()
    print("Average cycle times")
    for i in CycleResults:
        print (i, ":", (sum(CycleResults[i])/len(CycleResults[i])))
        
    #Slowest Time
    print()
    print("__________")
    print ("Slowest times in mph:")
    for i in CycleResults:
        print (i, ":", (min(CycleResults[i])))
        
    #Fastest Cycle Time

    print()
    print("__________")
    print ("Fastest times in mph:")
    for i in CycleResults:
        print (i, ":", (max(CycleResults[i])))

    #___________________________
    #Run Times
    print()
    print("+++++++++++++++++++++++++++++++++++++")
    print ("Comparison of Run times in mph:")
    for i in RunResults:
        print (i, ":", (sum(RunResults[i])/len(RunResults[i])))
        
    #Slowest Time
    print()
    print("__________")
    print ("Slowest times in mph:")
    for i in RunResults:
        print (i, ":", (min(RunResults[i])))
        
    #Fastest Cycle Time

    print()
    print("__________")
    print ("Fastest times in mph:")
    for i in RunResults:
        print (i, ":", (max(RunResults[i])))

    #___________________________
    #Swim Times
    print()
    print("+++++++++++++++++++++++++++++++++++++")
    print ("Comparison of Swim times in mph:")
    for i in SwimResults:
        print (i, ":", (sum(SwimResults[i])/len(SwimResults[i])))
        
    #Slowest Time
    print()
    print("__________")
    print ("Slowest times in mph:")
    for i in SwimResults:
        print (i, ":", (min(SwimResults[i])))
        
    #Fastest Cycle Time

    print()
    print("__________")
    print ("Fastest times in mph:")
    for i in SwimResults:
        print (i, ":", (max(SwimResults[i])))




