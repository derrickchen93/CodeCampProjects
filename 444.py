# Takes 2 inputs, a list containing the arithmetic functions and a boolean
def arithmetic_arranger(problems):
    top = list()
    bottom = list()
    operand = list()
    top2 = list()
    bottom2 = list()
    operand2 = list()
    storeval = list()
    arranged_problems = ""
    if len(problems) == 2 and type(problems[1]) == bool:
        storage = problems[0]
        bool1 = problems[1]
    elif type(problems[0]) != str:
        storage = problems[0]
    else:
        storage = problems

    if len(storage) > 5:
        return "Error: Too many problems."

    
    for equation in storage:
        store = equation.split(" ")
        if store[1] != "+" and store[1] != "-":
            return "Error: Operator must be '+' or '-'."
        try:
            store[0] = int(store[0])
            store[2] = int(store[2])
            if len(str(store[0])) > 4 or len(str(store[2])) > 4:
                return "Error: Numbers cannot be more than four digits."
        except:
            return "Error: Numbers must only contain digits."
        top.append(store[0])
        bottom.append(store[2])
        operand.append(store[1])

    for t,b,o in zip(top,bottom,operand):
        if len(str(t)) > len(str(b)):
            calc = len(str(t)) - len(str(b)) + 1
            store = o + (" " * calc) + str(b)
            top2.append((" " * (len(store) - len(str(t)))) + str(t) )
            bottom2.append(store)
        else:
            store = f"{o} {b}"
            top2.append((" " * (len(store) - len(str(t)))) + str(t) )
            bottom2.append(store)
    
    for x in range(len(top)):
        if operand[x] == "+":
            store = top[x] + bottom[x]
        else:
            store = top[x] - bottom[x]
        storeval.append(store)

    for t,b in zip(top2,bottom2):
        operand2.append("-" * max(len(t),len(b)))
    
    for x in range(len(storeval)):
        storeval[x] = " " * (len(operand2[x]) -  len(str(storeval[x]))) + str(storeval[x])

    for x in range(len(top2)-1):
        arranged_problems += f"{top2[x]}    "
    arranged_problems += (top2[-1] + "\n")

    for x in range(len(bottom2)-1):
        arranged_problems += f"{bottom2[x]}    "
    arranged_problems += (bottom2[-1] + "\n")

    for x in range(len(operand2)-1):
        arranged_problems += f"{operand2[x]}    "
    arranged_problems += (operand2[-1]) + "\n"

    try:
        if bool1:
            for x in range(len(storeval)-1):
                arranged_problems += f"{storeval[x]}    "
            arranged_problems += storeval[-1] + "\n"
    except:
        abc = 0

    return arranged_problems
    
