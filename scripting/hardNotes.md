
# Task
The VM you have to connect to has a UDP server running on port 4000. Once connected to this UDP server, send a UDP message with the payload "hello" to receive more information. You will find some sort of encryption(using the AES-GCM cipher). Using the information from the server, write a script to retrieve the flag. Here are some useful thingsto keep in mind:

    sending and receiving data over a network is done in bytes
    the PyCA encryption library and functions takes its inputs as bytes
    AES GCM sends both encrypted plaintext and tag, and the server sends these values sequentially in the form of the encrypted plaintext followed by the tag

This machine may take up to 5 minutes to configure once deployed. Please be patient. 

Use this general approach(use Python3 here as well):

    Use the Python sockets library to create a UDP socket and send the aforementioned packets to the server
    use the PyCA encyption library and follow the instructions from the server

First payload to send is 'hello'
first response: `You've connected to the super secret server, send a packet with the payload ready to receive more information`

Second payload to send is 'ready'
second response: `key:thisisaverysecretkeyl337 iv:secureivl337 to decrypt and find the flag that has a SHA256 checksum of ]w�ҿwx`T�U�Ms��'�΁n�h�]rbc�� send final in the next payload to receive all the encrypted flags` - font missing chars? 

payload to repeat ad infinitum from here is 'final'
send in pairs for text & tag, decrypt and check against the checksum