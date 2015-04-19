from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.firstTime = True
        self.result = 0.0
        self.a = 0.0
        self.b = 0.0
        self.usePrev = 0
    
    def run(self):
        while True:
            self.view.printMenu()
            selection = self.view.inputSelection()
            if selection <= 0:
                continue
            elif selection == 5:
                self.view.terminate()
                return
            elif not self.firstTime:
                if self.model.isNumber(self.result):
                    self.usePrev = self.view.usePrevious(self.result)
                else:
                    self.usePrev = 0
            else:
                self.firstTime = False
            if self.usePrev == 0:
                # Enter both operands
                self.a = self.view.oneOp(1)
                self.b = self.view.oneOp(2)
            elif self.usePrev == 1:
                # Enter second operand
                self.a = self.result
                self.view.printOp(1, self.a)
                self.b = self.view.oneOp(2)
            elif self.usePrev == 2:
                # Enter first operand
                self.a = self.view.oneOp(1)
                self.b = self.result
                self.view.printOp(2, self.b)
            else:
                # ERROR: Should never reach this block
                self.view.printInvalidArg()
                continue
            self.view.printCalc(selection, self.a, self.b)
            self.result = self.model.calculate(selection, self.a, self.b)
            self.view.printResult(self.result)
            if self.view.anotherOp():
                continue
            else:
                return
