import datetime
import pyrebase
import matplotlib.pyplot as plt

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
dat = db.get().val()
timestamps = []
values = []
counter = 0
for key, value in dat.items():
	timestamps.append(datetime.datetime.strptime(value['time'][12:], "%H:%M:%S"))
	if(value['data']=='Someone Entered'):
		counter+=1
	else:
		counter-=1
	values.append(counter)
	plt.plot(timestamps, values)
	plt.xlabel('Time')
	plt.ylabel('Crowd')
	plt.title('Crowd Data Analytics')
plt.show()
