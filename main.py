from machine import Pin, PWM
import time
import random

passiveBuzzer = PWM(Pin(21))

button = Pin(14, Pin.IN, Pin.PULL_UP) # The button value is 1

magnetic_button_stage_1 = Pin(13, Pin.IN, Pin.PULL_UP) # The value of magnetic_button_stage_1 is 1
magnetic_button_stage_2 = Pin(12, Pin.IN, Pin.PULL_UP) # The value of magnetic_button_stage_2 is 1
end_stage = Pin(15, Pin.IN, Pin.PULL_UP)

led1 = Pin(1, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)
led4 = Pin(6, Pin.OUT)
led5 = Pin(7, Pin.OUT)
led6 = Pin(8, Pin.OUT)
player_1_led = Pin(9, Pin.OUT)
player_2_led = Pin(10, Pin.OUT)
button_led = Pin(11, Pin.OUT)

# Reset
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)

passiveBuzzer.duty(0)

Switch = True

player_1_led.value(0)
player_2_led.value(0)
button_led(0)
# Reset

volume = 200	# fallið duty er notað til að stilla styrkinn (spennu) á merkinu, 0 til 1023. Skrifar út hér 3.3V

led_time = 100
led_time_slow = 500

player_1_turn = True
player_2_turn = False

player_1_turn_end = False
player_2_turn_end = False

player_1_gas = 12
player_2_gas = 12

player_1_stage_1 = False
player_1_stage_2 = False

player_2_stage_1 = False
player_2_stage_2 = False

player_1_finish = False
player_2_finish = False

# Music
def playdraw():
    volume = 200
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(100)
    player_1_led.value(1)
    player_2_led.value(1)
    time.sleep_ms(800)
    passiveBuzzer.duty(0)
    player_1_led.value(0)
    player_2_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(100)
    player_1_led.value(1)
    player_2_led.value(1)
    time.sleep_ms(800)
    passiveBuzzer.duty(0)
    player_1_led.value(0)
    player_2_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(200)
    player_1_led.value(1)
    player_2_led.value(1)
    time.sleep_ms(400)
    passiveBuzzer.freq(400)
    player_1_led.value(0)
    player_2_led.value(0)
    time.sleep_ms(400)
    passiveBuzzer.freq(200)
    player_1_led.value(1)
    player_2_led.value(1)
    time.sleep_ms(400)
    passiveBuzzer.duty(0)
    

def playfinish(player_led):
    volume = 200
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(800)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(700)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(800)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(700)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(180)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(600)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(160)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(500)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(160)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(800)
    player_led.value(1)
    time.sleep_ms(200)
    player_led.value(0)
    passiveBuzzer.duty(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(0)
    
    
def playwin(player_led):
    volume = 200
    
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(1700)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(600)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(1000)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(1700)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(100)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(100)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    player_led.value(0)
    time.sleep_ms(200)
    
    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(100)
    player_led.value(1)
    time.sleep_ms(200)
    passiveBuzzer.duty(0)
    time.sleep_ms(200)
    
    
    passiveBuzzer.duty(0)

def playgasup(player_led):
    volume = 200

    player_led.value(0)
    time.sleep_ms(125)

    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(1500)
    player_led.value(1)
    time.sleep_ms(125)
    passiveBuzzer.duty(0)

    player_led.value(0)
    time.sleep_ms(125)

    passiveBuzzer.duty(volume)
    passiveBuzzer.freq(1500)
    player_led.value(1)
    time.sleep_ms(125)
    passiveBuzzer.duty(0)
    passiveBuzzer.duty(0)
# Music


# Start up
passiveBuzzer.init()
passiveBuzzer.duty(volume)
passiveBuzzer.freq(100)
led1.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(300)
led2.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(500)
led3.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(700)
led4.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(900)
led5.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(1100)
led6.value(1)
time.sleep_ms(500)
passiveBuzzer.duty(0)
time.sleep_ms(200)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
time.sleep_ms(300)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(1500)
led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)
led5.value(1)
led6.value(1)
time.sleep_ms(125)
passiveBuzzer.duty(0)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
time.sleep_ms(125)

