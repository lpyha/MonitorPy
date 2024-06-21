import serial
from enum import Enum
PORT = "COM5"
BAUDRATE = 115200
PAYLOAD_SIZE = 32

class HEADER(Enum):
    ACC = b'\xf0\xff\xff\xff'
    GYR = b'\xf1\xff\xff\xff'
    MAG = b'\xf2\xff\xff\xff'
    QUA = b'\xf3\xff\xff\xff'
    BAR = b'\xf4\xff\xff\xff'


def log_parser(data):
    match data[0:4]:
        case HEADER.ACC:
            return HEADER.ACC
        case HEADER.GYR:
            return HEADER.GYR
        case HEADER.MAG:
            return HEADER.MAG
        case HEADER.QUA:
            return HEADER.QUA
        case HEADER.BAR:
            return HEADER.BAR
        case _:
            return None

ser = serial.Serial(PORT, BAUDRATE)
while True:
    data = ser.read(PAYLOAD_SIZE)
    print(data[0:4])
    if (data[0:4] == HEADER.ACC.value):
        print("ACC")
    elif (data[0:4] == HEADER.GYR.value):
        print("GYR")
    elif (data[0:4] == HEADER.MAG.value):
        print("MAG")
    elif (data[0:4] == HEADER.QUA.value):
        print("QUA")
    elif (data[0:4] == HEADER.BAR.value):
        print("BAR")
    else:
        print("Unknown")
ser.close()
