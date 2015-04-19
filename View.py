class View:
    def __init__(self):
        # No initialization
        return
    
    def get_input(self, message):
        try: 
            return raw_input(message)
        except:
            return input(message)

    def printMenu(self):
        print("")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("")

    def inputSelection(self):
        try:
            selection = int(self.get_input("Select an option from above: "))
        except:
            print("\nError: Invalid input\n")
            return 0
        if selection < 1 or selection > 5:
            print("\nError: Invalid selection\n")
            return 0
        else:
            return selection

    def usePrevious(self, prevRes):
        print("")
        while True:
            print("Use previous result (" + str(prevRes) + ")?")
            print("0. Enter two new operands")
            print("1. Set the first operand to " + str(prevRes))
            print("2. Set the second operand to " + str(prevRes))
            print("")
            try:
                selection = int(self.get_input("Select an option from above: "))
            except:
                print("\nError: Invalid input\n")
                continue
            if selection < 0 or selection > 2:
                print("\nError: Invalid selection\n")
                continue
            else:
                return selection

    def oneOp(self, op):
        opString = ""
        if op == 1:
            opString = "first"
        else:
            opString = "second"
        while True:
            try:
                a = float(self.get_input("Enter the " + opString + " operand: "))
            except:
                print("\nError: Not a valid operand\n")
                continue
            break
        return a

    def anotherOp(self):
        while True:
            selection = self.get_input("Perform another operation? Y/N: ")
            if len(selection) < 1:
                print("\nError: Invalid input\n")
                continue
            elif selection[0] == 'Y' or selection[0] == 'y' or selection[0] == 'N' or selection[0] == 'n':
                break
            else:
                print("\nError: Invalid input\n")
                continue
        if selection[0] == 'N' or selection[0] == 'n':
            print("\nGoodbye")
            return False
        else:
            return True

    def printOp(self, opNum, op):
        if opNum == 1:
            print("First operand set to " + str(op))
        elif opNum == 2:
            print("Second operand set to " + str(op))
        else:
            # ERROR: Should never reach this point
            print("\nError: Invalid operand\n")

    def printCalc(self, operation, op1, op2):
        print("")
        if operation == 1:
            print("Addition: " + str(op1) + " + " + str(op2))
        elif operation == 2:
            print("Subraction: " + str(op1) + " - " + str(op2))
        elif operation == 3:
            print("Multiplication: " + str(op1) + " * " + str(op2))
        elif operation == 4:
            print("Division: " + str(op1) + " / " + str(op2))
        else:
            # ERROR: Should never reach this point
            print("\nError: Invalid operation\n")

    def printResult(self, result):
        print("Result: " + str(result))
        print("")

    def printInvalidArg(self):
        print("\nError: Invalid argument\n")

    def terminate(self):
        print("\nGoodbye")
