from time import sleep
import sys

def show_loading(number_of_seconds):
  for _ in range(number_of_seconds):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
  
def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    show_loading(12)
    return False
  if pulseRate < 60 or pulseRate > 100:
    print('Pulse Rate is out of range!')
    show_loading(12)
    return False
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
    show_loading(12)
    return False
  return True