# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def msg0():
    print(msg_0)
    
def msg1():
    print(msg_1)
    
def msg2():
    print(msg_2)

def msg3():
    print(msg_3)
    
def msg4():
    print(msg_4)

def msg5():
    print(msg_5)

def msg10():
    print(msg_10)
    
def msg11():
    print(msg_11)

def msg12():
    print(msg_12)
    
def pr_question(v):
    if (v == 10):
        msg10()
    elif (v == 11):
        msg11()
    elif (v == 12):
        msg12()    
    
def is_one_digit(v):
    if (v < 10 and v > -10 and (v % 1 == 0.0)):
        output = True
    else:
        output = False
    return output
    
def check(v1, v2, v3):
    msg = ""
    if (is_one_digit(v1) and is_one_digit(v2)):
        msg = msg + msg_6
    if (((v1 == 1) or (v2 == 1)) and v3 == "*"):
        msg = msg + msg_7
    if (((v1 == 0) or (v2 == 0)) and (v3 in ["*","+","-"])):
        msg = msg + msg_8
    if (msg != ""):
        msg = msg_9 + msg
        print (msg)
    
test = True
operands = ["+", "-", "*", "/"]
memory = 0

valid_operations = ["+", "-", "/", "*"]
running = True
memory = 0
while running:
    msg0()
    user_input = input()
    x, operation, y = user_input.split()

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        msg1()
        continue

    if operation not in valid_operations:
        msg2()
        continue
    result = 0
    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        if y == 0:
            check(x,y,operation)
            msg3()
            continue
        else:
            result = x / y
    check(x,y,operation)
    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        msg4()
        answer = input()
        if answer == "y":
            if (is_one_digit(result)):
                msg_index = 10
                pr_question(msg_index)
                answer = input()
                if (answer == "y"):
                    while ( msg_index < 12 and answer == "y"):
                        msg_index = msg_index + 1
                        pr_question(msg_index)
                        answer = input()
                        if (msg_index == 12):
                            memory = result
                elif (answer == "n"):
                    memory = result
                else:
                    continue                    
            else:
                memory = result

    answer = ""
    while answer != "y" and answer != "n":
        msg5()
        answer = input()
        if answer == "n":
            running = False

