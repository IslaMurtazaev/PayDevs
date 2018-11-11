### Tech assignment
Task: Create a system for calculating the cost of development services (billing - hourly, monthly, task).

As a logged in user, I can:
Create a project - name and description.
Set the rate of its services per hour for the created project.
Specify your tariff rate for the created project (the method of charging is hourly, monthly, recurring). If the tariff rate is hourly, then I can issue an invoice for payment at any time, after specifying the time and date of completion of work. If the monthly tariff rate, then I can issue an invoice for payment only for the previous months. If the tariff rate is backward, then I can issue an invoice for payment only after indicating that the task has been completed.
Specify the time and date of commencement of work on the created project.
Specify the time and date of completion of work on the created project.
Create an invoice for the created project, which will indicate the project name, tariff rate, the time worked out and automatically calculate the cost of services based on the hours worked and the established rate.
Save invoice for payment in PDF format.

#### Setup instructions

##### Set up backend
* ```cd backend/```
* ```python3 -m venv ./venv```
* ```source venv/bin/activate```
* ```pip install -r requirements.txt```
* ```python manage.py migrate```

##### Install frontend dependencies
* ```cd frontend/```
* ```npm install```


#### Start servers

Start backend
* ```python manage.py runserver```

Start frontend
* ```npm start```
