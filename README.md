# BitVivAZ DOTA STATS

I created this project to learn more about using API's and serving data with a Flask application. It was also a good opportunity to learn more about AWS, therefore I decided to host the back end on an Amazon Elastic Compute Cloud.

Currently, the website only supports the resolution of 1920x1080.

### TODO

- Support more resolutions
- Add a search bar to filter through heroes

### Tech Stack

- Flask
- Python
- JavaScript
- HTML
- CSS
- Bootstrap
- SQLite
- Nginx
- Gunicorn
- Amazon Web Services
- GitPages

### Features

- Heroes Pages, Data Page
- SQLite for database
- Python Script that retrieves data from Valve's DOTA API and stores it
- Flask Application which serves the SQLite data to the front-end website
- Front-end that parses all the data and displays it to the user
- Cronjob that runs a python script to update every hour all the data

### Source Code

- Front end: [GitHub](https://github.com/bitVivAZ/dota-stats)

### Screenshots
![Home Page][Welcome Page]
![Oracle][Oracle]
![Axe][Axe]
![Pudge][Pudge]

[Welcome Page]: https://buxmann.dev/static/img/dotastats-homepage.png "Home Page"
[Oracle]: https://buxmann.dev/static/img/dotastats-oracle.png "Oracle"
[Axe]: https://buxmann.dev/static/img/dotastats-axe.png "Axe"
[Pudge]: https://buxmann.dev/static/img/dotastats-pudge.png "Pudge"
