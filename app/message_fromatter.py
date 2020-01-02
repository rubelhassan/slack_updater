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

    def format_ticket_links(self, ticket_links):
        ticket_links = self.customize_ticket_messages(ticket_links)
        if len(ticket_links) == 1:
            return ticket_links[0]

        return ''.join(['\n\t• ' + link for link in ticket_links])

    @staticmethod
    def customize_ticket_messages(tickets):
        user_tickets = []
        for ticket in tickets:
            customized = input("Type message like: custom message for {ticket} or Press ENTER to skip\n")
            if customized and customized.strip():
                customized = customized.format(ticket=ticket)
            else:
                customized = ticket
            user_tickets.append(customized)
        return user_tickets

    def load_placeholders(self):
        for variable in self.message_json['variables']:
            self.placeholders[variable] = self.determine_variable_value(variable,
                                                                        self.message_json['variables'][variable])

    @staticmethod
    def determine_variable_value(variable, values):
        if values == 1:
            return values[0]
        return input(f'select any of {values} for {variable}\n')
