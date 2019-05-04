# rss-nofification-google-chat
## Using this tool to notify news that get from RSS Feed

### Requirement:  
Python 2.5+. 
Pip. 

### Install dependency:
pip install -r requirements.txt

### Usage:
Add RSS feeds to rss.conf && set Google Chat webhook in *rssbot.py* (variable: `googleChatWebHook`).   
Run the following command. 
`python /path_to_script/rssbot.py`

### Crontab:
`* */10 * * * python /path_to_script/rssbot.py #Remember set timedelta in rssbot.py`
