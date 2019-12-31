import datetime
from git import Repo


class GitMiner:
    def __init__(self, path):
        self.repo = Repo(path)
        assert not self.repo.bare

    def find_author_commits(self, max_count, author_email, branch=None, date=None):
        if not date:
            date = self.yesterday().isoformat()

        if branch:
            commits = self.repo.iter_commits(branch, max_count=max_count, committer=author_email, after=date)
        else:
            commits = self.repo.iter_commits(max_count=max_count, committer=author_email, after=date, all=True)

        return [commit for commit in commits]

    @staticmethod
    def yesterday():
        return datetime.date.today() - datetime.timedelta(days=1)
