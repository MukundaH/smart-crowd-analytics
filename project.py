import serial
import datetime
import pyrebase

config = {
  'apiKey': "AIzaSyAq0G9B-HBlLAxRKZzoC3eJnOtsyBu14Bk",
  'authDomain': "smart-crowd-analytics.firebaseapp.com",
  'databaseURL': "https://smart-crowd-analytics-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "smart-crowd-analytics",
  'storageBucket': "smart-crowd-analytics.appspot.com",
  'messagingSenderId': "243437997148",
  'appId': "1:243437997148:web:c0ef398d7b6713e3b7aa99"
};
firebase = pyrebase.initialize_app(config)
db = firebase.database()
ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
counter = 0
while(True):
	arduinodata = ser.readline().decode('ascii')
	if(arduinodata!=""):
		if(arduinodata=="Someone Entered"):
			counter+=1
		else:
			counter-=1
		current_time = datetime.datetime.now()
		dat = {"time" : current_time.strftime("%d/%m/%Y, %H:%M:%S"), "data" : arduinodata}
		db.push(dat)
		print(current_time , " " , arduinodata, " ", counter)
