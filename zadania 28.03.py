from traceback import print_tb
from unittest.mock import Mock
# Zad1
m1 = Mock(name = "Test Mock")
print(m1)
m1.get_data.return_value = 567

result = m1.get_data('user')
print(result)

m1.get_data_assert_called_with('user')
print(m1.get_data.call_args)

#Zad2
m2 = Mock(autospec = True)
m2.method.side_effect = [10,20,30]

def side_effect_func(*args):
    args = [arg*2 for arg in args]
    return args


m2.get_data.side_effect = side_effect_func

print(m2.get_data(7,-8))

m2.get_data.side_effect = TypeError("Wrong Type")

try:
    print(m2.get_data())
except TypeError as er:
    print(er)

#Zad3
m3 = Mock()
m3.some_method(4,5,6)
m3.some_method()
m3.some_method("a",name = "TEST")
m3.some_method(a=99.2, b = -4.5)

print(m3.some_method.called)
print(m3.some_method.call_count)
print(m3.some_method.call_args)
print(m3.some_method.call_args_list)


#Zad10
class DataService:
    def __init__(self,api_client):
        self.api_client = api_client


    def fetch_user_data(self,args):
      return self.api_client.get
    pass




#plik test_data_service.py
#Zad10
import unittest
from unittest.mock import Mock
from zad1 import DataService

class TestDataService(unittest.TestCase):

    def setUp(self):
        self.api_mock = Mock()
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_positive_values(self):
        self.api_mock.get_data.side_effect = ["Jan","Sylwia"]
        result1 = self.service.fetch_user_data()
        self.assertEqual(result1,"Jan")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()


