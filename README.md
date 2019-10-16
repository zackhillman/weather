*Run:* 

`python -m venv venv`

`. venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

*Send Emails:* 

`python manage.py sendemail`

### Scalability 
**Bottlenecks**:

1. Emails are processed synchronously

**Solutions**: 

1. When we send emails, we can batch together users with the same location.

2. I would add "email tasks" to a queue and have multiple workers reading from the queue. This would allow emails to be processed concurrently. 

3. Allow workers to pull weather data from separate in-memory cache.

### Security 
As it stands user's can enter any "valid" email they like.

**Solutions**:

1. Make users confirm email address.
2. Add captcha (or similar solution) to prevent non-human users.

### Re-Usability 
1. Fetching weather data can be a separate service.
2. Sending emails can also be separate.

### Re-Inventing the Wheel? 
1. django-autocomplete-light - for location autocompletion

### Usability 
Users are able to select their location using autocomplete. To improve upon this, I would add more location choices, and possibly branding to the front end.
