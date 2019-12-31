import json

import requests

from app import GitMiner, JiraParser, MessageFormatter, AppSettings


class SlackUpdater:

    def __init__(self):
        self.settings = AppSettings()
        assert len(self.settings.repositories) > 0
        self.commits = []
        self.load_recent_commits()

    def parse_tickets_from_commits(self, parser: JiraParser):
        parser.initialize([commit.message for commit in self.commits], self.settings.ticket_map)
        return parser.parse_tickets()

    def update_to_slack_channel(self, links):
        message = MessageFormatter(links).format_message()
        requests.post(self.settings.webhook, json.dumps(message))

    def load_recent_commits(self):
        for repo in self.settings.repositories:
            miner = GitMiner(repo)
            self.commits.extend(miner.find_author_commits(self.settings.commit_depth, self.settings.user['email']))

        if len(self.commits) <= 0:
            print("No commits are found")

