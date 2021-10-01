from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")



print("TUKAJ:")
# fan.read_param("000b")
fan.read_param("0024")
fan.read_param("0302")
fan.read_param("0303")
fan.read_param("0304")
fan.read_param("002403020303030400a3")

#print(fan.state)
#print(fan.speed)
#print(fan.man_speed)
#print(fan.airflow)
#print(fan.humidity)
#
#fan.set_speed(2)
#print(fan.speed)
#fan.set_state_off()
#fan.set_state_on()

