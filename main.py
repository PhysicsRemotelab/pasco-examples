from lib.pasco_ble_device import PASCOBLEDevice

my_sensor = PASCOBLEDevice()
found_devices = my_sensor.scan()

for _, ble_device in enumerate(found_devices):
    display_name = ble_device.name.split('>')
    print(f'{_}: {display_name[0]}')

ble_device = found_devices[int(0)]
my_sensor.connect(ble_device)

mes = my_sensor.get_measurement_list()
print(mes)
voltage = my_sensor.read_data('Voltage')
print(voltage)