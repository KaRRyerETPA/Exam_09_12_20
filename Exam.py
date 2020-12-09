mon_mot = ["C","I","T","R","O","N"]
correction = ["A","A","A","A","A","A"]
position_correct = [0,0,0,0,0,0]
position_incorrect = [0,0,0,0,0,0]

def choix (correction):
    for i in range (0,6):
        print("Insérez les lettres dans l'ordre jusqu'a 6 max")
        correction[i] = input()
    return correction

def match (correction,mon_mot,position_correct):
    for i in range (0,6):
        if (correction[i]==mon_mot[i]):
           position_correct[i]=+1
    return position_correct