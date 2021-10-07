
""" Version  """
__version__ = "0.8.4"

"""Library to handle communication with Wifi ecofan from TwinFresh / Blauberg"""
import socket
import sys
import time

class Fan(object):
    """Class to communicate with the ecofan"""
    
    HEADER = f'FDFD'
    func = dict()
    
    func['read'] = "01"
    func['write'] = "02"
    func['write_return'] = "03"
    func['inc'] = "04"
    func['dec'] = "05"
    func['resp'] = "06"

    prmt = dict()
    prmt['state'] = "0001"
    prmt['speed'] = "0002"
    prmt['boost_status'] = "0006"
    prmt['timer_mode'] = "0007"
    prmt['timer_counter'] = "000B"
    prmt['humidity_sensor_state'] = "000F"
    prmt['relay_sensor_state'] = "0014"
    prmt['analogV_sensor_state'] = "0016"
    prmt['humidity_treshold'] = "0019"
    prmt['battery_voltage'] = "0024"
    prmt['humidity'] = "0025"
    prmt['analogV'] = "002D"
    prmt['relay_status'] = "0032"
    prmt['man_speed'] = "0044"
    prmt['fan1_speed'] = "004A"
    prmt['fan2_speed'] = "004B"
    prmt['filter_timer_countdown'] = "0064"
    prmt['filter_timer_reset'] = "0065" 
    prmt['boost_time'] = "0066"
    prmt['rtc_time'] = "006F"
    prmt['rtc_date'] = "0070"
    prmt['weekly_schedule_state'] = "0072"
    prmt['weekly_schedule_setup'] = "0077"
    prmt['device_search'] = "007C"
    prmt['device_password'] = "007D"
    prmt['machine_hours'] = "007E"
    prmt['reset_alarms'] = "0080"
    prmt['alarm_state'] = "0083"
    prmt['cloud_server_state'] = "0085"
    prmt['firmware'] = "0086"
    prmt['factory_reset'] = "0087"
    prmt['filter_replacement_status'] = "0088"
    prmt['wifi_operation_mode'] = "0094"
    prmt['wifi_name'] = "0095"
    prmt['wifi_pasword'] = "0096"
    prmt['wifi_enc_type'] = "0099"
    prmt['wifi_freq_chnnel'] = "009A"
    prmt['wifi_dhcp'] = "009B"
    prmt['wifi_assigned_ip'] = "009C"
    prmt['wifi_assigned_netmask'] = "009D"
    prmt['wifi_main_gateway'] = "009E"
    prmt['wifi_apply_and_quit'] = "00A0"
    prmt['wifi_discard_and_quit'] = "00A2"
    prmt['curent_wifi_ip'] = "00A3"

    states = ['off', 'on' , 'togle']
    speeds = [ 'low', 'medium', 'high', 'manual' ]
    timer_modes = [ 'off', 'night', 'party' ]
    statuses = [ 'off', 'on' ]
    airflows = [ 'ventilation', 'heat recovery', 'supply' ]
    alarms = [ 'no', 'alarm', 'warning' ]
    filters = [ 'filter replacement not required' , 'replace filter' ]
    unit_types = {
                    0x0300: 'Vento Expert A50-1/A85-1/A100-1 W V.2', 
                    0x0400: 'Vento Expert Duo A30-1 W V.2', 
                    0x0500: 'Vento Expert A30 W V.2' }
    
    wifi_operation_modes = {
        1: 'client' ,
        2: 'ap' 
    }
    wifi_enc_types =  {  
            48: 'Open', 
            50: 'wpa-psk' , 
            51: 'wpa2_psk',  
            52: 'wpa_wpa2_psk' 
    } 
    wifi_dhcps = [ 'STATIC', 'DHCP', 'Invert' ]
    
    params = {
        0x0001: [ 'state', states ],
        0x0002: [ 'speed', speeds ],
        0x0006: [ 'boost_status', statuses ],
        0x0007: [ 'timer_mode', timer_modes ],
        0x000b: [ 'timer_counter', None ],
        0x000f: [ 'humidity_sensor_state', states ],
        0x0014: [ 'relay_sensor_state', states ],
        0x0016: [ 'analogV_sensor_state', states ],
        0x0019: [ 'humidity_treshold', None ],
        0x0024: [ 'battery_voltage', None ],
        0x0025: [ 'humidity', None ],
        0x002d: [ 'analogV', None ],
        0x0032: [ 'relay_status', statuses ],
        0x0044: [ 'man_speed', None ],
        0x004a: [ 'fan1_speed', None ],
        0x004b: [ 'fan2_speed', None ],
        0x0064: [ 'filter_timer_countdown', None ],
        # 0x0065: [ 'filter_timer_reset', None ],
        0x0066: [ 'boost_time', None ],
        0x006f: [ 'rtc_time', None ],
        0x0070: [ 'rtc_date', None ],
        0x0072: [ 'weekly_schedule_state', states ],
        # 0x0077: [ 'weekly_schedule_setup', None ],
        0x007c: [ 'device_search', None ],
        0x007d: [ 'device_password', None ],
        0x007e: [ 'machine_hours', None ],
        # 0x0080: [ 'reset_alarms', None ],
        0x0083: [ 'alarm_status', alarms ],
        0x0085: [ 'cloud_server_state', states ],
        0x0086: [ 'firmware', None ],
        # 0x0087: [ 'factory_reset', None ],
        0x0088: [ 'filter_replacement_status', statuses ],
        0x0094: [ 'wifi_operation_mode', wifi_operation_modes  ],
        0x0095: [ 'wifi_name' , None ],
        0x0096: [ 'wifi_pasword', None ],
        0x0099: [ 'wifi_enc_type', wifi_enc_types ],
        0x009a: [ 'wifi_freq_chnnel', None ],
        0x009b: [ 'wifi_dhcp', wifi_dhcps  ],
        0x009c: [ 'wifi_assigned_ip', None ],
        0x009d: [ 'wifi_assigned_netmask', None ],
        0x009e: [ 'wifi_main_gateway', None ],
        # 0x00a0: [ 'wifi_apply_and_quit', None ],
        # 0x00a2: [ 'wifi_discard_and_quit', None ],
        0x00a3: [ 'curent_wifi_ip', None ],
        0x00b7: [ 'airflow' , airflows ],
        0x00b8: [ 'analogV_treshold', None ],
        0x00b9: [ 'unit_type', unit_types ],
        0x0302: [ 'night_mode_timer', None ],
        0x0303: [ 'party_mode_timer', None ],
        0x0303: [ 'party_mode_timer', None ],
        0x0304: [ 'humidity_status', statuses ],
        0x0305: [ 'analogV_status', statuses ]
    }
    

    def __init__(self, host, fan_id="003A00345842570A", password="1111", name="ecofanv2", port=4000 ):
        self._name = name
        self._host = host
        self._port = port
        self._type = "02"
        self._id = fan_id
        self._pwd_size = 0
        self._password = password

        # self.update_all()
        # self.read_param('000B')

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(4)
        self.socket.connect((self._host, self._port))
        return self.socket

    def str2hex(self,str_msg):
        return "".join("{:02x}".format(ord(c)) for c in str_msg)
        
    def hex2str(self,hex_msg):
        return "".join( chr(int("0x" + hex_msg[i:(i+2)],16)) for i in range(0,len(hex_msg),2))

    def hexstr2tuple(self,hex_msg):
        return [int(hex_msg[i:(i+2)], 16) for i in range(0,len(hex_msg), 2)]
        
    def chksum(self,hex_msg):
        checksum = hex(sum(self.hexstr2tuple(hex_msg))).replace("0x","").zfill(4)
        byte_array = bytearray.fromhex(checksum)
        chksum = hex(byte_array[1]).replace("0x","").zfill(2) + hex(byte_array[0]).replace("0x","").zfill(2)
        return f"{chksum}"

    def get_size(self,str):
        return hex(len(str)).replace("0x","").zfill(2)

    def get_header(self):
        id_size = self.get_size(self._id)
        pwd_size = self.get_size (self._password)
        id = self.str2hex(self._id)
        password = self.str2hex(self._password)
        str = f"{self._type}{id_size}{id}{pwd_size}{password}"
        return str

    def send(self, data):
        self.socket = self.connect()
        payload = self.get_header() + data
        payload = Fan.HEADER + payload + self.chksum(payload)
        return self.socket.sendall( bytes.fromhex(payload))

    def receive(self):
        try:
            response = self.socket.recv(256)
            return response
        except socket.timeout:
            return None

    def read_param(self, input ):
        out = ""
        parameter = ""
        for i in range (0,len(input), 4):
            out = input[i:(i+4)] ;
            if out[:2] != "00":
                    out = "ff" + out
            # if out[:4] == "0077":
            #   out = "fe0677000101ee0101"
            parameter += out ;
        data = Fan.func['read'] + parameter
        time.sleep(0.01)
        self.send(data)
        response = self.receive()
        if response:
            return self.parse_response(response)
        else:
            return 0

    def update_all(self):
        # print ("Update all")
        data = Fan.func['read'] + Fan.prmt['state'] + Fan.prmt['speed'] + Fan.prmt['boost_status'] + Fan.prmt['timer_mode'] + Fan.prmt['timer_counter'] + Fan.prmt['humidity_sensor_state'] + Fan.prmt['relay_sensor_stated']
        self.send(data)
        response = self.receive()
        if response:
            return self.parse_response(response)
        else:
            return 0

    def update_state(self):
        self.send(f'010001')
        response = self.receive()
        if response:
            # print ( response )
            self.parse_response(response)
            self.socket.close()
            return 0
        else:
            return 1

    def update(self):
        self.send(bytes.fromhex('0100'))
        response = self.receive()
        if response:
            self.parse_response(response[6:])
            self.socket.close()
            return 0
        else:
            return 1

    def set_state_on(self):
        if self.state == 'unknown':
            self.update()

        if self.state ==  'off':
            cmd = bytes.fromhex('0300')
            self.send(cmd)
            self.socket.close()

        self.update()

    def set_state_off(self):
        if self.state == 'unknown':
            self.update()

        if self.state ==  'on':
            cmd = bytes.fromhex('0300')
            self.send(cmd)
            self.socket.close()

        self.update()

    def set_speed(self, speed):
        if speed >= 1 and speed <= 3:
            cmd = '04' + '{0:0{1}x}'.format(speed,2)
            self.send(bytes.fromhex(cmd))
            self.socket.close()

            self.update()

    def set_man_speed(self, speed):
        if speed >= 22 and speed <= 255:
            cmd = '05' + '{0:0{1}x}'.format(speed,2)
            self.send(bytes.fromhex(cmd))
            self.socket.close()

            self.update()

    def set_airflow(self, val):
        if val >= 0 and val <= 2:
            cmd = '06' + '{0:0{1}x}'.format(val,2)
            self.send(bytes.fromhex(cmd))
            self.socket.close()

            self.update()

    def parsebytes(self, bytestring, params):
        i = iter(bytestring)
        for param in i:
            value = [next(i) for _ in range(params[param][0])]
            yield(param,value)

    def parse_response(self,data):
        pointer = 20 ; # discard header bytes 
        length = len(data) - 2 ;
        pwd_size = data[pointer] 
        pointer += 1
        password = data[pointer:pwd_size]
        pointer += pwd_size
        function = data[pointer]
        pointer += 1
        # from here parsing of parameters begin
        payload=data[pointer:length]
        response = bytearray()
        ext_function = 0
        value_counter = 1
        high_byte_value = 0
        parameter = 1 ;
        # print ("payload:" + str (payload.hex()))
        for p in payload:
            # print (hex(p)) #.replace("0x","").zfill(2))
            # print ( "par: " + str(parameter) + " count: " + str(value_counter) + " ext: " + hex (ext_function) )
            if parameter and p == 0xff:
                ext_function = 0xff
                # print ( "def ext:" + hex(0xff) )
            elif parameter and p == 0xfe:
                ext_function = 0xfe
                # print ( "def ext:" + hex(0xfe) )
            elif parameter and p == 0xfd:
                ext_function = 0xfd
                # print ( "dev ext:" + hex(0xfd) )
            else:
                if ext_function == 0xff:
                    high_byte_value = p
                    ext_function = 1
                elif ext_function == 0xfe:
                    value_counter = p
                    ext_function = 2
                elif ext_function == 0xfd:
                    None
                else:
                    if ( parameter == 1 ):
                        # print ("appending: " + hex(high_byte_value))
                        response.append(high_byte_value)
                        parameter = 0
                    else:
                        value_counter -= 1
                    response.append(p)

            if value_counter <= 0:
                parameter = 1
                value_counter = 1
                high_byte_value = 0
                setattr ( self, Fan.params[int(response[:2].hex(),16)][0], response[2:].hex())
                response = bytearray()

        payload = data[pointer:length]
        return payload.hex()       

    @property
    def name(self):
        return self._name

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, ip):
        try:
            socket.inet_aton(ip)
            self._host = ip
        except socket.error:
            sys.exit()
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = pwd

    @property
    def port(self):
        return self._port

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        self._state = Fan.states[int(val)]

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, input):
        val = int (input, 16 )
        if val == 255:
            val = 3
        self._speed = Fan.speeds[val]
        
    @property
    def boost_status(self):
        return self._boost_status

    @boost_status.setter
    def boost_status(self, input):
        val = int (input, 16 )
        self._boost_status = Fan.statuses[val]

    @property
    def timer_mode(self):
        return self._timer_mode

    @timer_mode.setter
    def timer_mode(self, input):
        val = int (input, 16 )
        self._timer_mode = Fan.timer_modes[val]

    @property
    def humidity_sensor_state(self):
        return self._humidity_sensor_state

    @humidity_sensor_state.setter
    def humidity_sensor_state(self, input):
        val = int (input, 16 )
        self._humidity_sensor_state = Fan.states[val]

    @property
    def relay_sensor_state(self):
        return self._relay_sensor_state

    @relay_sensor_state.setter
    def relay_sensor_state(self, input):
        val = int (input, 16 )
        self._relay_sensor_state = Fan.states[val]

    @property
    def analogV_sensor_state(self):
        return self._analogV_sensor_state

    @analogV_sensor_state.setter
    def analogV_sensor_state(self, input):
        val = int (input, 16 )
        self._analogV_sensor_state = Fan.states[val]

    @property
    def humidity_treshold (self):
        return self._humidity_treshold

    @humidity_treshold.setter
    def humidity_treshold(self, input):
        val = int (input, 16 )
        self._humidity_treshold = str( val ) + " %"
        
    @property
    def battery_voltage (self):
        return self._battery_voltage

    @battery_voltage.setter
    def battery_voltage(self, input):
        val = int.from_bytes(int(input,16).to_bytes(2,'big'), byteorder='little', signed=False)
        self._battery_voltage = str( val ) + " mV"        

    @property
    def humidity (self):
        return self._humidity

    @humidity.setter
    def humidity(self, input):
        val = int (input, 16 )
        self._humidity = str( val ) + " %"

    @property
    def analogV (self):
        return self._analogV

    @analogV.setter
    def analogV(self, input):
        val = int (input, 16 )
        self._analogV = str( val )

    @property
    def relay_status (self):
        return self._relay_status

    @relay_status.setter
    def relay_status(self, input):
        val = int (input, 16 )
        self._relay_status = Fan.statuses[val]

    @property
    def man_speed(self):
        return self._man_speed

    @man_speed.setter
    def man_speed(self, input ):
        val =  int(input,16)
        self._man_speed = str(int( val / 255 * 100)) + " %"
        
    @property
    def fan1_speed(self):
        return self._fan1_speed

    @fan1_speed.setter
    def fan1_speed(self, input ):
        val = int.from_bytes(int(input,16).to_bytes(2,'big'), byteorder='little', signed=False)
        self._fan1_speed = str ( val ) + " rpm" 
        
    @property
    def fan2_speed(self):
        return self._fan2_speed

    @fan2_speed.setter
    def fan2_speed(self, input ):
        val = int.from_bytes(int(input,16).to_bytes(2,'big'), byteorder='little', signed=False)
        self._fan2_speed = str ( val ) + " rpm" 

    @property
    def filter_timer_countdown(self):
        return self._filter_timer_countdown

    @filter_timer_countdown.setter
    def filter_timer_countdown(self, input ):
        val = int(input,16).to_bytes(3,'big')
        
        self._filter_timer_countdown = str ( val[2] ) + "d " +str ( val[1] ) + "h " + str ( val[0] ) + "m " 

    @property
    def boost_time (self):
        return self._boost_time

    @boost_time.setter
    def boost_time(self, input):
        val = int (input, 16 )
        self._boost_time = str( val ) + " m"

    @property
    def rtc_time(self):
        return self._rtc_time

    @rtc_time.setter
    def rtc_time(self, input ):
        val = int(input,16).to_bytes(3,'big')
        
        self._rtc_time = str ( val[2] ) + "h " +str ( val[1] ) + "m " + str ( val[0] ) + "s " 

    @property
    def rtc_date(self):
        return self._rtc_date

    @rtc_date.setter
    def rtc_date(self, input ):
        val = int(input,16).to_bytes(4,'big')
        self._rtc_date = str ( val[1] ) + " 20" + str ( val[3] ) + "-" +str ( val[2] ).zfill(2 ) + "-" + str( val[0] ).zfill(2 )

    @property
    def weekly_schedule_state(self):
        return self._weekly_schedule_state

    @weekly_schedule_state.setter
    def weekly_schedule_state(self, val):
        self._weekly_schedule_state = Fan.states[int(val)]

    @property
    def device_search(self):
        return self._device_search

    @device_search.setter
    def device_search(self, val):
        self._device_search = self.hex2str(val)
        
    @property
    def device_password(self):
        return self._device_password

    @device_password.setter
    def device_password(self, val):
        self._device_password = self.hex2str(val)        

    @property
    def machine_hours(self):
        return self._machine_hours

    @machine_hours.setter
    def machine_hours(self, input ):
        val = int(input,16).to_bytes(4,'big')
        self._machine_hours = str ( int.from_bytes(val[2:3],'big') ) + "d " + str ( val[1] ) + "h " +str ( val[0] ) + "m "

    @property
    def alarm_status (self):
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, input):
        val = int (input, 16 )
        self._alarm_status = Fan.alarms[val]

    @property
    def cloud_server_state (self):
        return self._cloud_server_state

    @cloud_server_state.setter
    def cloud_server_state(self, input):
        val = int (input, 16 )
        self._cloud_server_state = Fan.states[val]

    @property
    def firmware (self):
        return self._firmware

    @firmware.setter
    def firmware(self, input):
        val = int(input,16).to_bytes(6,'big')
        self._firmware = str(val[0]) + '.' + str(val[1]) + " " + str(int.from_bytes(val[4:6], byteorder='little', signed=False)) + "-" + str ( val[3] ).zfill(2) + "-" +str ( val[2] ).zfill(2)

    @property
    def filter_replacement_status (self):
        return self._filter_replacement_status

    @filter_replacement_status.setter
    def filter_replacement_status(self, input):
        val = int (input, 16 )
        self._filter_replacement_status = Fan.statuses[val]

    @property
    def wifi_operation_mode (self):
        return self._wifi_operation_mode

    @wifi_operation_mode.setter
    def wifi_operation_mode(self, input):
        val = int (input, 16 ) 
        self._wifi_operation_mode = Fan.wifi_operation_modes[val]

    @property
    def wifi_name (self):
        return self._wifi_name

    @wifi_name.setter
    def wifi_name(self, input):
        self._wifi_name = self.hex2str(input)

    @property
    def wifi_pasword (self):
        return self._wifi_pasword

    @wifi_pasword.setter
    def wifi_pasword(self, input):
        self._wifi_pasword = self.hex2str(input)
        
    @property
    def wifi_enc_type (self):
        return self._wifi_enc_type

    @wifi_enc_type.setter
    def wifi_enc_type(self, input):
        val = int (input, 16 )
        self._wifi_enc_type = Fan.wifi_enc_types[val]        
        
    @property
    def wifi_freq_chnnel (self):
        return self._wifi_freq_chnnel

    @wifi_freq_chnnel.setter
    def wifi_freq_chnnel(self, input):
        val = int (input, 16 )
        self._wifi_freq_chnnel = val                

    @property
    def wifi_dhcp (self):
        return self._wifi_dhcp

    @wifi_dhcp.setter
    def wifi_dhcp(self, input):
        val = int (input, 16 )
        self._wifi_dhcp = Fan.wifi_dhcps[val]

    @property
    def wifi_assigned_ip (self):
        return self._wifi_assigned_ip

    @wifi_assigned_ip.setter
    def wifi_assigned_ip(self, input):
        val = int(input,16).to_bytes(4,'big')
        self._wifi_assigned_ip = str(val[0]) + '.' + str(val[1]) + "." + str(val[2]) + "." + str ( val[3] )

    @property
    def wifi_assigned_netmask (self):
        return self._wifi_assigned_netmask

    @wifi_assigned_netmask.setter
    def wifi_assigned_netmask(self, input):
        val = int(input,16).to_bytes(4,'big')
        self._wifi_assigned_netmask = str(val[0]) + '.' + str(val[1]) + "." + str(val[2]) + "." + str ( val[3] )

    @property
    def wifi_main_gateway (self):
        return self._wifi_main_gateway

    @wifi_main_gateway.setter
    def wifi_main_gateway(self, input):
        val = int(input,16).to_bytes(4,'big')
        self._wifi_main_gateway = str(val[0]) + '.' + str(val[1]) + "." + str(val[2]) + "." + str ( val[3] )

    @property
    def curent_wifi_ip (self):
        return self._curent_wifi_ip

    @curent_wifi_ip.setter
    def curent_wifi_ip(self, input):
        val = int(input,16).to_bytes(4,'big')
        self._curent_wifi_ip = str(val[0]) + '.' + str(val[1]) + "." + str(val[2]) + "." + str ( val[3] )

    @property
    def airflow(self):
        return self._airflow

    @airflow.setter
    def airflow(self, input ):
        val = int (input, 16 )
        self._airflow = Fan.airflows[val]

    @property
    def analogV_treshold (self):
        return self._analogV_treshold

    @analogV_treshold.setter
    def analogV_treshold(self, input):
        val = int(input,16)
        self._analogV_treshold = (str(int(val/255*100))) + ' %'
        
    @property
    def unit_type (self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, input):
        val = int (input, 16 )
        self._unit_type = Fan.unit_types[val]        

    @property
    def night_mode_timer (self):
        return self._night_mode_timer

    @night_mode_timer.setter
    def night_mode_timer(self, input):
        val = int(input,16).to_bytes(2,'big')
        self._night_mode_timer = str(val[1]).zfill(2) + "h " + str(val[0]).zfill(2) + "m"

    @property
    def party_mode_timer (self):
        return self._party_mode_timer

    @party_mode_timer.setter
    def party_mode_timer(self, input):
        val = int(input,16).to_bytes(2,'big')
        self._party_mode_timer = str(val[1]).zfill(2) + "h " + str(val[0]).zfill(2) + "m"

    @property
    def humidity_status (self):
        return self._humidity_status

    @humidity_status.setter
    def humidity_status(self, input):
        val = int (input, 16 )
        self._humidity_status = Fan.statuses[val]

    @property
    def analogV_status (self):
        return self._analogV_status

    @analogV_status.setter
    def analogV_status(self, input):
        val = int (input, 16 )
        self._analogV_status = Fan.statuses[val]

