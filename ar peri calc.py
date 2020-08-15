def heronf(a, b, c):
    import math
    s = (a+b+c)/2
    ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return ar

def pi():
    import math
    return math.pi

if __name__ == "__main__":
    try:
        print ("This is the perimeter/area calculator")
        while True:
            what_to_find = int(input("What do you want to find: \n1. Perimter \n2. Area (1/2) "))

            # PERIMETER
            if what_to_find==1:
                shape = int(input("Which shape's perimeter? \n1. Square \n2. Rectangle \n3. Circle \n4. Triangle "))
                # SQUARE PERI
                if shape==1:
                    a = float(input("Enter its side length: "))
                    print("Square's perimeter is", a*4)
                # RECTANGLE PERI
                elif shape==2:
                    l = float(input("Enter its length: "))
                    b = float(input("Enter its width: "))
                    print ("Rectangle's perimeter is", 2*(l+b))
                # CIRCLE PERI
                elif shape==3:
                    r = float(input("Enter its radius: "))
                    print("Circle's perimeter is", (pi())*(r)*2)
                # TRIANGLE PERI
                elif shape==4:
                    s1 = float(input("Enter its first side length: "))
                    s2 = float(input("Enter its second side length: "))
                    s3 = float(input("Enter its third side length: "))
                    print("Triangle's perimeter is", s1+s2+s3)
                else:
                    print("Invalid input")
                    continue

            # AREA
            elif what_to_find==2:
                shape = int(input("Which shape's area? \n1. Square \n2. Rectangle \n3. Circle \n4. Triangle "))

                # SQUARE AREA
                if shape==1:
                    a = float(input("Enter its side length: "))
                    print("Square's area is", a*a)
                # RECTANGLE AREA
                elif shape==2:
                    l = float(input("Enter its length: "))
                    b = float(input("Enter its width: "))
                    print ("Rectangle's area is", l*b)
                # CIRCLE AREA
                elif shape==3:
                    r = float(input("Enter its radius: "))
                    print("Circle's area is", (pi())*(r*r))
                # TRIANGLE AREA
                elif shape==4:
                    s1 = float(input("Enter its first side length: "))
                    s2 = float(input("Enter its second side length: "))
                    s3 = float(input("Enter its third side length: "))
                    print("Triangle's area is", heronf(s1, s2, s3))
                else:
                    print("Invalid input")
                    continue

            else:
                print("Invalid input")
                continue
            
            exit_or_not = input("Do you want to exit this calculator(Y/N)? ")
            if exit_or_not in ["y", "Y"]:
                print("Thanks for visiting!")
                break
            elif exit_or_not in ["N", "n"]:
                continue
            else:
                print("You are such an idiot!!!!!")
                quit()


    except Exception as identifier:
        print("Error!", identifier)
        quit()