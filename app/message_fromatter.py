import json
import os
import re


class MessageFormatter:
    VARIABLE_PATTERN = re.compile(r'(?:{([\w]+)})')

    def __init__(self, ticket_links):
        assert len(ticket_links) > 0
        self.placeholders = {'tickets': self.format_ticket_links(ticket_links)}
        path = os.path.join(os.path.dirname(__file__), '../message.json')
        assert os.path.exists(path)
        with open(path) as json_file:
            self.message_json = json.load(json_file)
            self.load_placeholders()

    def format_message(self):
        for section in self.message_json['message']['blocks']:
            text = section['text']['text']
            matches = self.VARIABLE_PATTERN.findall(text)
            if len(matches) > 0:
                text = text.format(**self.placeholder_value_map(matches))
                section['text']['text'] = text

        return self.message_json['message']

    def placeholder_value_map(self, matches):
        value_map = {}
        for match in matches:
            if match in self.placeholders:
                value_map[matches[0]] = self.placeholders[matches[0]]
        return value_map

    @staticmethod
    def format_ticket_links(ticket_links):
        if len(ticket_links) == 1:
            return ticket_links[0]

        return ''.join(['\n\t• ' + link for link in ticket_links])

    def load_placeholders(self):
        for variable in self.message_json['variables']:
            # TODO: if variable has multiple options let's uer decide
            self.placeholders[variable] = self.message_json['variables'][variable][0]
