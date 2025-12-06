from machine import Pin, I2C, RTC
import network, time
import esp32
import onewire, ds18x20

print(esp32.mcu_temperature())

rtc = RTC()
print(rtc.datetime())

# wlan = network.WLAN()
# wlan.active(True)
# print(wlan.scan())

ds_pin = Pin(3)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
serialByteArray = ds_sensor.scan()
print(serialByteArray)
i = 0
while (i < 30):
    ds_sensor.convert_temp()            
    time.sleep_ms(1000)
    for UID in serialByteArray:
        temp_value = ds_sensor.read_temp(UID)
        print(temp_value)
    i += 1
