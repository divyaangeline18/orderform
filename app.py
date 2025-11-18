from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FORMSPREE_URL = "https://formspree.io/f/your_form_id"   # <-- paste your Formspree link here

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    product_size = request.form.get("product_size")
    quantity = request.form.get("quantity")
    name = request.form.get("name")
    price = request.form.get("price")

    data = {
        "Product Size": product_size,
        "Quantity": quantity,
        "Name": name,
        "Price Paid": price
    }

    # Send to Formspree
    requests.post(FORMSPREE_URL, data=data)

    return "Order Submitted Successfully!"
