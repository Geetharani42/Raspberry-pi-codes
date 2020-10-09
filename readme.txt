steps for connecting raspberry pi desktop in virtual mode:


step-1: turn on your hotspot. change your hotspot username:project1 and password: 123456789

step-2: Install Advance ip scanner , VNC viewer application in your laptop 

step-3: connect your laptop wifi to your mobile hotspot and turn on the raspberrypi. 
	now you can able to see connected devices as 2.

step-4: open advance ip scanner app and click on scan button ther you will get the raspberrypi ip like 192.xxx.xx.xx

step-5: open VNC viewer app and enter this ip. 
	it will pop-up one window click on continue and enter the username:pi and password:raspberrypi
	you can able to see the raspberry pi desktop.

step-6: click on file manager in top of the menu bar.

steps for run the project code:

 in this project we have 3 stages:
				1.dataset
				2.training
				3.recognation

step-1:first run the code home/pi/1_dataset.py. we need to enter the id first and then we need to see the camera. 
	it will take 30 images of user face.

step-2: Run the code home/pi/2_training.py. it will genrate an .yml file

step-3:Run the code home/pi/3_recognation.py. it will detecet your face and if it valid gate will open. 
       above 2 program need to run only when you need to train new faces to the device.