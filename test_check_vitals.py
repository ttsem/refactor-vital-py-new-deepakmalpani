import unittest
from check_vitals import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_temperature_out_of_bounds(self):
        self.assertFalse(vitals_ok(94, 102, 70))
        
    def test_not_ok_when_temperature_out_of_bounds(self):
        self.assertFalse(vitals_ok(108, 102, 70))
        
    def test_ok_when_temperature_in_bounds(self):
        self.assertTrue(vitals_ok(97, 102, 70))
        
    def test_not_ok_when_pulserate_out_of_bounds(self):
        self.assertFalse(vitals_ok(55, 102, 70))
        
    def test_not_ok_when_temperature_out_of_bounds(self):
        self.assertFalse(vitals_ok(108, 102, 70))


if __name__ == '__main__':
  unittest.main()