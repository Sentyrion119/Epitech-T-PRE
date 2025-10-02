import random
liste_mot=["apple", "banana", "orange", "grape", "pear", "peach", "cherry", "melon", "strawberry", "lemon","dog", "cat", "mouse", "horse", "cow", "sheep", "goat", "duck", "lion", "tiger","red", "blue", "green", "yellow", "black", "white", "purple", "brown", "pink", "gray","car", "bus", "train", "bicycle", "plane", "boat", "truck", "motorcycle", "ship", "submarine","table", "chair", "bed", "sofa", "door", "window", "floor", "roof", "wall", "lamp","water", "fire", "earth", "air", "wind", "rain", "snow", "ice", "storm", "cloud","happy", "sad", "angry", "tired", "excited", "scared", "calm", "proud", "bored", "nervous","computer", "keyboard", "mouse", "screen", "phone", "internet", "cloud", "server", "cable", "battery","house", "school", "city", "village", "country", "street", "park", "garden", "shop", "market","morning", "afternoon", "evening", "night", "day", "week", "month", "year", "hour", "minute","bread", "rice", "pasta", "meat", "fish", "egg", "milk", "cheese", "butter", "sugar","football", "basketball", "tennis", "golf", "boxing", "swimming", "running", "cycling", "skiing", "hiking","king", "queen", "prince", "princess", "man", "woman", "child", "boy", "girl", "baby","sun", "moon", "star", "planet", "universe", "galaxy", "space", "rocket", "satellite", "astronaut","book", "pen", "pencil", "paper", "notebook", "bag", "box", "letter", "envelope", "stamp","music", "song", "guitar", "piano", "drum", "violin", "dance", "movie", "theater", "painting","food", "drink", "coffee", "tea", "juice", "watermelon", "grapefruit", "plum", "apricot", "mango","money", "coin", "bank", "credit", "debit", "salary", "price", "cost", "market", "trade","doctor", "nurse", "teacher", "student", "engineer", "driver", "farmer", "worker", "police", "firefighter","strong", "weak", "fast", "slow", "big", "small", "hot", "cold", "light", "dark"]

def randome(liste_mot):
    return liste_mot[random.randint(0, len(liste_mot) -1)]

def motAnd_(liste_mot):
    mot = randome(liste_mot)
    lenMot= len(mot)
    lenMotAnd_ = lenMot * ("_ ")
    return lenMotAnd_, mot

def hangman(lenMotAnd_, mot):
    lives = input("Combien de vie souhaitez vous ? ")
    if lives.isdigit() :
        lives = int(lives)
        while lives > 0 :
            print(lenMotAnd_)
            # print(mot)
            userLetter = input("Trouver une bonne lettre : ")
            if userLetter.isalpha():
                if len(userLetter) <= 1 :
                    if userLetter in mot :
                        indexes = []
                        for index, currLetter in enumerate(mot):
                            if userLetter == currLetter:
                                indexes.append(index * 2)
                            
                        for index in indexes:
                            lenMotAnd_ = lenMotAnd_[:index] + userLetter + lenMotAnd_[index+1:]    
                        splitMot_ = lenMotAnd_.split()
                        splitMot_ = "".join(splitMot_)
                        if splitMot_ == mot:
                            print ("you win")
                            break
                    else:
                        lives -= 1
                        print("Il vous reste", lives, "vie")
                        
                elif len(userLetter) > 1 :
                    if userLetter == mot:
                        print ("you win")
                        break
                elif lives == 0:
                    print("Vous avez perdu le mot était :", mot)        
            else :
                print("les caractères autre que les alphas sont refusé.")    
    else :
        print("Merci de mettre un chiffre.")
            
            
            
    
    
bresom=motAnd_(liste_mot)
hangman(bresom[0], bresom[1])
    
