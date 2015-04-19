class Model:
    def __init__(self):
        # No initialization
        return
    
    def isNumber(self, num):
        try:
            float(num)
            return True
        except:
            return False

    def calculate(self, operation, op1, op2):
        if operation == 1:
            return op1 + op2
        elif operation == 2:
            return op1 - op2
        elif operation == 3:
            return op1 * op2
        elif operation == 4:
            if op2 == 0:
                return "Error: Cannot divide by 0"
            else:
                return op1 / op2
        else:
            # ERROR: Should never reach this point
            return "\nError: Invalid operation\n"
