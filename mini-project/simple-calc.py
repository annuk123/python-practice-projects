while True:
    first_num = int(input("Enter the first number: "))
    operation = input("enter the operations +, -, *, or /: ")
    sec_num = int(input("Enter the second number: "))

    if operation == "+":
        sum_result = first_num + sec_num
        print(f"the result is {sum_result}")
        

    elif operation == "-":
        sub_result = first_num - sec_num
        print(f"the result is {sub_result}")
        
    elif operation == "*":
        multi_result = first_num * sec_num
        print(f"the result is {multi_result}")
        
    elif operation == "/":
        if sec_num == 0:
            print("your number is 0, use correct number")
            
        else:
            div_result = (first_num / sec_num)
            print(f"the result is {div_result}")     
    else:
        print("the operation is not valid") 


    
    while True:
        question = input("do you want to perform another calculation?(yes/no): ").lower().strip()
        if question in ["yes", 'y', "no", 'n']:
            break
        print("Invalid answer.. please enter yes or no..")

    if question in ["no", 'n']:
        print("goodbye")
        break
 



