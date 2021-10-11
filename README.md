# pyEcoventV2

Python3 library for single-room energy recovery ventilators with api V2 from Vents / Blauberg / Flexit

## Install
	pip3 install pyEcoventV2

## Example usage
	from ecoventv2 import Fan
	""" Create a new fan with IP Address """
	""" The Fan object takes 'host', 'name', 'port' as arguments """
	""" 'host' (IP address) is mandatory argument """
	""" 'fan_id' (ID from label on fan) is mandatory argument """
	""" 'password' is optional and will default to 1111 """
	""" 'name' is optional and will default to ecofanv2 """ 
	""" 'port' is also optional and will default to 4000 """"
	fan=Fan("192.168.0.22","003A00345842570A")
	
	""" Optinally create a Fan with a name  
	fan=Fan("192.168.0.22", "003A00345842570A", "1111", "Cellar Fan")

	""" Update the current values of the fan """
	fan.update()


	""" Print the current configured values """
	print(fan.state)
	print(fan.speed)
	print(fan.man_speed)
	print(fan.airflow)
	print(fan.humidity)

	""" Set speed to medium (low=1 / medium=2 / high=3) """
	fan.set_speed(2)
	print(fan.speed)

	""" Set fan state to off/on """
	fan.set_state_off()
	fan.set_state_on()

	""" Set manual speed to 123 (valid values 22 -> 255) """
	fan.set_man_speed(123)
	print(fan.man_speed)

	""" Set airflow to 'Air Supply' (ventilation=0 / heat recovery=1 / air supply=2)"""
	fan.set_airflow(2)
	print(fan.airflow)

	""" Generaly set any suported parameter
	fan.set_param('timer_mode','night')

	""" Supported parameters
	'state', 'speed', 'boost_status', 'timer_mode', 'timer_counter'
	'humidity_sensor_state', 'relay_sensor_state', 'analogV_sensor_state'
	'humidity_treshold', 'battery_voltage', 'humidity', 'analogV'
	'relay_status', 'man_speed', 'fan1_speed', 'fan2_speed',
	'filter_timer_countdown', 'boost_time', 'rtc_time', 'rtc_date',
	'weekly_schedule_state', 'weekly_schedule_setup', 'device_search',
	'device_password', 'machine_hours', 'alarm_status', 
	'cloud_server_state', 'firmware', 'filter_replacement_status',
	'wifi_operation_mode', 'wifi_name', 'wifi_pasword',
	'wifi_enc_type', 'wifi_freq_chnnel', 'wifi_dhcp', 'wifi_assigned_ip',
	'wifi_assigned_netmask', 'wifi_main_gateway', 'curent_wifi_ip',
	'airflow', 'analogV_treshold', 'unit_type', 'night_mode_timer',
	'party_mode_timer', 'humidity_status', 'analogV_status'

## Intended usage
The intended usage of this library is to include ventilation fans from Vents / Blauberg / Flexit
with api V2 in <https://www.home-assistant.io/>

## Tested fans 
This library has only been tested on the following fans:
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)
