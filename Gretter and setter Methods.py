class car:
    def __init__(self, a=40):
        self.speed=a
    def get_speed(self): #getter method
        return self._speed
    def set_speed(self,a):#setter method
        if a<=0 or a>=160:
            print('Speed needs to between 0 to 160')
        else:
            self._speed=a
        
    speed=property(get_speed,set_speed)
