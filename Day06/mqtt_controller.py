from threading import Thread, Timer
import  time
import json
import datetime as dt

import paho.mqtt.client as mqtt
import Adafruit_DHT as dht

sensor = dht.DHT22
rcv_pin = 10 


class publisher(Thread):
        def __init__(self):
                Thread.__init__(self)
                self.host = '210.119.12.84'
                self.port = 1883
                self.clientId = 'IOT84'
                print('publisher 스레드 시작')
                self.client = mqtt.Client(client_id=self.clientId)

        def run(self):
                self.client.connect(self.host, self.port)
                self.publish_data_auto()

        def publish_data_auto(self):
                humid, temp = dht.read_retry(sensor, rcv_pin)
                curr = dt.datetime.now().strftime('%Y-%m-%d %H: %M: %S') 
                origin_data = {'DEV_ID' : self.clientId, 'CURR_DT' : curr, 'TYPE' : 'TEMPHUMID', 
                               
                            'STAT' : f'{temp} | {humid}'}
                pub_data = json.dumps(origin_data)
                self.client.publish(topic='pknu/rpi/control/', payload=pub_data)
                print('Data published') 
                Timer(2.0, self.publish_data_auto).start() 

class subscriber(Thread):
        def __init__(self) : #생성자
                Thread.__init__(self)
                self.host =  '210.119.12.84'
                self.port = 1883
                self.clientId = 'IOT84_SUB'
                self.topic = 'pknu/monitor/control/'
                print('subscriber 스레드  시작')


if __name__ == '__main__':
        thPub = publisher() # 객체 생성
        thPub.start() #run 자동실행      
                
