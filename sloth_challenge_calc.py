def turnCalc(numbers):
    output= []
    for num in str(numbers):
        if num == "1":
            output.append("I")
        elif num =="2":
            output.append("Z")
        elif num == "3":
            output.append("E")
        elif num == "4":
            output.append("H")
        elif num == "5":
            output.append("S")
        elif num == "6":
            output.append("G")
        elif num == "7":
            output.append("L")
        elif num == "8":
            output.append("B")
        elif num == "9":
            output.append("-")
        else:
            output.append("O")
    print("".join(reversed(output)))

turnCalc(707)
turnCalc(5508)
turnCalc(3045)
turnCalc("07734")