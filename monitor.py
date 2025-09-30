from time import sleep
import sys

def show_loading(number_of_seconds):
  for _ in range(number_of_seconds):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)

def check_temperature(temperature):
  if temperature > 102 or temperature < 95:
    show_loading(12)
    return False
  return True

def check_pulserate(pulse_rate):
  if pulse_rate < 60 or pulse_rate > 100:
    print('Pulse Rate is out of range!')
    show_loading(12)
    return False
  return True

def check_spo2(spo2):
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
    show_loading(12)
    return False
  return True
  
def vitals_ok(temperature, pulse_rate, spo2):
  return check_temperature(temperature) and check_pulserate(pulse_rate) and check_spo2(spo2)