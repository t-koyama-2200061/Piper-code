import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
dynamodb_key = 0

try:
    while True:
        result = instance.read()
        print("result:",vars(result))
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            
            # put DynamoDB
            os.system(f"/home/pi/DHT11_Python/put_dynamodb.sh {dynamodb_key} {result.humidity}")
            dynamodb_key += 1


        time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
