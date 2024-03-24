# tarpit
Tool for detecting web-interactions. 

```
"It's like a HoneyPot, but Tar instead of Honey, and a Pit instead of a Pot"
```

Tarpit is a webserver that sends you Discord notifications via webhooks upon GET requests. Best suited for XSS-Bug hunting, but sky is your limit!

## Usage:
To get the server running, run these commands:
```
pip install -r requirements.txt
python3 main.py
```

and modify the `settings.json` generated to your liking! 

> ⚠️ Remember to add a Discord Hook url to the `settings.json` file after first run!

Without this url the alerting system will not work, and you will not be notified of when a payload is triggered or a resource is being requested.

It is reccomended to tie the server to a domain for ease of access. Any requests made to the server as for example: `example.com/example_path` will trigger a Discord message, if the example_path is not excluded by `"path_block"` in the `settings.json`


## Description:
Tarpit is meant to be used as a handy tool to detect when and where HTTP- requests are made. One of it's main use-cases is detecting "behind the curtain" XSS- vulnerabilites with payloads that require resources from a web server. Such a payload would be for example `<img href=":SERVER_ADDRESS:">`.

Because you get a Discord notification from the request, even payloads that are rendered later will get caught. With the headers it's easy to identify who, what, and where of the connection.

## Notes
Important: This project is intended for educational and lawful purposes only. The author and contributors are not responsible for any misuse or illegal activities that may arise from using this software. By using this software, you agree to comply with all applicable laws and regulations. If you are uncertain about the legality of your actions, please seek legal advice before proceeding. The author and contributors disclaim any and all liability for any direct, indirect, or consequential loss or damage arising from your use of the software. Use this software at your own risk.

Thank you for your understanding and cooperation.