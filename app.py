import argparse
import os
import datetime
from git import Repo

# TODO: remove when user preference is done
parser = argparse.ArgumentParser()
parser.add_argument('--paths', '-p', help="set git repository path")
parser.add_argument('--branch', '-b', help="set git repository branch")
args = parser.parse_args()


def yesterday():
    return datetime.date.today() - datetime.timedelta(days=1)


# TODO: isolate git related staff
def find_last_n_commits(repo, branch, n, author_email, date):
    last_n_commits = repo.iter_commits(branch, max_count=n, committer=author_email, after=date)
    return [commit for commit in last_n_commits]


if __name__ == '__main__':
    if args.paths and os.path.isdir(args.paths):
        repo = Repo(args.paths)
        assert not repo.bare
        branch = repo.active_branch
        if args.branch:
            branch = args.branch
        # commits = find_last_n_commits(repo, 'dev', 10, 'rubel.hassan@dsinnovators.com', '2019-12-10')
        commits = find_last_n_commits(repo, branch, 10, 'rubelhassan@outlook.com', yesterday().isoformat())
        for commit in commits:
            print(commit.authored_date)
            print(commit.authored_datetime)

    print("Done Processing!")
