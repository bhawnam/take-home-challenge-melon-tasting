# Melon Tasting Reservation Scheduler

The idea of this app is tp build a simple service to help users make reservations to go to a fancy melon tasting! 
Enabling users to search for and book reservations.
We offer coverage 24/7/365 (including weekends and holidays) and have unlimited appointments.

<br> 
Tasks:
1. A user should be able to “log in”, pick a date, choose an optional time range, and then be shown all the available reservations that meet the criteria.
2. They can then book an appointment of their choice. If there are no reservations available, you should display a message indicating that.
3. There should also be a page which shows all reservations for a given user.	

Reservation Contraints:
all reservations must start and end on the hour or half hour
all reservations are exactly 30 minutes long
a user can only have 1 reservation on a calendar date (#tooMuchMelon)
If these conditions cannot be met (for example the user has already booked an appointment on the chosen date), show an error message indicating that.

<br> 

## Contents 
* [Features Built](#features)
* [Technologies & Stack](#techstack)
* [Set-up & Installation](#installation)

## <a name="features"></a> Features


<br>
<br>
For Task 1,
On the homepage, I built a login form with the ability to take in username or their email address with the password to allow the users to see their profile page. The password is validated against the database field of that user's email or username. A flash message idicates their successful or unsuccessful login attemp.
Once users are logged in, they are taken to the reservation scheduler page to pick a date of their choice. They can also choose a optional start and end time to serch for avialable options. (Times are validated to be chosen such that they start and end on the hour or half hour)
After choosing the date and optional time range, users can Search for available slots. 
<br>
<br>
For Task 2, 
Ater making the selection, their choice is matched against their reservations in the DB. If a reservation in found for the same date, users are prompted an error message (#TOOMUCHMELONS).
If not, users are taken to all_reservations page and are shown (in a dropdown format) avaialable time slots in 30 min intervals of their desired date. They can choose a slot and book. 
<br>
<br>
For Task 1,


<br>
<br>

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
$ git clone 
```

cd into the take-home-challenge folder
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
python3 server.py
```