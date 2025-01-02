class Robot():
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.orientation=0
        self._step=1
    
    @property
    def id(self):
        return self._id
    @property
    def x(self):
        return self._x
    @property
    def y(self):

        return self._y

    @id.setter
    def id(self, value):
        self._id = value
    @x.setter
    def x(self, value):
        self._x = value
    @y.setter
    def y(self, value):
        self._y = value
    def turn_clockWise(self):
        self.orientation += 90
        if self.orientation==360:
            self.orientation=0
    def turn_antiClockWise(self):
        
        self.orientation -= 90
        if self.orientation<0:
            self.orientation=270
    def walk(self,):
        if self.orientation == 0 or self.orientation % 360 == 0:
           self.x+=self._step
        elif self.orientation % 270 == 0:
            self.y-=self._step
        elif self.orientation % 180 == 0:
            self.x-=self._step
        elif self.orientation % 90 == 0:
            self.y+=self._step
    def get_position(self):
        print(f"the robot is at ({self.x},{self.y})")
    def __str__(self):
        return "this first generation robot"

myrobot=Robot("41894",0,0)
myrobot.walk()
myrobot.turn_clockWise()    
myrobot.walk()
myrobot.get_position()

class Robot_G2(Robot):
    def __init__(self,id,x,y,charge):
        super().__init__(id,x,y)
        self.charge=charge
        self.turbo_state=False
    def turbo(self):
        if self.charge>0:
            self.turbo_state=True
        else :
            print("out of energy")
    def walk(self):
        if self.turbo_state and self.charge > 0:
            self._step=2
            self.charge-=1
        else:
            self.turbo_state=False
            self._step=1
        super().walk()
    def __str__(self):
        return "this 2 generation robot"
robot2gen=Robot_G2("4484",0,0,10)
robot2gen.turbo()
robot2gen.walk()
robot2gen.turn_antiClockWise()
robot2gen.walk()
robot2gen.turn_clockWise()
robot2gen.walk()
robot2gen.get_position()
print(robot2gen)