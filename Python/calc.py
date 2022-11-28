import input

ans = 0

if (input.error_flag == 0):
    if(input.operation == "plus"):
        ans = input.num1 + input.num2

    elif(input.operation == "minus"):
        ans = input.num1 - input.num2

    elif(input.operation == "cross"):
        ans = input.num1 * input.num2

    elif(input.operation == "devision"):
        ans = input.num1 / input.num2

    print("Data1 : " + str(input.num1))
    print("Data2 : " + str(input.num2))
    print("type : " + input.operation)
    print("answer : " + str(ans))

else:
    ans = "error: incorrect input"
    print(ans)
    
