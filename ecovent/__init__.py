""" __init__.py """
""" Version  """
__version__ = "0.8.1"

"""Library to handle communication with Wifi ecofan from TwinFresh / Blauberg"""
import socket
import sys


class Fan(object):
    """Class to communicate with the ecofan"""
    HEADER = bytes.fromhex('6D6F62696C65')
    FOOTER = bytes.fromhex('0D0A')

    def __init__(self, host, port=4000):
        self._host = host
        self._port = port
        self._fan_state = None
        self._fan_speed = None
        self._fan_man_speed = None
        self._fan_airflow = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(15)
        self.socket.connect((self._host, self._port))
        return self.socket

    def send(self, data):
        self.socket = self.connect()
        return self.socket.send(Fan.HEADER + data + Fan.FOOTER)

    def receive(self):
        return self.socket.recv(98)

    def update(self):
        self.send(bytes.fromhex('0100'))
        response = self.receive()
        self.parse_response(response[6:])
        self.socket.close()

    def set_state_on(self):
        if self.state == 'unknown':
            self.update()

        if self.state ==  'off':
            cmd = bytes.fromhex('0300')
            self.send(cmd)
            self.socket.close()
        else:
           print("No action required")

        self.update()

    def set_state_off(self):
        if self.state == 'unknown':
            self.update()

        if self.state ==  'on':
            cmd = bytes.fromhex('0300')
            self.send(cmd)
            self.socket.close()
        else:
           print("No action required")

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

    def parse_response(self, data):
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
    def port(self):
        return selv._port

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
