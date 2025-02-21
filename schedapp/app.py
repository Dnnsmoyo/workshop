# Importing our modules

from flask import Flask
from flask import Flask, render_template
import schedule
import time
import os

# Import SENGRID CLIENT and Mail

from sendgrid import SendGridAPIClient
from sendgridhelpers.mail import Mail


@app.route("/workshop/", methods=['POST'])
def workshop():    
   sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
   from_email = Email("hr@gmail.com")
   to_email = To("sales@gmail.com","accounts@gmail.com","marketing@gmail.com")
   subject = "Workshop reminder"
   content = Content("text/plain", "Workshop around the corner!" )
   mail = Mail(from_email, to_email, subject, content)
   response = sg.client.mail.send.post(request_body=mail.get())
   print(response.status_code)
   print(response.body)
   print(response.headers)
   return render("Success")

schedule.every().monday.do(workshop)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
