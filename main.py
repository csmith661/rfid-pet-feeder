from machine import Pin, PWM
from mfrc522 import MFRC522
from lidmovement import setLid
import utime

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

#Array of Accepted RFID cards
white_list = [649377408, 359787737]

green_led = Pin(15, Pin.OUT)
red_led = Pin(14, Pin.OUT)

#Lid movement Configuration

lid_closed = 4000
lid_open = 9000
lid_increment = 50
lid_speed = 0.01

#Servo Motors Configuration

right_servo = PWM(Pin(13))
right_servo.freq(50)
right_servo.duty_u16(5000)

left_servo = PWM(Pin(12))
left_servo.freq(50)
left_servo.duty_u16(5000)


    

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    
    
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        
        if stat == reader.OK:
            
            #turn card into readable number
            card = int.from_bytes(bytes(uid),"little",False)
            
            
            #check if card is in white list, then sets the opening of the lids
            if card in white_list:
                green_led.value(1)
                red_led.value(0)
                setLid('open', right_servo, left_servo, lid_open, lid_closed, lid_speed, lid_increment)
                print('opened')
                utime.sleep_ms(5000)
                
    else:
        red_led.value(1)
        green_led.value(0)
        setLid('closed', right_servo, left_servo, lid_open, lid_closed, lid_speed, lid_increment)
                