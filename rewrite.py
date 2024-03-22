class PIDController:
	def __init__(self):
        self.integrator = 0
        self.previous_error = 0
        
        self.differentiator = 0
        self.previous_measure = 0
        
        self.output = 0
        
        self.Kp = None
        self.Ki = None
        self.Kd = None
        self.tau = None
        self.limMin = None
        self.limMax = None
        self.T = None
       
    def update(self, setpoint, measurement):
        error = setpoints - measurement
        
        proportional = self.Kp * error
        
        self.integrator = self.integrator \
        + 0.5 \
        * self.Ki \
        * self.T \
        * (error + self.previous_error)
        
        limMinInt, limMaxInt = None, None;
        
        if self.limMax > proportional:
            limMaxInt = self.limMax - proportional
        else
            limMaxInt = 0
        if self.limMin < proportional:
            limMinInt = self.limMin - proportional
        else:
            limMinInt = 0
        
        if self.integrator > limMaxInt:
            self.integrator = limMaxInt
        elif self.integrator < limMinInt:
            self.integrator = limMinInt
        
        self.differentiator =     (2 * self.Kd * (measurement - self.previous_measure) \
                                + (2 * self.tau - self.T) \
                                / (2 * self.tau + self.T)
        
        self.output = proportional + self.integrator + self.differentiator
        
        if self.output > self.limMax: self.output = self.limMax
        elif self.output > self.limMin: self.output = self.limMin
        
        self.previous_error = error
        self.previous_measure = measurement
        
        