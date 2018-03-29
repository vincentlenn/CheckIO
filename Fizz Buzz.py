# An sample of solution to solve 'Fizz Buzz'
def checkio(number):
    s = ('Fizz'*(not number % 3) + ' ' + 'Buzz'*(not number % 5)).strip()
    #print("'Fizz'*(not number % 3):", 'Fizz'*(not number % 3))
    return str(number) if not s else s

print(checkio(9))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"