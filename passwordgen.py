#lists
alphabets_C = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alphabets_S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "@", "#", "$", "%", "&"]

#variable random
import random
ALPHABET = random.choice(alphabets_C)
alphabet1 = random.choice(alphabets_S)
Number1 = random.choice(numbers)
Symbol1 = random.choice(symbols)
alphabet2 = random.choice(alphabets_S)
Number2 = random.choice(numbers)
alphabet3 = random.choice(alphabets_S)
Number3 = random.choice(numbers)
Symbol2 = random.choice(symbols)
ALPHABET2 = random.choice(alphabets_C)

#password lengths
pass6 = ALPHABET+alphabet1+Number1+Number2+Symbol1+alphabet2
pass7 = ALPHABET+alphabet1+Number1+Number2+Symbol1+alphabet2+Number3
pass8 = ALPHABET+alphabet1+Number1+Number2+Symbol1+alphabet2+Symbol2+Number3
pass9 = ALPHABET+alphabet1+Number1+Number2+Symbol1+alphabet2+Number3+Symbol2+alphabet3
pass10 = ALPHABET+alphabet1+Number1+Number2+Symbol1+ALPHABET2+alphabet2+Symbol2+alphabet3+Number3


#main
print ("This is the password generator!")
print ("Note: Minimum password length is 6 whereas maximum of that is 10.")

try:
    purpose = input("For which account is this password? ")
    digits = int(input("How many digit password do you want? "))
    if digits == 6:
        print ("A strong password for", purpose, "could be", pass6)
      
    elif digits == 7:
        print ("A strong password for", purpose, "could be", pass7)
       
    elif digits == 8:
        print ("A strong password for", purpose, "could be", pass8)
     
    elif digits == 9:
        print ("A strong password for", purpose, "could be", pass9)
      
    elif digits == 10:
        print ("A strong password for", purpose, "could be", pass10)

    else:
        print ("Invalid input!")
        print ("Try again!")
    
        
except Exception as e:
    print (e)
    quit()
