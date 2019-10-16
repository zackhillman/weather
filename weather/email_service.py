import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def sendEmail(location, weather, toEmail):
    """
    Sends an email to given toEmail. Body of email includes given location and weather.
    """
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "zackweather2@gmail.com"
    password = 'Zackweather1'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = getSubject(weather)
    msg['From'] = 'zackweather2@gmail.com'
    msg['To'] = toEmail
    html = """\
    <html>
    <body>
        <p>Hi! <br><br>
        It is currently {} degrees in {}, {}.
        </p>
        <img height="50" width="50" src="https://www.weatherbit.io/static/img/icons/{}.png">
    </body>
    </html>
    """.format(weather['today_temp'], location.name, location.state, weather['iCode'])
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, toEmail, msg.as_string())

def getSubject(weather):
    code = weather['condition']
    diff = weather['today_temp'] - weather['tomorrow_temp']
    sun = code >= 800 and code <= 803
    rain = code >= 200 and code <= 623 or weather['precip'] > 0

    if diff >= 5 or sun: return 'It is nice out! Enjoy a discount on us.'
    if diff <= -5 or rain: return 'Not so nice out? That is okay, enjoy a discount on us.'
    return 'Enjoy a discount on us'

