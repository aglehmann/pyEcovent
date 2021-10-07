import time
from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")
for param in fan.params:
 print ( fan.params[param][0] + ": " + str(getattr ( fan, fan.params[param][0])))

#fan.set_state_off();
#time.sleep ( 1 )
#fan.set_state_on();
#fan.set_man_speed(50)
#time.sleep ( 1 )
#fan.update()

# fan.set_speed(1)
# fan.set_state_on();
# fan.set_man_speed(2)
# fan.set_airflow(1)
# print ( fan.state )
# print ( fan.speed )
# print ( fan.man_speed )
# print ( fan.fan1_speed )
# print ( fan.fan2_speed )
# print ( fan.airflow )
