import serial
import requests
import socket
if __name__ == '__main__':
    hostname = socket.gethostname()
    ip = socket.gethostbtname(hostname)
    url = "http://"+str(ip)":5000/"
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            try:
                if line == "ua":
                    requests.post(url+'set_stat',{"num":1})
                if line == "a":
                    requests.post(url+'set_stat',{"num":2})
                if line == "b":
                    requests.post(url+'set_stat',{"num":3})

            except:
                print("error appear")
            print(line)
