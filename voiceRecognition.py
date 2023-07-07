import speech_recognition as sr
import time
import keyboard
import pyautogui
import json
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
    split_string = str(onePort).split(" - ")
    portVar = split_string[0]

print(portVar)
serialInst = serial.Serial(port=str(portVar), baudrate=9600)
serialInst.write(bytes("1", 'utf-8'))

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        if(keyboard.is_pressed('v')):
            audio = r.listen(source)
            try:
                command = str(r.recognize_google(audio)).lower()         
                print("You have said : \n")
                print(command)
                if(command == "turn on the light"):
                    serialInst.write(bytes("2", 'utf-8'))
                else:
                    serialInst.write(bytes("1", 'utf-8'))
            except Exception as e:
                print("Error: " + str(e))
   # time.sleep(1)
""""
r = sr.Recognizer()
def main():
    loop()

def loop():
    while(True):
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        if(keyboard.is_pressed('v')):
            audio = r.listen(source)
            try:
                command = str(r.recognize_google(audio)).lower()         
                print("You have said : \n")
                print(command)
                    
            except Exception as e:
                print("Error: " + str(e))
if __name__ == "__main__":
    main()       
    """