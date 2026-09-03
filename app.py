from flask import Flask, render_template, request

app = Flask(__name__)
balance = 10000
transactions = []

@app.route("/", methods=["GET", "POST"])
def home():
    global balance
    message = ""
    if request.method == "POST":
        action = request.form["action"]
        amount = int(request.form["amount"])

        if action == "deposit":
            balance += amount
            transactions.append(f"+ ₹{amount} Deposit")
            message = f"₹{amount} deposited successfully."

        elif action == "withdraw":
            if amount > balance:
                message = "Insufficient balance."
            else:
                balance -= amount
                transactions.append(f"- ₹{amount} Withdrawal")
                message = f"₹{amount} withdrawn successfully."

    return render_template("index.html", balance=balance, transactions=transactions, message=message)

if __name__ == "__main__":
    app.run(debug=True)