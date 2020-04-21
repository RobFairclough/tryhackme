num = 0
port = 3010
operations = ['add', 'minus']

def readCommand(res):
    split = res.split(' ')
    nextOp = split[0]
    nextNum = split[1]
    nextPort = split[2]