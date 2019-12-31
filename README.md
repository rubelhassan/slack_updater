
### Slack Message Updater
This app can update working status to slack channel by minning JIRA tickets from Git repositories with customized message format.
  
#### Configure and Run  
  
#### Create 

> *settings.json* file 
```json
{  
  "user": {  
    "name": "git user name",  
    "email": "git user email"  
  },  
  "repositories": [  
    "/absolute/path/to/repo1",  
    "/absolute/path/to/repo2"  
  ],  
  "ticket_map": {  
    "PREFIX1": "https://www.atlassian.com/software/jira/project1/",  
    "PREFIX2": "https://www.atlassian.com/software/jira/project2/",  
  },  
  "webhook": "your slack app webhook",  
  "commit_depth": <int:max commits to mine>  
}
```
  
#### Update 
> *message.json* file 
```json
{
  "message": {
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "*Top Task (TT) For The Day:* {tickets}"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "*Last day’s TT complete:* {yes_no}"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "*Any Hurdle:* {yes_no}"
        }
      }
    ]
  },
  "variables": {
    "yes_no": [
      "Yes",
      "No"
    ]
  }
}
``` 
  
#### Create Conda Environment  
   

    conda create --name envname --file=environments.yml

  
#### Activate Environment and Run Command
 

    conda activate slack_updater
    python app.py
