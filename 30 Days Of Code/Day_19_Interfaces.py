class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 1:
            return 1
        else:
            factor_sum = 1 + n
            for i in range(2, n // 2 + 1):  # no need to iterate though each number - only the first half.
                if n % i == 0:
                    factor_sum += i
        return factor_sum
        # 6 => 1+2+3+6=12, 20 => 1+2+4+5+10+20=42
        # sum = 0
        # for i in range(1, n+1):
        #     if n % i == 0:
        #         sum += i
        # return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
