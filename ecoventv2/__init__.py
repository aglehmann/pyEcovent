""" __init__.py """
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
    prmt['relay_value'] = "0032"
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
    prmt['filter_replacement_state'] = "0088"
    prmt['wifi_operation_mode'] = "0094"
    prmt['wifi_name'] = "0095"
    prmt['wifi_pasword'] = "0096"
    prmt['wifi_enc_type'] = "0099"
    prmt['wifi_freq_chnnel'] = "009A"
    prmt['wifi_dhcp'] = "009B"
    prmt['wifi_assigned_ip'] = "009C"
    prmt['wifi_assigned_netmask'] = "009D"
    prmt['wifi_main_gateway'] = "009E"
    prmt['wifi_apply_adn_quit'] = "00A0"
    prmt['wifi_discard_adn_quit'] = "00A2"
    prmt['curent_wifi_ip'] = "00A3"
    prmt['airflow'] = "00B7"
    prmt['analogV_treshold'] = "00B8"
    prmt['unit_type'] = "00B9"
    prmt['night_mode_timer'] = "0302"
    prmt['party_mode_timer'] = "0303"
    prmt['party_mode_timer'] = "0303"
    prmt['humidity_status'] = "0304"
    prmt['analogV_status'] = "0305"

    states = dict()    
    states['OFF'] = "00"
    states['ON'] = "01"
    states['TOGLE'] = "02"

    speeds = dict()
    speeds['01'] = "low"
    speeds['02'] = "medium"
    speeds['03'] = "high"
    speeds['FF'] = "manual"

    status = dict()
    status['00'] = "off"
    status['01'] = "on"

    timer_mode = dict ()
    timer_mode['00'] = "off"
    timer_mode['01'] = "Night"
    timer_mode['02'] = "Party"
    
    alarms = dict ()
    alarms['00'] = "no"
    alarms['01'] = "alarm"
    alarms['02'] = "warning"
    
    airflows = dict ()
    airflows['00'] = "ventilation"
    airflows['01'] = "heat recovery"
    airflows['02'] = "supply"
    
    unit_types = dict ()
    unit_types['03'] = "Vento Expert A50-1/A85-1/A100-1 W V.2"
    unit_types['04'] = "Vento Expert Duo A30-1 W V.2"
    unit_types['05'] = "Vento Expert A30 W V.2"
    
    def __init__(self, host, fan_id="003A00345842570A", password="1111", name="ecofanv2", port=4000 ):
        self._name = name
        self._host = host
        self._port = port
        self._type = "02"
        self._fan_id_size = 10
        self._fan_id = fan_id
        self._pwd_size = 0
        self._password = password
#        self._fan_state = Fan.status[self.read_param(Fan.prmt['state'])]
#        self._fan_speed = Fan.speeds[self.read_param(Fan.prmt['speed'])]
#        self._fan_boost_status = Fan.status[self.read_param(Fan.prmt['boost_status'])]
#        self._fan_timer_mode = Fan.timer_mode[self.read_param(Fan.prmt['timer_mode'])]
#        self._fan_timer_counter = None
#        self._fan_humidity_sensor_state = Fan.status[self.read_param(Fan.prmt['humidity_sensor_state'])]
#        self._fan_relay_sensor_state = Fan.status[self.read_param(Fan.prmt['relay_sensor_state'])]
#        self._fan_analogV_sensor_state = Fan.status[self.read_param(Fan.prmt['analogV_sensor_state'])]
#        self._fan_humidity_treshold = int(self.read_param(Fan.prmt['humidity_treshold']),16)
#        self._fan_battery_voltage = None # int(self.read_param(Fan.prmt['battery_voltage']),16)
#        self._fan_humidity = int(self.read_param(Fan.prmt['humidity']),16)
#        self._fan_analogV = int(self.read_param(Fan.prmt['analogV']),16)
#        self._fan_relay_value = Fan.status[self.read_param(Fan.prmt['relay_value'])]
#        self._fan_man_speed = int(int(self.read_param(Fan.prmt['man_speed']),16)/255*100)
#        self._fan_fan1_speed = None
#        self._fan_fan2_speed = None
#        self._fan_filter_timer_countdown = None
#        self._fan_boost_time = int(self.read_param(Fan.prmt['boost_time']),16)
#        self._fan_rtc_time = None
#        self._fan_rtc_date = None
#        self._fan_weekly_schedule_state = Fan.status[self.read_param(Fan.prmt['weekly_schedule_state'])]
#        self._fan_schedule_setup = None
#        self._fan_machine_hours = None
#        self._fan_alarm_state = Fan.alarms[self.read_param(Fan.prmt['alarm_state'])]
#        self._fan_cloud_server_state = Fan.status[self.read_param(Fan.prmt['cloud_server_state'])]
#        self._fan_firmware = None
#        self._fan_filter_replacement_state = Fan.status[self.read_param(Fan.prmt['filter_replacement_state'])]
#        self._fan_curent_wifi_ip = None
#        self._fan_airflow = Fan.airflows[self.read_param(Fan.prmt['airflow'])]
#        self._fan_analogV_treshold = int(int(self.read_param(Fan.prmt['analogV_treshold']),16)/255*100)
#        self._fan_unit_type = None # Fan.unit_types[self.read_param(Fan.prmt['unit_type'])]
#        self._fan_night_mode_timer = None 
#        self._fan_party_mode_timer = None
#        self._fan_humidity_status = None # Fan.status[self.read_param(Fan.prmt['humidity_status'])]
#        self._fan_analogV_status = None # Fan.status[self.read_param(Fan.prmt['analogV_status'])]

        # self.update_all()
        # self.read_param('000B')

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(4)
        self.socket.connect((self._host, self._port))
        return self.socket

    def str2hex(self,str_msg):
        return "".join("{:02x}".format(ord(c)) for c in str_msg)

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
        fan_id_size = self.get_size(self._fan_id)
        pwd_size = self.get_size (self._password)
        fan_id = self.str2hex(self._fan_id)
        password = self.str2hex(self._password)
        str = f"{self._type}{fan_id_size}{fan_id}{pwd_size}{password}"
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
        print ( "input: " + str(input) )
        out = ""
        parameter = ""
        for i in range (0,len(input), 4):
            out = input[i:(i+4)] ;
            if out[:2] != "00":
                out = "ff" + out ;
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
        print ("Update all")
        data = Fan.func['read'] + Fan.prmt['state'] + Fan.prmt['speed'] + Fan.prmt['boost_status'] + Fan.prmt['timer_mode'] + Fan.prmt['timer_counter'] + Fan.prmt['humidity_sensor_state'] + Fan.prmt['relay_sensor_state']
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
        pointer = 20 ;
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
        print ("payload:" + str (payload.hex()))
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
                print ( response.hex() )
                response = bytearray()           

        parameter = data[pointer]
        pointer += 1
        payload = data[pointer:length]
