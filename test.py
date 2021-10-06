from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")



print("TUKAJ:")
# fan.read_param("0001")
# fan.read_param("000b")
# fan.read_param("0024")
# fan.read_param("0302")
# fan.read_param("0303")
# fan.read_param("0304")
# fan.read_param("002403020303030400a3")
fan.read_param("0001000200060007000B000F00140016001900240025002D00320044004A004B006400650066006F007000720077007C007D007E00830085008600880094009500960099009A009B009C009D009E00A300B700B800B90302030303040305")

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

