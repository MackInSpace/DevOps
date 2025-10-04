#README.MD
"""Job-Search mini-app
Overview
Add job description (POST/jobs)
Search job description (GET http://….5000)
Return results ranked (title matches > description matches)

Service Python(Flask) = memory storage

Using Python 3.9+
Pip install -r requirements.txt (bash)

-Run the app with 
Python app.py

http://…5000 web page

Blank slate web page - next task is to add our jobs
(curl or insomnia) 
Adding to our application/json (POST)
{
“Title”: “Backend Engineer”,
“Company”: “Ziprecruiter”,
“Location”: “Remote”,
“Description”: “Work on backend systems with Python and Kubernetes”,
“Tags”: [“Python”, “Kubernetes”, “Backend”]
}

Response (JSON/I cannot remember the code):
{“id”: 1, “message”: “Successfully added job”}

Search Jobs (GET http//….)

Response:
{
“Id”: 1,
“Title”: “Backend Engineer”,
“Company”: “Ziprecruiter”,
“Location”: “Remote”,
“Description”: “Work on backend systems with Python and Kubernetes”,
“Tags”: [“Python”, “Kubernetes”, “Backend”],
“Score”: 2
}

Testing phase:
Bash terminal:
Pytest

Future improvements 
Database of different jobs (Postgres, MongoDB)
Algo - Sorting
Implementation of more advanced ranking algorithms
Adding Frontend UI
OPTIONALLY - Dockerfile - docker-compose.yml """
