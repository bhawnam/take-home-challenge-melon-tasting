# Melon Tasting Reservation Scheduler

The idea of this app is to build a simple service to help users make reservations to go to a fancy melon tasting! 
Enabling users to search for and book reservations.
We offer coverage 24/7/365 (including weekends and holidays) and have unlimited appointments.
<br> 
Tasks:
<br> 
1. A user should be able to “log in”, pick a date, choose an optional time range, and then be shown all the available reservations that meet the criteria.
<br>
2. They can then book an appointment of their choice. If there are no reservations available, you should display a message indicating that.
<br>
3. There should also be a page which shows all reservations for a given user.	
<br>
Reservation Contraints:
<br>
all reservations must start and end on the hour or half hour
all reservations are exactly 30 minutes long
a user can only have 1 reservation on a calendar date (#tooMuchMelon)
If these conditions cannot be met (for example the user has already booked an appointment on the chosen date), show an error message indicating that.

<br> 

## Contents 
* [Features Built](#features)
* [Technologies & Stack](#techstack)
* [Set-up & Installation](#installation)

## <a name="features"></a> Features Built

For Task 1,
<br>
On the homepage, I built a login form with the ability to take in username or their email address with the password to allow the users to see their profile page. The password is validated against the database field of that user's email or username. A flash message indicates their successful or unsuccessful login attempt.
<br>
Once users are logged in, they are taken to the reservation scheduler page to pick a date of their choice. They can also choose an optional start and end time to serch for avialable options. (Times are validated to be chosen such that they start and end on the hour or half hour)
After choosing the date and optional time range, users can search for available slots. 
<br>
<br>
For Task 2, 
<br>
After making the selection, their choice is matched against their reservations in the DB. If a reservation is found for the same date, users are prompted an error message (#TOOMUCHMELONS).
<br>
If not, users are taken to all_reservations page and are shown (in a dropdown format), available time slots in 30 min intervals of their desired date. They can then choose a slot and book. 
<br>
<br>
For Task 3,
<br>
After successfully booking a slot, users are directed to the user-reservations page. Then can then see a table of all their reservations.
<br>
<br>
Notes:
<br>
I added a seed_database file which makes use of Faker library to feed the database with 5 users and their respective melon tasting reservations. 
<br>
For the date and time logic to work while reserving slots, I leveraged Python's datetime library. 
<br>
Added some styling using CSS and added it in styles.css file

## <a name="techstack"></a> Technologies and Stack
**Backend:**
Python, Flask, Jinja, SQLAlchemy, PostgreSQL, Faker <br>
**Frontend:**
HTML5, CSS3 <br>


## <a name="installation"></a> Set-up & Installation

Install a code editor such as [VS code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/).<br>
Install [Python3](https://www.python.org/downloads/mac-osx/)<br>
Install [pip](https://pip.pypa.io/en/stable/installing/), the package installer for Python <br>
Install [postgreSQL](https://www.postgresql.org/) for the relational database.<br>


Clone or fork repository:
```
$ git clone https://github.com/bhawnam/take-home-challenge-melon-tasting.git
```

cd into the project folder
```
cd take-home-challenge-melon-tasting
```
Create and activate a virtual environment
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```
With PostgreSQL, create the melon_reservations database
```
$ createdb melon_reservations
```
Create all tables and relations in the database and seed all data:
```
$ python3 seed_database.py
```

In the project folder run, 
```
$ python3 server.py
```