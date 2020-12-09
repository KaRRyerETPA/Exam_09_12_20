mon_mot = ["C","I","T","R","O","N"]
correction = ["A","A","A","A","A","A"]
position_correct = [0,0,0,0,0,0]
position_incorrect = [0,0,0,0,0,0]
random = [0,1,2,3,4,5,6,7,8,9]
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
    
ran = random.randint(0,10)

if (ran == 0):
    mon_mot=["C","I","T","R","O","N"]
if (ran == 1):
    mon_mot=["G","I","R","O","U","D"]
if (ran == 2):
    mon_mot=["P","I","S","T","O","N"]
if (ran == 3):
    mon_mot=["V","I","R","A","G","E"]
if (ran == 4):
    mon_mot=["M","I","R","A","G","E"]
if (ran == 5):
    mon_mot=["T","U","N","N","E","L"]
if (ran == 6):
    mon_mot=["C","H","A","N","T","S"]
if (ran == 7):
    mon_mot=["C","L","A","S","S","E"]
if (ran == 8):
    mon_mot=["O","I","S","E","A","U"]
print(mon_mot)



print(correction)
choix(correction)

input()