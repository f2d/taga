import json
from taga import Taga

settings_filename = 'settings.json'

with open(settings_filename) as settings_file:
	settings = json.load(settings_file)

tagaInstance = Taga(settings)
tagaInstance.run()
