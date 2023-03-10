from time import sleep



def setLid(intended_status, right_servo, left_servo, lid_open, lid_closed, lid_speed, lid_increment):
    
    def threshold (percent):
        return (lid_open - lid_closed) * percent + lid_closed
    
    if intended_status == 'closed':
        
        right_position = right_servo.duty_u16()
        left_position = left_servo.duty_u16()
        
        while right_position > lid_closed:
            
            right_servo.duty_u16(right_position)
            left_servo.duty_u16(left_position)
            right_position -= lid_increment
            left_position += lid_increment
            

            if(right_position > threshold(0.1)):
                sleep(lid_speed)
            if(right_position <= threshold(0.1) and right_position > threshold(0.05)):
                sleep(lid_speed*2)
            if(right_position <= threshold(0.5)):
                sleep(lid_speed*4)
            
    if intended_status == 'open':
        
        right_position = right_servo.duty_u16()
        left_position = left_servo.duty_u16()
        
        while right_position < lid_open:
            
            right_servo.duty_u16(right_position)
            left_servo.duty_u16(left_position)
            
            right_position += lid_increment
            left_position -= lid_increment
            
            if(right_position > threshold(0.1)):
                sleep(lid_speed)
            if(right_position <= threshold(0.5)):
                sleep(lid_speed*4)