import unittest
from mathematics import Mathematics
#öğrenmek amaçlıdır.
class TESTING(unittest.TestCase):# Kalıtımı kullanıyoruz.
    def test_sumTwoNumbers(self): # test edeceğimiz fonksiyonun başına test yazarak fonksiyonu oluşturuyoruz.
        self.assertEqual((2+3),5) # Burdada test başarısız ise programın  çalışması başarısız ise çökmesini sağlıyoruz.
    # 2+3, 5e eşit ise başarılı olduğundan program çalışır.
    def test_multiplyTwoNumbers(self):
        self.assertEqual((2*3),6)  

if __name__ == "main":
    unittest.main()
#Profesyonel biçimde

class MyTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.math = Mathematics()
    
    def test_sumTwoNumbers(self):
        result = self.math.sumTwoNumbers(10,30)
        self.assertEqual(result,40)
    
    def test_multiplyTwoNumbers(self):
        result = self.math.multiplyTwoNumbers(10,30)
        self.assertEqual(result,300)
        
        
        
        
        
        
        
        
        
    def tearDown(self):
        pass