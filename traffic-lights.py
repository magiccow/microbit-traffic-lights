from microbit import *

class Light:
    def __init__(self):
        self.phases = ["red","redamber","green","amber"]
        self.phase = 0
        self.oldPhase = 0
        
    def next(self):
        self.oldPhase = self.phase
        self.phase = (self.phase + 1) % 4
        
    def show(self):
        oldPhaseName = self.phases[self.oldPhase]
        self.lightMode(oldPhaseName, 0)
        
        phaseName = self.phases[self.phase]
        self.lightMode(phaseName, 9)

    def lightMode(self,phaseName,onoff):
        if phaseName=="red":
            display.set_pixel(0, 0, onoff) 
            pin0.write_digital(onoff>0)
        elif phaseName=="redamber":
            display.set_pixel(0, 0, onoff) 
            display.set_pixel(0, 1, onoff) 
            pin0.write_digital(onoff>0)
            pin1.write_digital(onoff>0)
        elif phaseName=="green":
            display.set_pixel(0, 2, onoff) 
            pin2.write_digital(onoff>0)
        elif phaseName=="amber":
            display.set_pixel(0, 1, onoff) 
            pin1.write_digital(onoff>0)            


light = Light()    

while True:
    light.show()
    sleep(1500)
    light.next()
        
