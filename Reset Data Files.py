#Reset Data Files (This will bring the system back to having just 2 users 



import pickle

Members = [["Claire", "08/01/1981", "123"], ["Mark", "05/05/1982", "456"]]

file = open("members.txt", "wb")
pickle.dump(Members, file)
file.close()

CycleResults = {"Claire": [], "Mark": []}
file = open("CycleResults.txt", "wb")
pickle.dump(CycleResults, file)
file.close()

SwimResults = {"Claire": [], "Mark": []}
file = open("SwimResults.txt", "wb")
pickle.dump(SwimResults, file)
file.close()

RunResults = {"Claire": [], "Mark": []}
file = open("RunResults.txt", "wb")
pickle.dump(RunResults, file)
file.close()



