class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def processes(self):
        results = []
        results.append(self.washing.wash())
        results.append(self.rinsing.rinse())
        results.append(self.spinning.spin())
        return "\n".join(results)

    def startWashing(self):
        print(self.processes())


class Washing:
    def wash(self):
        return 'Washing...'

class Rinsing:
    def rinse(self):
        return 'Rinsing...'

class Spinning:
    def spin(self):
        return 'Spinning...'


washingMachine = WashingMachine()
washingMachine.startWashing()