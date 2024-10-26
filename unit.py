import unittest


# Función FizzBuzz original
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


class TestFizzBuzz(unittest.TestCase):

    # Happy path
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(6), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(10), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')

    def test_number(self):
        self.assertEqual(fizzbuzz(1), '1')
        self.assertEqual(fizzbuzz(2), '2')

    # Edge cases
    def test_zero(self):
        self.assertEqual(fizzbuzz(0), 'FizzBuzz')

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz(-3), 'Fizz')
        self.assertEqual(fizzbuzz(-5), 'Buzz')
        self.assertEqual(fizzbuzz(-15), 'FizzBuzz')

    def test_large_numbers(self):
        self.assertEqual(fizzbuzz(3000), 'FizzBuzz')
        self.assertEqual(fizzbuzz(3003), 'Fizz')
        self.assertEqual(fizzbuzz(5000), 'Buzz')


if __name__ == '__main__':
    unittest.main()
