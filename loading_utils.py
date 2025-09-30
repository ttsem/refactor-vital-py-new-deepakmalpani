import sys
from time import sleep

def show_loading(number_of_seconds):
  for _ in range(number_of_seconds):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)