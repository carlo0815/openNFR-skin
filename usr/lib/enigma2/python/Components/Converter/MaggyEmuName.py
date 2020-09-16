from enigma import iServiceInformation
from Components.Converter.Converter import Converter
from Components.Element import cached
from Tools.Directories import fileExists
from Poll import Poll
import os

from enigma import iServiceInformation
from Components.Converter.Converter import Converter
from Components.config import config
from Components.Element import cached
from Tools.Directories import fileExists
from Poll import Poll
import os

class EmuName(Poll, Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)
		self.poll_interval = 2000
		self.poll_enabled = True
		
	@cached
	def getText(self):
		info = ""
		info2 = ""
		camdname = None
		cardname = None
		camdlist = None
		# VTI 	
		if fileExists("/tmp/.emu.info"):
			try:
				camdname = open("/tmp/.emu.info", "r")
			except:
				camdname = None
		# TS-Panel
		elif fileExists("/etc/startcam.sh"):
			try:
				for line in open("/etc/startcam.sh"):
					if "script" in line:
						camdname = "%s" % line.split("/")[-1].split()[0][:-3]
			except:
				camdname = None
		# BlackHole	
		elif fileExists("/etc/CurrentBhCamName"):
			try:
				camdname = open("/etc/CurrentBhCamName", "r")
			except:
				camdname = None
		# Domica	
		elif fileExists("/etc/active_emu.list"):
			try:
				camdname = open("/etc/active_emu.list", "r")
			except:
				camdname = None
				# OoZooN
		elif fileExists("/tmp/cam.info"):
			try:
				camdname = open("/tmp/cam.info", "r")
			except:
				camdname = None
		# Merlin2	
		elif fileExists("/etc/clist.list"):
			try:
				camdname = open("/etc/clist.list", "r")
			except:
				camdname = None
		#Pli
		elif fileExists("/etc/init.d/softcam") or fileExists("/etc/init.d/cardserver"):
			try:
				camdname = open("/etc/init.d/softcam", "r")
			except:
				camdname = None
			try:
				cardname = open("/etc/init.d/cardserver", "r")
			except:
				cardname = None 
		elif fileExists("/etc/.emustart"):
			try:
				camdname = open("/etc/.emustart", "r")
			except:
				camdname = None

	# NFR SoftCam Manager
		if config.NFRSoftcam.actcam.value:
			if config.NFRSoftcam.actcam.value != "none":
				camdlist = config.NFRSoftcam.actcam.value.split()

		if cardname:
			for line in cardname:
				info2 = ""
				if 'oscam' in line.lower():
					info2 = 'oscam'
				elif 'newcs' in line.lower():
					info2 = 'newcs'
				elif 'wicard' in line.lower():
					info2 = 'wicardd'
				elif 'cccam' in line.lower():
					info2 = 'cccam'
			cardname.close()
		if camdname:
			camdlist = camdname
		if camdlist:
			info = 'unknow'
			for line in camdlist:
				if 'mgcamd' in line.lower() and 'oscam' in line.lower():
					info = 'oscammgcamd'
					break
				if 'cccam' in line.lower() and 'oscam' in line.lower():
					info = 'oscamcccam'
					break
				elif 'mgcamd' in line.lower():
					info = 'mgcamd'
				elif 'oscam' in line.lower():
					info = 'oscam'
				elif 'wicard' in line.lower():
					info = 'wicardd'
				elif 'cccam' in line.lower():
					info = 'cccam'
				elif 'camd3' in line.lower():
					info = 'camd3'
				elif 'evocamd' in line.lower():
					info = 'evocamd'
				elif 'newcs' in line.lower():
					info = 'newcs'
				elif 'rqcamd' in line.lower():
					info = 'rqcamd'
				elif 'gbox' in line.lower():
					info = 'gbox'
				elif 'mpcs' in line.lower():
					info = 'mpcs'
				elif 'sbox' in line.lower():
					info = 'sbox'
		if camdname:
			camdname.close()
		return info2 + info

	text = property(getText)

	def changed(self, what):
		Converter.changed(self, (self.CHANGED_POLL, ))
