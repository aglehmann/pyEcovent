from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")

for param in fan.params:
 print ( fan.params[param][0] + ": " + str(getattr ( fan, fan.params[param][0])))


