# Andela Bootcamp Project REF: bc-8-ideabox.
######***Submitted by : Kimani Ndegwa [https://www.kimanindegwa.co.ke]***
######***Submitted to : Andela Kenya***

Repository for the IdeaBox Project application.

The IdeaBox is a project buit by the Flask Microframework in the Python stack leveraging its brilliant extension library to improve its feature base.

To describe its primary features, the IdeaBox was built so that:

1. As a user I should be able to signup / login
2. As a user I can post ideas
3. Ideas should have a title and a description
4. Use Markdown editor for description
5. Other users can comment on the ideas
6. Other users can upvote / downvote ideas

This project was submitted as part of a learning process to Andela Kenya for the qualification of the 8th Cohort.
The steps to have the project locally are:

1. Create your virtual environment at a desired location on your local machine via `virtualenv venv`
2. First clone the repository via `git clone https://github.com/Kimanicodes/bc-8-ideabox.git`
3. Install its dependencied via `pip install -r requirements.txt`
4. Initialise the database environment via `python routes.py db init`
5. Load the migrations via `python routes.py db migrate `
6. Upgrade the migrations via `python routes.py db upgrade`
7. Run the server via `python routes.py` in the app folder and view.

