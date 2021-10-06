from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")

request = fan.prmt['state']
request += fan.prmt['speed']
request += fan.prmt['boost_status']
request += fan.prmt['boost_status']
request += fan.prmt['timer_mode']
request += fan.prmt['timer_counter']
request += fan.prmt['humidity_sensor_state']
request += fan.prmt['relay_sensor_state']
request += fan.prmt['analogV_sensor_state']
request += fan.prmt['humidity_treshold']
request += fan.prmt['battery_voltage']
request += fan.prmt['humidity']
request += fan.prmt['analogV']
request += fan.prmt['relay_value']
request += fan.prmt['man_speed']
request += fan.prmt['fan1_speed']
request += fan.prmt['fan2_speed']
request += fan.prmt['filter_timer_countdown']
# request += fan.prmt['filter_timer_reset']
request += fan.prmt['boost_time']
request += fan.prmt['rtc_time']
request += fan.prmt['rtc_date']
request += fan.prmt['weekly_schedule_state']
request += fan.prmt['weekly_schedule_setup']
request += fan.prmt['device_search']
request += fan.prmt['device_password']
request += fan.prmt['machine_hours']
# request += fan.prmt['reset_alarms']
request += fan.prmt['alarm_state']
request += fan.prmt['cloud_server_state']
request += fan.prmt['firmware']
request += fan.prmt['filter_replacement_state']
# request += fan.prmt['factory_reset']
request += fan.prmt['filter_replacement_state']
request += fan.prmt['wifi_operation_mode']
request += fan.prmt['wifi_name']
request += fan.prmt['wifi_pasword']
request += fan.prmt['wifi_enc_type']
request += fan.prmt['wifi_freq_chnnel']
request += fan.prmt['wifi_dhcp']
request += fan.prmt['wifi_assigned_ip']
request += fan.prmt['wifi_assigned_netmask']
request += fan.prmt['wifi_main_gateway']
# request += fan.prmt['wifi_apply_adn_quit']
# request += fan.prmt['wifi_discard_adn_quit']
request += fan.prmt['curent_wifi_ip']
request += fan.prmt['airflow']
request += fan.prmt['analogV_treshold']
request += fan.prmt['unit_type']
request += fan.prmt['night_mode_timer']
request += fan.prmt['party_mode_timer']
request += fan.prmt['party_mode_timer']
request += fan.prmt['humidity_status']
request += fan.prmt['analogV_status']

fan.read_param(request)
#fan.read_param("0001000200060007000B000F00140016001900240025002D00320044004A004B006400650066006F007000720077007C007D007E00830085008600880094009500960099009A009B009C009D009E00A300B700B800B90302030303040305")

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

