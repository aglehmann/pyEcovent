from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")

request = "";
for param in fan.params:
 request += hex(param).replace("0x","").zfill(4)

fan.read_param(request)

#request = "0072" ;
#fan.read_param(request);

# request = b'\xFE\x06\x77'
# request = "0077"
# fan.read_param(request);
