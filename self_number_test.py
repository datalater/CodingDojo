import unittest

def d(n):
    str_n = str(n)

    result = 0
    for i in str_n:
        result += int(i)

    result += n
    return result


def generatorList(n):
    generator_list = []
    for i in range(1, n+1):
       generator_list.append(d(i))

    return generator_list

def selfNumberList(n):
    total_list = range(1, n+1)
    self_number_set = set(total_list) - set(generatorList(n))

    return self_number_set

def selfNumberSum(n):
    return sum(selfNumberList(n))

class SelfNumberTest(unittest.TestCase):
    def test_function_d(self):
        self.assertEqual(101, d(91))
        self.assertEqual(101, d(100))
        self.assertEqual(2, d(1))

    def test_selfNumberList(self):
        self.assertEqual({1,3,5}, selfNumberList(5))

    def test_selfNumberSum(self):
        self.assertEqual(9, selfNumberSum(5000))

if __name__ == '__main__':
    unittest.main()





# "안녕하세요!"
# "기분이 아주 좋은 날이에요. 유후!"
