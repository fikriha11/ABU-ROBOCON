'''
update : 21 februari 2019 
Tracking FIX

'''

from math import*
import irlib.vision as vs
import irlib.engine as en
from time import sleep
import signal as sg
import irlib.kinematix as kn

#dAll = en.readAll()
#ballBool = dAll[4]
ballRange = 200
PORT = '/dev/ttyACM0'
def init():
	en.__init(PORT)
	sleep(1)
	#dAll = en.readAll()
	#ballBool = dAll[4]
	vs._init_(640, 480,"r2",False)
	sleep(1)
	en.modRPS(80)
def __signal(signum, fram):
	global loop
	#print 'Exiting Program'
	loop = False
	#sleep(1)
	en.RESET()
	sleep(1)
	en.__exit()
def pixel(rx, ry):
	jarakPixel = 0
	jarakPixel = ((ry*ry) + (rx*rxx))**0.5
	return jarakPixel
def Main():
	while True:
		ball_x,ball_y = vs.BallObstacle()
		print " ini x ", ball_x , "ini y : ", ball_y
		print 'tracking'
		xMember = ball_x
		yMember = ball_y
		pwmBelakang,pwmKanan,pwmKiri= kn.speed_out(53)
		
		print " pwmBelakang = ", pwmBelakang, ", pwmKiri = ", pwmKiri, ", pwmKanan = ", pwmKanan
		en.Dribble(pwmKanan,pwmKiri)
		en.setRPS(pwmBelakang,pwmKanan,pwmKiri)
		
		
		
		if yMember < 53 :
			en.setKick(75)
			#en.STOP()
			print "stop"
#		elif yMember >= 100:
#			en.setDribble(0)
		sleep(0.1)

if __name__ == '__main__':
	print "go . . . "
	init()
	sg.signal(sg.SIGINT, __signal)
	Main()


