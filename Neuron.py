# Constants defining the neuron's response curve

minact, rest, thresh, decay, maxact = -0.2, -0.1, 0.0, 0.1, 1.0
alpha, gamma, estr = 0.1, 0.1, 0.4

units = []
pools = []
unitbyname = {}

class Unit(object):
    __slots__ = ['name', 'pool', 'extinp', 'activation', 'output', 'exciters', 'newact']

    def __init__(self, name, pool):
        self.name = name
        self.pool = pool
        self.reset()
        self.exciters = []
        unitbyname[name] = self
        
    def reset(self):
        self.setext(0.0)
        self._setactivation()
        
    def setext(self, weight=1.0):
        self.extinp = weight
        
    def _setactivation(self, val=rest):
        self.activation = val
        self.output = max(thresh, val)
        
    def addexciter(self, aunit):
        self.exciters.append(aunit)
        
    def remove(self, aunit):
        self.exciters.remove(aunit)
        
    def computenewact(self):
        ai = self.activation
        plus = sum(exciter.output for exciter in self.exciters)
        minus = self.pool.sum - self.output
        netinput = alpha*plus - gamma*minus + estr*self.extinp
        if netinput > 0:
            ai = (maxact-ai)*netinput - decay*(ai-rest) + ai
        else:
            ai = (ai-minact)*netinput - decay*(ai-rest) + ai
        self.newact = max(min(ai, maxact), minact)
        
    def commitnewact(self):
        self._setactivation(self.newact)
