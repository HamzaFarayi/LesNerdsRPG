import math
import random
import time


def select():
    mode = input("Training, Test or back to mode selection? \ntr or te or B: \n - ")
    if mode == "tr": 
      training()

    elif mode == "te":
        test()

    elif mode == "B":
        selection()
    
    else:
        select()

def training():

    try:
        dif = int(input("Choose difficulty: \n: \n 1 = easy \n 2 = medium \n 3 = hard\n\n - "))
      
    except:
        print("Error")
        training()
    if dif < 4:
        if dif > 0:
            if dif == 1:
                a = random.randint(1,50)
                b = random.randint(1,50)
                c = random.randint(1,9)
                d = random.randint(1,9)
                e = random.randint(1,9)

            elif dif == 2:
                a = random.randint(1,99)
                b = random.randint(1,99)
                c = random.randint(1,11)
                d = random.randint(1,99)
                e = random.randint(1,99)

            elif dif == 3:
                a = random.randint(1,999)
                b = random.randint(1,999)
                c = random.randint(1,99)
                d = random.randint(1,999)
                e = random.randint(1,999)

            else:
              print("Error")
              training()
        else:
          print("Error")
          training()
    else: 
      print("Error")
      training()

    try:
      opp = int(input("Which operation?\n\n 1 = +\n 2 = -\n 3 = *\n 4 = /\n\n - "))

      if opp == 1:
        print(a, "+", b)
        startpoint = time.time()

        answer = input("\nEnter answer: ")
        endpoint = time.time()
    
        if answer == str(a+b):
            print("\nTrue ᕦ(ò_óˇ)ᕤ")
    
        else:
            print("\nFalse (=^▽^)σ")

      elif opp == 2:
        print(a, "-", b)
        startpoint = time.time()

        answer = input("\nEnter answer: ")
        endpoint = time.time()
        
        if answer == str(a-b):
            print("\nTrue ᕦ(ò_óˇ)ᕤ")

        else:
            print("\nFalse (=^▽^)σ")

      elif opp == 3:
        print(d, "*", e)
        startpoint = time.time()

        answer = input("\nEnter answer: ")
        endpoint = time.time()
        
        if answer == str(d*e):
            print("\nTrue ᕦ(ò_óˇ)ᕤ")

        else:
            print("\nFalse (=^▽^)σ")

      elif opp == 4:
        print(a*c, "/", c)
        startpoint = time.time()

        answer = input("\nEnter answer: ")
        endpoint = time.time()

        if answer == str(a):
            print("\nTrue ᕦ(ò_óˇ)ᕤ")

        else:
            print("\nFalse (=^▽^)σ")
        timetaken = endpoint-startpoint    
        print(math.floor(timetaken), "s")  
      
    except:
        print("Error")
        training()
        
    con = input("Continue? Y or B (B = back to te / tr selection): ")
    if con == "Y":
        training()

    elif con == "B":
        select()

    else:
        print("Error")
        select()

    
