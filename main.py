from controller import *

while True:
  if True == I1.get_state():
    # Convert from degree (0..360) to internal (0..72); 72/360=1/5
    M1.set_distance(5 / 5 , None)
  else:
    M1.stop()
