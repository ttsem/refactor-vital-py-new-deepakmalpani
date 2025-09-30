from loading_utils import show_loading

def check_temperature(temperature):
  return temperature > 102 or temperature < 95

def check_pulserate(pulse_rate):
  return pulse_rate < 60 or pulse_rate > 100

def check_spo2(spo2):
  if spo2 < 90:
    print('Oxygen Saturation out of range!')
    show_loading(12)
    return False
  return True
  
def vitals_ok(temperature, pulse_rate, spo2):
  if check_temperature(temperature): 
    show_loading(12)
    return False
  if check_pulserate(pulse_rate):
    print('Pulse Rate is out of range!')
    show_loading(12)
    return False
  return check_spo2(spo2)