def test():
    try:
      problem = int(input("\nHow many calculations?: ")) 
    except:
      print("Error")
      test()
    if problem <= 0:
      print("Error")
      test()
      
    try:
        dif = int(input("Choose difficulty: \n\n 1 = easy \n 2 = medium \n 3 = hard\n\n - "))
    except:
        print("Error")
        test()
    if dif < 4:
        if dif > 0:
            pro = problem 
            print("Readyyy?")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("GOOO!")
            score = 0
            tim = []
            while problem != 0:

                if dif == 1:
                    a = random.randint(1,50)
                    b = random.randint(1,50)
                    c = random.randint(1,9)
                    d = random.randint(1,9)
                    e = random.randint(1,9)

                elif dif == 2:
                    a = random.randint(1,99)
                    b = random.randint(1,99)
                    c = random.randint(1,11)
                    d = random.randint(1,99)
                    e = random.randint(1,99)

                elif dif == 3:
                    a = random.randint(1,999)
                    b = random.randint(1,999)
                    c = random.randint(1,99)
                    d = random.randint(1,999)
                    e = random.randint(1,999)
                    
                
                operation = random.randint(1,4)
                time.sleep(1)
                startpoint = time.time()
              
                if operation == 1:
                    print("\n",a, "+", b)
                    ans = input("\nEnter answer: ")
                    endpoint = time.time()
                    tim.append(math.floor(endpoint-startpoint))
                      
                    if ans == str(a+b):
                        print("\nTrue ᕦ(ò_óˇ)ᕤ")
                        score += 1
               
                    else:
                        print("\nFalse (=^▽^)σ")

                if operation == 2:
                    print("\n", a, "-", b)
                    ans = input("\nEnter answer: ")
                    endpoint = time.time()
                    tim.append(math.floor(endpoint-startpoint))

                    if ans == str(a-b):
                        print("\nTrue ᕦ(ò_óˇ)ᕤ")
                        score += 1

                    else:
                        print("\nFalse (=^▽^)σ")

                if operation == 3:
                    print("\n", d, "*", e)
                    ans = input("\nEnter answer: ")
                    endpoint = time.time()
                    tim.append(math.floor(endpoint-startpoint))

                    if ans == str(d*e):
                        print("\nTrue ᕦ(ò_óˇ)ᕤ")
                        score += 1

                    else:
                        print("\nFalse (=^▽^)σ")

                if operation == 4:
                    print("\n", a*c, "/", c)
                    ans = input("\nEnter answer: ")
                    endpoint = time.time()
                    tim.append(math.floor(endpoint-startpoint))

                    if ans == str(a):
                        print("\nTrue ᕦ(ò_óˇ)ᕤ")
                        score += 1

                    else:
                        print("\nFalse (=^▽^)σ")
                  
                problem -= 1
            su = sum(tim)
            per = sum(tim)/len(tim) 
            sco = score*100/pro
            pp = 100 - sco
            print(len(tim))
            print("time taken: ", math.floor(su), "s")
            print("time average: ", math.floor(per), "s")
            print("\n", score, "calculation(s) were(was) correct!" )
            print("True: ", math.floor(sco), "%" )
            print("False: ", math.floor(pp), "%\n")
              
            cont = input("Continue? Y or B (B= back to tr / te selection): ")
            if cont == "Y":
              test()

            elif cont == "B":
              select()
                             
            else:
              print("Error")
              select()
      
        else:
            print("Error")
            select()
    else:
        print("Error")
        select()


def calculator():
  Nerds = 1
  try:
    num1 = int(input("Enter number1: "))
  except:
    print("Error")
    calculator()
  while Nerds == 1:  
    try:
      operation = input("Enter operation (+,-,*,/,^,mod, !, cos, sin, tan): ")
    except:
      print("Error")
      Nerds -= 1
      calculator()

    if operation == "!":
        num1 = math.factorial(num1)
        print(num1)

    elif operation == "cos":
        num1 = math.cos(num1)
        print(num1)

    elif operation == "sin":
        num1 = math.sin(num1)
        print(num1)

    elif operation == "tan":
        num1 = math.tan(num1)
        print(num1)

    else:

        try:  
          num = int(input("Enter number: "))
        except:
          print("Error")
          Nerds -= 1
          calculator()
        
        if operation == "+":
          num1 += num     
          print(int(num1))
        
        elif operation == "-":   
          num1 -= num
          print(num1)  
        elif operation == "*":
          num1 *= num
          print(num1)
        
        elif operation == "/":
          num1 /= num
          print(num1)        
        
        elif operation == "^":
          num1 **= num
          print(num1)
          
        elif operation == "mod":
          num1 = num1 % num 
          print(num1)
          
        else:
          print("Error! Enter correct operation")
          Nerds -= 1
          calculator()
      

    next = input("Continue calculation with the result? \nY, N or B (B = back to mode selection): ",)

    if next == "Y":
      print("-----------------------------    Your number: ", num1)

    elif next == "N":
      Nerds -= 1
      calculator()
      
    elif next =="B":
      Nerds -= 1
      selection()
                
    else:
      print("Error")
      Nerds -= 1
      calculator()

      
def selection():
    first = input("Calculator, Calculation or end? \nAnswer with 1(calculator), 2(calculation) or end\n")
    
    if first == "1":
      calculator()
  
    elif first == "2":
      select()
  
    elif first == "end":
      print("Wiedersehen")
      
    else:
      print("Error")
      selection()
  
 
selection()
