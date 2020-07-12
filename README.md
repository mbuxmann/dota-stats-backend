# BitVivAZ DOTA STATS

I created this Project to learn more about using API's and serving data with a Flask application. This was also a good chance to learn more about AWS and thus decided to host the back-end on an Amazon Elastic Compute Cloud.

The back-end consists of two different parts. The first part is a Python script which retrieves data from the public DOTA 2 API and stores the data into a SQLite database. This Python script is run via a cronjob on the server which allows it to run hourly. The script then checks if the new data from DOTA 2 API is equal or not equal to the latest data in the SQLite database and acts accordingly.

The second part is a Flask application that serves the data from the SQLite database to my front-end website that is hosted on GitPages.

The front-end consists of two pages. The home page which retrieves all the heroes available from the Flask application and stores it in an array. From that array the heroes are added to the website and shown. After selecting a hero from the home page a function is fired which stores the hero's name via local storage and is served to the second page.

The Second page is the data page which uses the stored hero name from the home page and retrieves the hero_id from the Flask application.
With the hero id a lot of requests are then made to the Flask application. The data from the Flask application is then parsed using Vanilla JavaScript and served to the user.

Currently the website only supports the resolution of 1920x1080

<b>Website:</b> [BitVivAZ DOTA STATS](https://bitvivaz.com/dota-stats/)

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
![alt text][Welcome Page]
![alt text][Oracle]
![alt text][Axe]
![alt text][Pudge]

[Welcome Page]: https://bitvivaz.com/personal/assets/webdev/dotastats/images/homepage.png "Home Page"
[Oracle]: https://bitvivaz.com/personal/assets/webdev/dotastats/images/oracle.png "Oracle"
[Axe]: https://bitvivaz.com/personal/assets/webdev/dotastats/images/axe.png "Axe"
[Pudge]: https://bitvivaz.com/personal/assets/webdev/dotastats/images/pudge.png "Pudge"
