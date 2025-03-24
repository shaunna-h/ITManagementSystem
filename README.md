# ITManagementSystem
# Create Virtual Environment
python -m venv myenv
source venv/bin/activate or just activate
On Windows: venv\Scripts\activate

# Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

# To start the server
python manage.py runserver

# Docker
If you want to run the local docker container in the terminal:
docker build -t my-django-app .
docker run --rm -p 8000:8000 my-django-app
Access it through docker desktop rather than the terminal.

# Render
Access docker container on Render via: https://itmanagementsystem-docker.onrender.com/ 

# Sign-in for admin
I have been unable to link this to the main UI, so to access admin, enter /admin/ on the homepage url.
They can create categories, users, etc.
Username: administrator
Password: administrator

# Sign-in for User
Username = johndoe
Password = userpass123

Can create your own through the Sign-up page.

# Content
Home Page (Index): Basic welcome page.
Dashboard: After logging in, users can see a list of their assets and low-inventory warnings.
Add/Edit/Delete Assets: Administrators can manage asset records.
Categories: Users can assign categories to assets.
Logout: Securely end the session.

# Tests
python manage.py test

# OWASP
SQL Injection:
Uses Django’s ORM for all database queries, preventing raw SQL concatenation.
Any raw queries (if needed) are parameterized.

Cross-Site Scripting (XSS):
Rely on Django’s template autoescaping.
Avoid |safe for user-generated data.
Optionally configure a Content Security Policy (CSP) using django-csp.

Cross-Site Request Forgery (CSRF):
CsrfViewMiddleware is enabled, requiring a valid CSRF token for all POST requests.
Templates include {% csrf_token %} in forms.
