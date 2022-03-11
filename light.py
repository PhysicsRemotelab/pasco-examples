from lib.pasco_ble_device import PASCOBLEDevice

my_sensor = PASCOBLEDevice()
found_devices = my_sensor.scan()

if not found_devices:
    print('No devices found')
    exit()

for _, ble_device in enumerate(found_devices):
    display_name = ble_device.name.split('>')
    print(f'{_}: {display_name[0]}')

ble_device = found_devices[int(0)]
my_sensor.connect(ble_device)

sensors = my_sensor.get_measurement_list()
print(sensors)
for sensor in sensors:
    result = my_sensor.read_data(sensor)
    print(sensor + ' - ' + str(result))

