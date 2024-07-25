import serial

ser = serial.Serial("COM3", 9600)

while True:
    a_var = ser.readline().decode()
    print("Type : " + str(type(a_var)) + " Value : " + a_var)