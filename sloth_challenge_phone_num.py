#sloth challenge
def phone_formatting(numbers):
    pre= ''.join(map(str,numbers[:3]))
    mid= ''.join(map(str,numbers[3:6]))
    end=''.join(map(str,numbers[6:]))
    output= "(" + pre + ") " + mid + "-" + end
    #print(pre + mid + end)
    print(output)

phone_formatting([1,2,3,4,5,6,7,8,9,0])