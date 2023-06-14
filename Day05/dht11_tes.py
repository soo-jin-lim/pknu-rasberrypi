import Adafruit_DHT as dht
import time
sensor = dht.DHT22
rcv_pin = 10

try:
    while True:
            humid, temp = dht.read_retry(sensor, rcv_pin)
            if humid is not None and temp is not None:
                print(f'온도: {temp}c / 습도: {humid}%')
            else:
                 print('센싱에러')
            time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    print('프로그램 종료')

