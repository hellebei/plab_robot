class Motob:

    def __init__(self):
        self.motors = [] #list of all motors whose values it sets
        self.value = None #most recent motor recommendation sent to the motob.

    def update(self):
        #load new motor recommendation into the value slot and operationalize it.
        pass

    def operationalize(self):
        #convert value into motor settings and send to the corresponding motor(s).
        pass


'''
In the robot project, the only actuators are the wheels, so the motob and the
(wheel) motor wrapper are about the same thing. See file motors.py for
details of the motor wrapper, and then build your motob class based on that.
'''