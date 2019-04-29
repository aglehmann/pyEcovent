# pyEcovent

Python3 library for single-room energy recovery ventilators from Vents / Blauberg / Flexit

## Install
	pip3 install pyEcovent

## Example usage
	from pyEcovent.ecovent import Fan

	""" Create a new fan with IP Address """
	fan=Fan("192.168.0.22")

	""" Update the current values of the fan """
	fan.update()


	""" Print the current set values """
	print(fan.state)
	print(fan.speed)
	print(fan.man_speed)
	print(fan.airflow)

	""" Set speed to medium """
	fan.set_speed(2)
	print(fan.speed)

	""" Toggle fan state """
	fan.set_state()
	print(fan.state)

	""" Set manual speed to 123 """
	fan.set_man_speed(123)
	print(fan.man_speed)

	""" Set airflow to 'Air Supply' """
	fan.set_airflow(1)
	print(fan.airflow)

## Intended usage
The intended usage of this library is to include ventilation fans from Vents / Blauberg / Flexit in <https://www.home-assistant.io/>

## Tested fans 
This library has only been tested on [Twinfresh Expert RW1-50](http://vents-us.com/item/5262/VENTS_TwinFresh_Expert_RW1-50-2_Wi-Fi/)

There are fans from Blauberg and Flexit that are identical and should work, but I have not verified that.
- [Single room ventilator Roomie Dual](https://www.flexit.no/en/products/single_room_ventilator/single_room_ventilator_roomie_dual/single_room_ventilator_roomie_dual/)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)