passiveBuzzer.duty(volume)
passiveBuzzer.freq(1500)
led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)
led5.value(1)
led6.value(1)
time.sleep_ms(125)
passiveBuzzer.duty(0)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
time.sleep_ms(1000)

passiveBuzzer.duty(0)

# Start up

player_1_led.value(1)
player_2_led.value(0)

print("Program has started!")
while True:
    while Switch == False:
        button_led(1)
        if not button.value():
            player_1_turn = True
            player_2_turn = False

            player_1_turn_end = False
            player_2_turn_end = False

            player_1_gas = 12
            player_2_gas = 12

            player_1_stage_1 = False
            player_1_stage_2 = False

            player_2_stage_1 = False
            player_2_stage_2 = False

            player_1_finish = False
            player_2_finish = False
            
            # Reset
            led1.value(0)
            led2.value(0)
            led3.value(0)
            led4.value(0)
            led5.value(0)
            led6.value(0)

            passiveBuzzer.duty(0)

            player_1_led.value(0)
            player_2_led.value(0)
            # Reset
            Switch = True
            button_led(0)
            
            passiveBuzzer.duty(volume)
            passiveBuzzer.freq(1500)
            time.sleep_ms(200)
            passiveBuzzer.duty(0)
            time.sleep_ms(3000)
            player_1_led.value(1)
            player_2_led.value(0)
            print("Restarted")
    while Switch == True:
        button_led(1)
        # Magnetic Button
        if not magnetic_button_stage_1.value(): # Magnetic_button_stage_1 value is 0: Execute code
            if player_1_stage_1 == False:
                if player_1_finish == False:
                    if player_1_turn_end == True:
                        button_led(0)
                        print('Player 1: Stage 1 Activated')
                        player_1_gas += 1
                        player_1_stage_1 = True
                        print(f"Gas: {player_1_gas}")
                        player_2_led.value(0)
                        playgasup(player_1_led)
                
            if player_2_stage_1 == False:
                if player_2_finish == False:
                    if player_2_turn_end == True:
                        button_led(0)
                        print('Player 2: Stage 1 Activated')
                        player_2_gas += 1
                        player_2_stage_1 = True
                        print(f"Gas: {player_2_gas}")
                        player_1_led.value(0)
                        playgasup(player_2_led)

        if not magnetic_button_stage_2.value(): # Magnetic_button_stage_2 value is 0: Execute code
            if player_1_stage_2 == False:
                if player_1_finish == False:
                    if player_1_turn_end == True:
                        button_led(0)
                        print('Player 1: Stage 2 Activated')
                        player_1_gas += 1
                        player_1_stage_2 = True
                        print(f"Gas: {player_1_gas}")
                        player_2_led.value(0)
                        playgasup(player_1_led)
                        

            if player_2_stage_2 == False:
                if player_2_finish == False:
                    if player_2_turn_end == True:
                        button_led(0)
                        print('Player 2: Stage 2 Activated')
                        player_2_gas += 1
                        player_2_stage_2 = True
                        print(f"Gas: {player_2_gas}")
                        player_1_led.value(0)
                        playgasup(player_2_led)
        # Magnetic Button
        
        # Finish Line Button
        if not end_stage.value():
            if player_1_finish == False:
                if player_1_turn_end == True:
                    button_led(0)
                    player_1_final_gas = player_1_gas
                    print(f"Player 1 finished: {player_1_final_gas} gas remaining")
                    print()
                    player_1_finish = True
                    player_1_led.value(0)
                    player_2_led.value(0)
                    time.sleep_ms(100)
                    playfinish(player_1_led)
                    
            if player_2_finish == False:
                if player_2_turn_end == True:
                    button_led(0)
                    player_2_final_gas = player_2_gas
                    print(f"Player 2 finished: {player_2_final_gas} gas remaining")
                    print()
                    player_2_finish = True
                    player_1_led.value(0)
                    player_2_led.value(0)
                    time.sleep_ms(100)
                    playfinish(player_2_led)
        # Finish Line Button
        
        
        # The End of the Game
        if player_1_finish == True:
            if player_2_finish == True:
                if player_1_gas > player_2_gas:
                    button_led(0)
                    print(f"Player 1 wins: {player_1_gas} > {player_2_gas}")
                    button_led(0)
                    time.sleep(2)
                    # Reset
                    led1.value(0)
                    led2.value(0)
                    led3.value(0)
                    led4.value(0)
                    led5.value(0)
                    led6.value(0)
                    passiveBuzzer.duty(0)
                    player_1_led.value(0)
                    player_2_led.value(0)
                    # Reset
                    time.sleep(2)
                    playwin(player_1_led)
                    Switch = False
                    break
                if player_1_gas < player_2_gas:
                    button_led(0)
                    time.sleep(2)
                    print(f"Player 2 wins: {player_2_gas} > {player_1_gas}")
                    # Reset
                    led1.value(0)
                    led2.value(0)
                    led3.value(0)
                    led4.value(0)
                    led5.value(0)
                    led6.value(0)
                    passiveBuzzer.duty(0)
                    player_1_led.value(0)
                    player_2_led.value(0)
                    # Reset
                    time.sleep(2)
                    playwin(player_2_led)
                    Switch = False
                    break
                if player_1_gas == player_2_gas:
                    print(f"Draw: {player_1_gas} == {player_2_gas}")
                    button_led(0)
                    time.sleep(2)
                    # Reset
                    led1.value(0)
                    led2.value(0)
                    led3.value(0)
                    led4.value(0)
                    led5.value(0)
                    led6.value(0)
                    passiveBuzzer.duty(0)
                    player_1_led.value(0)
                    player_2_led.value(0)
                    # Reset
                    time.sleep(2)
                    playdraw()
                    Switch = False
                    break
        # The End of the Game
        
        
        # Will let the previous player move their charactar

        if player_1_finish == True:
            player_1_turn_end = False
            
        if player_2_finish == True:
            player_2_turn_end = False
            
        # Will let the previous player move their charactar


        # Player Led
        if player_1_turn == True:
            player_1_led.value(1)
            player_2_led.value(0)
        if player_2_turn == True:
            player_2_led.value(1)
            player_1_led.value(0)
        # Player Led
        
        if not button.value():       # hiddenButton value is 0: Execute code
            button_led(0)
            random_number = random.randint(1,6)
            if player_1_turn == True:
                player_1_gas -= 1
                print(f"Player 1 Rolled On: {random_number}")
                print(f"Gas: {player_1_gas}")
                print()
                player_1_turn = False
                player_2_turn = True
                
                player_1_turn_end = True
                player_2_turn_end = False
                
                if player_2_finish == True:
                    player_2_turn = False
                    player_1_turn = True
                
                
            else:
                if player_2_turn == True:
                    player_2_gas -= 1
                    print(f"Player 2 Rolled On: {random_number}")
                    print(f"Gas: {player_2_gas}")
                    print()
                    player_1_turn = True
                    player_2_turn = False
                    
                    player_2_turn_end = True
                    player_1_turn_end = False
                    
                    if player_1_finish == True:
                        player_1_turn = False
                        player_2_turn = True


            
            # Reset Pins
            led1.value(0)
            led2.value(0)
            led3.value(0)
            led4.value(0)
            led5.value(0)
            led6.value(0)
            # Reset Pins
            
            for i in range(4):
                player_1_led.value(0)
                player_2_led.value(0)
                
            # Led 1
                led1.value(1)
                
                passiveBuzzer.duty(volume)      # fallið duty er notað til að stilla styrkinn (spennu) á merkinu, 0 til 1023. Skrifar út hér 3.3V
                passiveBuzzer.freq(200)       # fallið freq er notað til að vinna með tíðni, nótur eru t.d. frá 31 til 4978
                
                time.sleep_ms(led_time)
                
                passiveBuzzer.duty(0)
                led1.value(0)
                time.sleep_ms(0)
            # Led 1


            # Led 2
                led2.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(400)
                
                time.sleep_ms(led_time)
                
                passiveBuzzer.duty(0)
                led2.value(0)
                time.sleep_ms(0)
            # Led 2


            # Led 3
                led3.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(600)
                
                time.sleep_ms(led_time)
                
                passiveBuzzer.duty(0)
                led3.value(0)
                time.sleep_ms(0)
            # Led 3


            # Led 4
                led4.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(800)
                
                time.sleep_ms(led_time)
                
                passiveBuzzer.duty(0)
                led4.value(0)
                time.sleep_ms(0)
            # Led 4


            # Led 5
                led5.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(1000)
                
                time.sleep_ms(led_time)
                
                passiveBuzzer.duty(0)
                led5.value(0)
                time.sleep_ms(0)
            # Led 5


            # Led 6
                led6.value(1)
                    
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(1200)
                
                time.sleep_ms(led_time) 
                
                passiveBuzzer.duty(0)
                led6.value(0)
                time.sleep_ms(0)
            # Led 6
                    
            for a in range(2):
                
            # Led 1
                led1.value(1)
                
                passiveBuzzer.duty(volume)      # fallið duty er notað til að stilla styrkinn (spennu) á merkinu, 0 til 1023. Skrifar út hér 3.3V
                passiveBuzzer.freq(200)       # fallið freq er notað til að vinna með tíðni, nótur eru t.d. frá 31 til 4978
                
                time.sleep_ms(led_time_slow)
                
                if a == 1:
                    if random_number == 1:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led1.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led1.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led1.value(0)
                        time.sleep_ms(100)
                        led1.value(1)
                        time.sleep_ms(1500)
                        break
                
                passiveBuzzer.duty(0)
                led1.value(0)
                time.sleep_ms(0)
            # Led 1


            # Led 2
                led2.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(400)
                
                time.sleep_ms(led_time_slow)
                
                if a == 1:
                    if random_number == 2:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led2.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led2.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led2.value(0)
                        time.sleep_ms(100)
                        led2.value(1)
                        time.sleep_ms(1500)
                        break
                
                passiveBuzzer.duty(0)
                led2.value(0)
                time.sleep_ms(0)
            # Led 2


            # Led 3
                led3.value(1)
                    
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(600)
                
                time.sleep_ms(led_time_slow)
                
                if a == 1:
                    if random_number == 3:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led3.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led3.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led3.value(0)
                        time.sleep_ms(100)
                        led3.value(1)
                        time.sleep_ms(1500)
                        break
                
                passiveBuzzer.duty(0)
                led3.value(0)
                time.sleep_ms(0)
            # Led 3


            # Led 4
                led4.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(800)
                
                time.sleep_ms(led_time_slow)
                
                if a == 1:
                    if random_number == 4:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led4.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led4.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led4.value(0)
                        time.sleep_ms(100)
                        led4.value(1)
                        time.sleep_ms(1500)
                        break
                
                passiveBuzzer.duty(0)
                led4.value(0)
                time.sleep_ms(0)
            # Led 4


            # Led 5
                led5.value(1)
                
                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(1000)
                
                time.sleep_ms(led_time_slow)
                if a == 1:
                    if random_number == 5:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led5.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led5.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led5.value(0)
                        time.sleep_ms(100)
                        led5.value(1)
                        time.sleep_ms(1500)
                        break

                passiveBuzzer.duty(0)
                led5.value(0)
                time.sleep_ms(0)
            # Led 5


            # Led 6
                led6.value(1)

                passiveBuzzer.duty(volume)
                passiveBuzzer.freq(1200)
                
                time.sleep_ms(led_time_slow)
                if a == 1:
                    if random_number == 6:
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        passiveBuzzer.duty(0)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led6.value(0)
                        time.sleep_ms(100)
                        if player_2_turn_end == True:
                            player_2_led.value(1)
                        if player_1_turn_end == True:
                            player_1_led.value(1)
                        led6.value(1)
                        time.sleep_ms(100)
                        
                        if player_2_turn_end == True:
                            player_2_led.value(0)
                        if player_1_turn_end == True:
                            player_1_led.value(0)
                        led6.value(0)
                        time.sleep_ms(100)
                        led6.value(1)
                        time.sleep_ms(1500)
                        break
                    
                passiveBuzzer.duty(0)
                led6.value(0)
                time.sleep_ms(0)
            # Led 6
