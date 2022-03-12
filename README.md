# pyEcoventV2

Python3 library for single-room energy recovery ventilators from Vents / Blauberg / Flexit

## Install
	pip3 install pyEcoventV2

## Example usage
	from ecovent import Fan
	""" Create a new fan with IP Address """
	""" The Fan object takes 'host', 'name', 'port' as arguments """
	""" 'host' (IP address) is the only mandatory argument """
	""" 'name' is optional and will default to ecofan """
	""" 'port' is also optional and will default to 4000 """"
	fan=Fan("192.168.0.22")
	
	""" Optinally create a Fan with a name  
	fan=Fan("192.168.0.22", "Cellar Fan")

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

## Intended usage
The intended usage of this library is to include ventilation fans from Vents / Blauberg / Flexit in <https://www.home-assistant.io/>

## Tested fans 
This library has only been tested on the following fans:
- [Twinfresh Expert RW1-50](http://vents-us.com/item/5262/VENTS_TwinFresh_Expert_RW1-50-2_Wi-Fi/)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)
- [Blauberg VENTO EXPERT DUO A30-1 W](https://blaubergventilatoren.de/en/series/vento-expert-duo-a30-1-s10-w-v2)

Fans from Flexit are identical and should work, but this is not yet tested:
- [Single room ventilator Roomie Dual](https://www.flexit.no/en/products/single_room_ventilator/single_room_ventilator_roomie_dual/single_room_ventilator_roomie_dual/)


## Changelog
- v 0.9.9.
-- initialize _battery_voltage with 0 not None
