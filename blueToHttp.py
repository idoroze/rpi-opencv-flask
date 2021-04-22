import serial
import requests
if __name__ == '__main__':
    url = "http://192.168.1.203:5000/"
    ser = serial.Serial('COM4', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            try:
                if line == "ua":
                    requests.get(url + "set_stat/1")
                if line == "a":
                    requests.get(url + "set_stat/2")
                if line == "b":
                    requests.get(url + "set_stat/3")

            except:
                print("error appear")
            print(line)
