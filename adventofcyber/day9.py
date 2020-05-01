import requests
MACHINE_IP = '10.10.169.100'
MACHINE_PORT = '3000'

curValue = ''
curPath = ''
flag = ''
while curValue != 'end':
    flag += curValue
    responseJSON = requests.get('http://' + MACHINE_IP + ':' + MACHINE_PORT + '/' + curPath).json()
    curValue = responseJSON['value']
    curPath = responseJSON['next']
print('final: ', flag)