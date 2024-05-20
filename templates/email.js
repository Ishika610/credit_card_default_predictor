import smtplib
import csv

smtp_server = "smtp.gmail.com"
smtp_port = 587
# Email of the client
sender_email = "mgpsishika7128@gmail.com"
sender_password = "znowjzrztiwrgswc"
recipient_email = "honeyguptaa0@gmail.com"
csv_file_path = "C:/Users/creditCardDefaulters/Prediction_Output_File/Predictions.csv"
a = 0
# Initialize the warning message
warning_message = ""

with open(csv_file_path, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row["Predictions"] == "1":
            # Append the warning message for each row with prediction value 1
            warning_message += ("user " + str(a) + " has defaulted\n\n")
        a += 1

if warning_message:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        subject = "Warning Notification"
        message = f"Subject: {subject}\n\n{warning_message}"
        server.sendmail(sender_email, recipient_email, message)