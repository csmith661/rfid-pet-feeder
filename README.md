# rfid-pet-feeder
Raspberry Pi Pico; MFRC522 RFID; PWM Servos; Actuates a lid for a pet feeder based on the RFID tag implanted in the pet or attached to the pet's collar(best result)


Hardware: 
 Raspberry Pi Pico
 mfrc522 RFID Reader
 RFID Chip 13.56mhz
 2x Servo Motors (MG90S 9g Metal Gear Digital Micro Servo)
 Green LED
 Red LED
 
 Module for MFRC522 courtesy of https://github.com/danjperron/micropython-mfrc522
 
 
 Pin Locations:
  Green LED Pin 15
  Red LED Pin 15
  Right Servo Pin 13
  Left Servo Pin 12
  
  MFRC:
    SPI Pin 0
    SCK Pin 2
    MISO Pin 4
    MOSI Pin 3
    CS Pin 1
    rst null
 
 
 //Schematic will be inlcuded in future repository
 
 //Configure custom Pin locations in main.py
 
 //Configure white_list RFID ID numbers in main.py
 
 //Lid movement can be adjusted in setup of main.py **note that increasing the value of lid_speed increases the downtime between movements, so increasing value slows down the speed**
 
 //3D designs ready for 3d printer will be included in future respository as well
  
