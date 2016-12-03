class Pool:

    __slots__ = ['sum', 'members']
    
    def __init__(self):
        self.sum = 0.0
        self.members = set()

    def addmember(self, member):
        self.members.add(member)

    def updatesum(self):
        self.sum = sum(member.output for member in self.members)

    def display(self):
        result = sorted(((unit.activation, unit.name) for unit in self.members), reverse=True)
        for i, (act, unitbyname) in enumerate(result):
            print '%s: %.2f\t' % (unitbyname, act),
            if i % 4 == 3: print
        print '\n'
