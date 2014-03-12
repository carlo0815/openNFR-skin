# 2boom & Taapat (c) 2012 0.5
from enigma import iServiceInformation
from Components.Converter.Converter import Converter
from Components.config import config
from Components.Element import cached
from Tools.Directories import fileExists
from Poll import Poll
import os

class MaggyEmuName(Poll, Converter, object):
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

		# NFR SoftCam Manager
		if config.NFRSoftcam.actcam.value:
			if config.NFRSoftcam.actcam.value != "none":
				camdlist = config.NFRSoftcam.actcam.value.split()
		if cardname:
			for line in cardname:
				if line.lower().find('oscam') > -1:
					info2 = 'oscam'
				elif line.lower().find('newcs') > -1:
					info2 = 'newcs'
				elif line.lower().find('wicard') > -1:
					info2 = 'wicardd'
				elif line.lower().find('cccam') > -1:
					info2 = 'cccam'
				else:
					info2 = ""
			cardname.close()
		if camdname:
			camdlist = camdname
		if camdlist:
			for line in camdlist:
				if line.lower().find('mgcamd') > -1 and line.lower().find('oscam') > -1:
					info = 'oscammgcamd'
					break
				if line.lower().find('cccam') > -1 and line.lower().find('oscam') > -1:
					info = 'oscamcccam'
					break
				elif line.lower().find('mgcamd') > -1:
					info = 'mgcamd'
				elif line.lower().find('oscam') > -1:
					info = 'oscam'
				elif line.lower().find('wicard') > -1:
					info = 'wicardd'
				elif line.lower().find('cccam') > -1:
					info = 'cccam'
				elif line.lower().find('camd3') > -1:
					info = 'camd3'
				elif line.lower().find('evocamd') > -1:
					info = 'evocamd'
				elif line.lower().find('newcs') > -1:
					info = 'newcs'
				elif line.lower().find('rqcamd') > -1:
					info = 'rqcamd'
				elif line.lower().find('gbox') > -1:
					info = 'gbox'
				elif line.lower().find('mpcs') > -1:
					info = 'mpcs'
				elif line.lower().find('sbox') > -1:
					info = 'sbox'
				else:
					info = 'unknow'
		if camdname:
			camdname.close()
		return info2 + info

	text = property(getText)

	def changed(self, what):
		Converter.changed(self, (self.CHANGED_POLL,))
