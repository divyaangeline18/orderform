from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(subject, body):
    sender_email = "divyathiyagumarriage@gmail.com"
    receiver_email = "divyaangeline18@gmail.com"
    password = "YOUR_APP_PASSWORD"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    pack_size = request.form["pack_size"]
    qty = request.form["qty"]
    name = request.form["customer_name"]
    price = request.form["price"]

    body = (
        f"New Order Details:\n"
        f"Pack Size: {pack_size} gms\n"
        f"Quantity: {qty}\n"
        f"Customer Name: {name}\n"
        f"Price Paid: ₹{price}"
    )

    send_email("New Product Order", body)
    return "Order submitted successfully! You can close this page."

if __name__ == "__main__":
    app.run()
