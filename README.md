
# 🚀 HackRadar: Discover & Share Hackathon Events

HackRadar is a web application developed for the IAB207 Assessment Task 3 at QUT. It allows users to discover upcoming hackathon events and share their own events with the community.

## Contributors

-   Ruben
    
-   Gustavo
    
-   Braydon
    

## Dependencies

Built Using Flask, SQLAlchemy, and Bootstrap.

### Installed using pip install

```
Bootstrap-Flask==2.1.0
click==8.1.3
dnspython==2.2.1
email-validator==1.2.1
Flask==2.2.2
Flask-Login==0.6.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
greenlet==1.1.2
idna==3.3
importlib-metadata==4.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
SQLAlchemy==1.4.40
Werkzeug==2.2.2
WTForms==3.0.1
zipp==3.8.1
gunicorn==20.1.0
```

## Features

-   **Event Discovery:** Browse and search for hackathon events.
    
-   **Event Details:** View detailed information about each event.
    
-   **User Submissions:** Users can upload their own hackathon events.
    
-   **User Authentication:** Secure login and registration for users.
    

## Deployment

Deploy the application on Heroku using the included Procfile with `gunicorn`:

1.  Create a new Heroku app:
    
    bash
    
    ```
    heroku create your-app-name
    ```
    
2.  Push the code to Heroku:
    
    bash
    
    ```
    git push heroku main
    ```
    
3.  Scale the application:
    
    bash
    
    ```
    heroku ps:scale web=1
    ```
    

## Usage

1.  Register or log in to your account.
    
2.  Browse through the list of hackathon events or use the search function to find specific events.
    
3.  Click on an event to view its details.
    
4.  Upload your own hackathon events or post comments on existing ones if you're a registered user.
