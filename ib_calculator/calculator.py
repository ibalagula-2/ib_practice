
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc_add(self):
        return self.num1 + self.num2    

    def calc_multiply(self):
        return self.num1 * self.num2     

def main():
    c = Calculator(3,4)
    add_val = c.calc_add()
    print( "result of addition " + str(add_val))
    mult_val = c.calc_multiply()
    print( "result of multiplication " + str(mult_val))

if __name__ == '__main__':
    main()