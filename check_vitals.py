from message_utils import handle_failure

def check_temperature(temperature):
  return not (temperature > 102 or temperature < 95)

def check_pulserate(pulse_rate):
  return not (pulse_rate < 60 or pulse_rate > 100)

def check_spo2(spo2):
  return not (spo2 < 90)
  
def vitals_ok(temperature, pulse_rate, spo2):
  checks = [
    (check_temperature, temperature, "temperature"),
    (check_pulserate, pulse_rate, "pulse_rate"),
    (check_spo2, spo2, "spo2")
  ]
  for check_function, vital_param, error_key in checks:
    if check_function(vital_param):
      handle_failure(error_key)
      return False
    
  return True