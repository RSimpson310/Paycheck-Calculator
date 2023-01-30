
class info:
    
    def __init__(self, name, hours, pay, target, gross, net):
        self.name = name
        self.hours = hours
        self.pay = pay
        self.target = target
        self.gross = gross
        self.net = net


def gross_income():
    global gross
    gross =  info.hours * info.pay
    return gross
    

def medicare():
    global med
    med = .0145 * gross
    return med

def social_sec():
    global ss
    ss = .062 * gross
    return ss

def find_taxes():
    global taxes
    global net
    taxes = med + ss
    net = gross - taxes
    return info.net

