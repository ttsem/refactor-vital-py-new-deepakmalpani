from error_messages import ERROR_MESSAGES
from message_utils import handle_failure, show_loading

def check_temperature(temperature):
  return temperature > 102 or temperature < 95

def check_pulserate(pulse_rate):
  return pulse_rate < 60 or pulse_rate > 100

def check_spo2(spo2):
  return spo2 < 90
  
def vitals_ok(temperature, pulse_rate, spo2):
  if check_temperature(temperature): 
    return False
  if check_pulserate(pulse_rate):
    handle_failure(ERROR_MESSAGES["pulse_rate"])
    return False
  if check_spo2(spo2):
    handle_failure(ERROR_MESSAGES["spo2"])
    return False
  return True