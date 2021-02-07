import string, random, pyperclip

capitals = string.ascii_uppercase
smalls = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
print(symbols)

def save(account, password, mode):
    with open(r"passwords.txt", 'a') as f:
        if mode == "password":
            f.write(f"Your {account} password is {password}\n")

        elif mode == "pin":
            f.write(f"Your {account} pin is {password}\n")

        else:
            print("Invalid mode!")

    pyperclip.copy(password)
    print("This password/pin is stored in your computer for future use!")

def retrieve(account):
    with open(r"passwords.txt") as f:
        fc = f.read().split("\n")

    for lines in fc:
        acc = lines.replace("Your", "").replace("password", "").replace("pin", "").replace("is", "").lstrip().rstrip().split(" ")[0]
        if account.lower() == acc.lower():
            pw = lines.split(" ")[-1]
            pyperclip.copy(pw)
            return f"Password for {account} is `{pw}`."

    return "Found no password corresponding with {}".format(account)

def pin(length):
    n = random.choice(numbers)
    pin = random.choice(numbers)
    for _ in range(length-1):
        pin = pin + n
        n = random.choice(numbers)
    return pin

def password(length):
    if length <= 4:
        print("Password length less than the minimum length 4.")
        quit()
    passw = random.choice(capitals) + random.choice(smalls) + random.choice(numbers) + random.choice(symbols)

    while len(passw) < length:
        next_chars = [random.choice(capitals), random.choice(smalls), random.choice(numbers), random.choice(symbols)]
        passw += random.choice(next_chars)

    return passw

if __name__ == "__main__":
    print("\nThis is the password/pin generator!\n\n")
    task = int(input("What do you want to do? \n 1. Generate password/pin \n 2. Retrieve password/pin \n"))

    if task == 1:
        print("Note: Minimum password length is 4.")

        pin_word = int(input("\nWhat to generate? \n 1.Password \n 2.Pin \n (1/2) "))


        if pin_word==1:
            purpose = input("For which account is this password? ")

            while True:
                length = int(input("How long password do you want? "))
                pw = password(length)
                print(f"A strong password for {purpose} could be {pw}.")
                satisfied = input("Are you satisfied with the password? If no then new password would be generated.(y/n) ")
                if satisfied.lower() != "n":
                    save(purpose, pw, "password")
                    break

        elif pin_word==2:
            purpose = input("For which account is this password? ")

            while True:
                length = int(input("How long password do you want? "))
                p = pin(length)
                print("A strong PIN for", purpose, "could be", p)
                satisfied = input("Are you satisfied with the password? If no then new pin would be generated.(y/n) ")
                if satisfied.lower() != "n":
                    save(purpose, p, "pin")
                    break

    elif task == 2:
        acc = input("Which account's password to retrieve? ")
        print(retrieve(acc))

    else:
        print("Invalid input!")
