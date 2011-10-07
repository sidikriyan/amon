from time import time
from amon.backends.mongodb import backend
import json

class Log(object):

	def __init__(self):
		self.levels = ('warning', 'error', 'info', 'critical', 'debug')

	def __call__(self, *args, **kwargs):

		log_dict = json.loads(args[0])

		try:
			level = log_dict.get('level')
			if level not in self.levels:
				level = 'notset'
		except: 
			level = 'notset'
		
		message = log_dict.get('message', '')

		now = int(time())
		entry = {'time': now, 'message': message, 'level': level}
		
		backend.store_entry(entry, 'logs')
		