
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='email',
    subject='Sendgrid API Email Test',
    html_content='<strong>Ths is my first API project using Python and Sendgrid to test automate an email!!</strong>')
try:
    sg = SendGridAPIClient((''))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