#        print ( response.hex() )
        return payload.hex()
        

    def old_parse_response(self, data):
        fan_params = {
        0x03: [1, 'state', None],
        0x04: [1, 'speed', None],
        0x05: [1, 'manual_speed', None],
        0x06: [1, 'air_flow_direction', None],
        0x08: [1, 'humidity_level', None],
        0x09: [1, 'operation_mode', None],
        0x0B: [1, 'humidity_sensor_threshold', None],
        0x0C: [1, 'alarm_status', None],
        0x0D: [1, 'relay_sensor_status', None],
        0x0E: [3, 'party_or_night_mode_countdown', None],
        0x0F: [3, 'night_mode_timer', None],
        0x10: [3, 'party_mode_timer', None],
        0x11: [3, 'deactivation_timer', None],
        0x12: [1, 'filter_eol_timer', None],
        0x13: [1, 'humidity_sensor_status', None],
        0x14: [1, 'boost_mode', None],
        0x15: [1, 'humidity_sensor', None],
        0x16: [1, 'relay_sensor', None],
        0x17: [1, '10V_sensor', None],
        0x19: [1, '10V_sensor_threshold', None],
        0x1A: [1, '10V_sensor_status', None],
        0x1B: [32, 'slave_device_search', None],
        0x1C: [4, 'response_slave_search', None],
        0x1F: [1, 'cloud_activation', None],
        0x25: [1, '10V_sensor_current_status', None]
        }
        for pair in self.parsebytes(data, fan_params):
            if pair[0] == 3:
                self.state = pair[1][0]
            elif pair[0] == 4:
                self.speed = pair[1][0]
            elif pair[0] == 5:
                self.man_speed = pair[1][0]
            elif pair[0] == 6:
                self.airflow = pair[1][0]
            elif pair[0] == 8:
                self.humidity = pair[1][0]

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
    def fan_id(self):
        return self._fan_id

    @fan_id.setter
    def fan_id(self, id):
        self._fan_id = id
        
    @property
    def fan_password(self):
        return self._fan_password

    @fan_password.setter
    def fan_password(self, pwd):
        self._fan_password = pwd        

    @property
    def port(self):
        return self._port

    @property
    def state(self):
        return self._fan_state

    @state.setter
    def state(self, val):
        if val == 0:
            self._fan_state = "off"
        elif val == 1:
            self._fan_state = "on"
        else:
            self._fan_state = "unknown"

    @property
    def speed(self):
        return self._fan_speed

    @speed.setter
    def speed(self, val):
        if val == 1:
            self._fan_speed = "low"
        elif val == 2:
            self._fan_speed = "medium"
        elif val == 3:
            self._fan_speed = "high"
        elif val == 4:
            self._fan_speed = "manual"
        else:
            self._fan_speed = "unknown"

    @property
    def man_speed(self):
        return self._fan_man_speed

    @man_speed.setter
    def man_speed(self, val):
        if val >= 22 and val <= 255:
            self._fan_man_speed = val
        else:
            self._fan_man_speed = 0

    @property
    def airflow(self):
        return self._fan_airflow

    @airflow.setter
    def airflow(self, val):
        if val == 0:
            self._fan_airflow = "ventilation"
        elif val == 1:
            self._fan_airflow = "heat recovery"
        elif val == 2:
            self._fan_airflow = "air supply"
        else:
            self._fan_airflow = "unknown"

    @property
    def humidity(self):
        return self._fan_humidity

    @humidity.setter
    def humidity(self, val):
        if val >= 40 and val <= 80:
            self._fan_humidity = val
        else:
            self._fan_humidity = None

