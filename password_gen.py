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

def save(txt):
    with open('passwords.txt', 'a') as f:
        f.write(txt)
    print("This password/pin is stored in your computer for future use!")

#main
print ("This is the password/pin generator!")
print ("Note: Minimum password length is 6 whereas maximum of that is 10.")

pin_word = int(input("\n1.Password\n2.Pin\n(1/2) "))

purpose = input("For which account is this password? ")

try:
    if pin_word==1:
        digits = int(input("How many digit password do you want? "))
        if digits == 6:
            print ("A strong password for", purpose, "could be", pass6)
            save(f"Your {purpose} password is {pass6}\n")

        elif digits == 7:
            print ("A strong password for", purpose, "could be", pass7)
            save(f"Your {purpose} password is {pass7}\n")

        elif digits == 8:
            print ("A strong password for", purpose, "could be", pass8)
            save(f"Your {purpose} password is {pass8}\n")

        elif digits == 9:
            print ("A strong password for", purpose, "could be", pass9)
            save(f"Your {purpose} password is {pass9}\n")

        elif digits == 10:
            print ("A strong password for", purpose, "could be", pass10)
            save(f"Your {purpose} password is {pass10}\n")

        else:
            print ("Password length limit too low or too higher!\nTry again!")
        

    elif pin_word==2:
        def pin():
            n = random.choice(numbers)
            pin = random.choice(numbers)
            d = int(input("Digits: "))
            for i in range(1, d):
                pin = pin + n
                n = random.choice(numbers)
            return pin

        print("A strong PIN for", purpose, "could be", pin())
        save(f"Your {purpose} pin is {(pin)}\n")
            
except Exception as e:
    print (e)
    quit()
