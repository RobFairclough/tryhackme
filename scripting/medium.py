import socket
import time
num = 0.0
host = '10.10.8.225'
startPort = 1337
finalPort = 9765

def operate(left, right ,operator):
    print(left, operator, right)
    if operator == 'add':
        return left + right
    elif operator == 'minus':
        return left - right
    elif operator == 'multiply':
        return left * right
    elif operator == 'divide':
        return left / right

curPort = startPort
while True:
    try:
        sock = socket.socket()
        sock.connect((host, curPort))
        print('connected to port', curPort)
        if curPort == 9765:
            print('done, port 9765 reached')
            print('final number: ', num)
            print('rounded to two decimals: ', round(num, 2))
            break
        # send request to port
        req = b"GET / HTTP/1.1\r\nHost: 10.10.8.225\r\nAccept: text/html\r\nConnection: close\r\n\r\n"
        sock.send(req)
        # receive response
        res = sock.recv(8192)
        readable = repr(res)
        print('response string: ', readable)
        splitRes = readable.split('\\n')
        print('split response: ', splitRes)
        # operation is the final part
        operation = splitRes[-1]
        print('operation: ', operation)
        # parse response
        splitOp = operation.split(' ')
        nextOp = splitOp[0]
        nextNum = float(splitOp[1])
        # has a trailing ' at the end which needs removing
        nextPort = int(splitOp[2][:-1])
        if curPort == nextPort:
            print('port not changed, repeating')
            time.sleep(1)
            continue
        curPort = nextPort
        num = operate(num, nextNum, nextOp)
        print('number is ', num, ' switching to port ', curPort)
        sock.close()
    except Exception as e:
        # this catches econnrefused
        sock.close()
        pass
