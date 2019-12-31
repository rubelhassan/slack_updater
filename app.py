from app import SlackUpdater, JiraParser

if __name__ == '__main__':
    try:
        slack_updater = SlackUpdater()
        tickets = slack_updater.parse_tickets_from_commits(JiraParser())
        slack_updater.update_to_slack_channel(tickets)
    except Exception as e:
        print("please configure settings.json")
        print(e)

    print("Done Processing!")
