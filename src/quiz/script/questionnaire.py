from random import randint, randrange

def questionnaire():
    f = open("quiz/data/q1.json", "a")
    f.write("[")
    for i in range(1,4):
        d={}
        d["question"] =  "q"+str(i)
        d["reponse"] = {}
        random = randint(3,4)
        for j in range(1,random):
            d["reponse"]["r"+str(j)] = "rep" + str(j)
        f.write(str(d)+ str(",\n"))
    f.write("]")
    
questionnaire()

