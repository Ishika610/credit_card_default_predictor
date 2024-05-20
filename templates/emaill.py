from flask import Flask, render_template, request
import smtplib
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "honeyguptaa0@gmail.com"
    sender_password = "vyrf smye ktbh kejt"
    recipient_email = "honey.21bcon412@jecrcu.edu.in"

    csv_file_path = request.form['csvfile']

    warning_message = ""
    with open(csv_file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["Predictions"] == "1":
                warning_message += f"User has defaulted\n\n"

    if warning_message:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            subject = "Warning Notification"
            message = f"Subject: {subject}\n\n{warning_message}"
            server.sendmail(sender_email, recipient_email, message)

    return 'Email sent successfully!'


if __name__ == '__main__':
    app.run(debug=True)

