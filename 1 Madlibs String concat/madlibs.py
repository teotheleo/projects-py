# Madlibs using string concatenation

# A paragraph with blank spaces which are going to be filled by the player 

# string concatenation
#name = "First"
#print("subscribe to " + name)
#print("subscribe to {}".format(name))
#print(f"subscribe to {name}")

def madlibs():
    
    adj = input("Adjective: ")
    adj2 = input("Second adjective")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")

    madlibs = f"Computer programming is so {adj}! IT makes me so {adj2} all the time because \
    I love to {verb1}. Stay focused and {verb2} like you are {famous_person}"

    print(madlibs)

madlibs()

