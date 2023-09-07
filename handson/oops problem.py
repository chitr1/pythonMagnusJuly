class car:
    def m1(self,color,max_speed,acceleration,tyre_friction,engine_started,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=accelerstion
        self.tyre_friction=tyre_friction
        self.engine_started=No
        self.current_speed=0

    def start_engine(self):
        self.engine_started=yes

    def stop_engine(self):
        self.engine_started=No

    def aaceleration(self):
        if not self.engine_started:
            print("car not started")
    def apply_brake(self):
        if self.current_speed:
            print("current speed is greater")

    def sound_horn(self):
        if self. start_engine:
            print("beep beep")
        else:
            print("car not started")




class Truck(car):
     def m2(self, color, max_speed, acceleration, tyre_friction, engine_started,current_speed, max_cargo_weight):

        self.color=color
        self.max_speed=max_speed
        self.acceleration=accelerstion
        self.tyre_friction=tyre_friction
        self.engine_started=No
        self.current_speed=0
