import argparse
import os
from app import GitMiner

# TODO: remove when user preference is done
parser = argparse.ArgumentParser()
parser.add_argument('--paths', '-p', help="set git repository path")
parser.add_argument('--branch', '-b', help="set git repository branch")
args = parser.parse_args()


if __name__ == '__main__':
    if args.paths and os.path.isdir(args.paths):
        miner = GitMiner(args.paths)
        commits = miner.find_author_commits(10, 'rubel.hassan@dsinnovators.com', date='2019-12-10')
        # commits = miner.find_author_commits(10, 'rubel.hassan@dsinnovators.com', branch='dev', date='2019-12-10')
        for commit in commits:
            print(commit)
            print(commit.message, commit.author)
            print(commit.authored_date)
            print(commit.authored_datetime)

    print("Done Processing!")
