from Components.VariableText import VariableText
from Components.config import config
from Components.UsageConfig import defaultMoviePath
from enigma import eLabel
from Components.Renderer.Renderer import Renderer
from os import path, statvfs



class mvmHDDfree(Renderer, VariableText):
	def __init__(self):
		Renderer.__init__(self)
		VariableText.__init__(self)
	GUI_WIDGET = eLabel

	def changed(self, what):
		if not self.suspended:
			try:
                                videodir_value = defaultMoviePath()
				if path.exists(videodir_value):
					stat = statvfs(videodir_value)
					free = (stat.f_bavail if stat.f_bavail!=0 else stat.f_bfree) * stat.f_bsize / 1048576
					if free >= 10240:
						fdspace = "%d GB " %(free/1024)
						self.text = fdspace + _(videodir_value)
					else:
						fdspace = "%d MB " %(free)
						self.text = fdspace + _(videodir_value)
				else:
					self.text = '---'
			except:
				self.text = 'ERR'
