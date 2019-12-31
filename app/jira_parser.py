import re


class JiraParser:

    def initialize(self, messages, prefixes):
        self.prefixes = prefixes
        self.messages = messages
        self.TICKET_PATTERNS = self.generate_pattern()

    def parse_tickets(self):
        tickets = self.TICKET_PATTERNS.findall(' '.join(self.messages))
        tickets = [tuple(filter(lambda x: x is not None and x != '', ticket)) for ticket in tickets]
        return [self.ticket_url(ticket[0], ticket[1]) for ticket in tickets]

    def generate_pattern(self):
        return re.compile('|'.join([f'(({prefix})-[\d]+)' for prefix in self.prefixes]))

    def ticket_url(self, ticket, prefix):
        if prefix in self.prefixes:
            return self.prefixes[prefix] + ticket
        return ticket
