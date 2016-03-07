
import pickle

def leader(Cat):
    try:
        name = Cat.name
        score = value(Cat)
        file = open("leader.txt","rb")
        points= pickle.load(file)
        name = pickle.load(file)
        
        
        if score > points :
            print(score)
            print ("You beat the highscore!")
            file = open("leader.txt","wb")
            pickle.dump(score,file)
            pickle.dump(name)
            addleader()
            file.close()
        
        else:
            print(score)
    except:
        file = open("leader.txt","wb")
        pickle.dump(score,file)
        pickle.dump(name,file)
        file.close()
        
        



def value(Cat):
    score = 0
    for i in Cat.inventory:
        score += i.quality
    return score
