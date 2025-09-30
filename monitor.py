
from time import sleep
import sys

def print_loading_statement():
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
  
def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    print_loading_statement()
    return False
  if pulseRate < 60 or pulseRate > 100:
    print('Pulse Rate is out of range!')
    print_loading_statement()
    return False
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
    print_loading_statement()
    return False
  return True