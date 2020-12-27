"""""
Code by: Charanpreet Singh
Email: Charanmakkar@gmail.com
Linkedin profile: https://www.linkedin.com/in/charanpreet-singh-a29949133/
DM linkedin if need any help (Always open to help)
Development date Aug 19, 2020
Final editing done on Aug 25, 2020
Github Upload: Dec 27, 2020
"""""

##Importing required libraries
from pymodbus.client.sync import ModbusTcpClient as tcp, time

""""
Defining all functions and parameteres start from here.
all the defined libraries are defined above this note.
"""
####Function to set parameters for communicattion
def setClient(ip_adress):
    client = tcp(ip_adress)
    return client

#Main CODE to read data from resisters
def readData(register_value, unit):
    read = client.read_holding_registers(register_value, 2, unit).registers
    print(read)
    value = read[0]
    return value

while(1):
    #Set Ip address of device you want to communicate
    client = setClient('10.10.10.1')

    #Set Slave Address / Slave ID of the device
    SLaddress = 99
    try:
        #read = client.read_holding_registers(Starting Register address, Number of registers, unit = int(SLaddress)).registers
        read = client.read_holding_registers(3059, 2, unit = int(SLaddress)).registers
        value = str(read[0])
        #It prints value in stored in Holding resister
        print(value)
    except:
        #If get any kind of distortion or error in communication or miss any data...
        print("LOST SOMEWHERE")

    #Time delay of (1 = 1 second) 1 second after each run
    time.sleep(1)

    #To seperate readings after each run
    print("__" * 40)

