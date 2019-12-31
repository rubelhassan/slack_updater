import json
import os


class AppSettings:

    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), '../settings.json')
        assert os.path.exists(path)
        with open(path) as json_file:
            settings_json = json.load(json_file)
            self.user = settings_json['user']
            self.repositories = settings_json['repositories']
            self.webhook = settings_json['webhook']
            self.ticket_map = settings_json['ticket_map']
            self.commit_depth = settings_json['commit_depth']
