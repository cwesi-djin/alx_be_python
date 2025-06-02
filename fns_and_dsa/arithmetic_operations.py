def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return(num1 + num2)
    elif operation == "subtract":
        return(num1 - num1)
    elif operation == "multiply":
        return(num1 * num1)
    elif operation == "divide":
        if num2 == 0:
            return "Error number cannot be divide by zero"
        else:
            return(num1 / num1)
    else:
        return "Invalid operation, try again"