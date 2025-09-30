import unittest
from check_vitals import check_pulserate, check_spo2, check_temperature


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_temperature_out_of_minbounds(self):
      self.assertFalse(check_temperature(94))
        
    def test_not_ok_when_temperature_out_of_maxbounds(self):
      self.assertFalse(check_temperature(108))
        
    def test_ok_when_temperature_in_bounds(self):
      self.assertTrue(check_temperature(97))
        
    def test_not_ok_when_pulserate_out_of_minbounds(self):
      self.assertFalse(check_pulserate(55))
        
    def test_not_ok_when_pulserate_out_of_maxbounds(self):
      self.assertFalse(check_pulserate(102))
        
    def test_ok_when_pulserate_in_bounds(self):
      self.assertTrue(check_pulserate(75))
    
    def test_not_ok_when_spo2_out_of_bounds(self):
      self.assertFalse(check_spo2(75))


if __name__ == '__main__':
  unittest.main()