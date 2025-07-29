import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import re
# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rowz = db.execute("SELECT symbol, SUM(total), SUM(share), price FROM transactions WHERE transact_id = ? GROUP BY symbol HAVING SUM(total) > 0" , session["user_id"])
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    end_total = db.execute("SELECT SUM(total) FROM transactions WHERE transact_id = ?", session["user_id"])
    total = user_cash[0]["cash"]
    if end_total[0]["SUM(total)"] != None:
        total = user_cash[0]["cash"] + end_total[0]["SUM(total)"]

    return render_template("/index.html", symbols=rowz, usercash=user_cash , total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        pattern ="[.a-zA-Z]"

        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        elif not request.form.get("shares"):
            return apology("missing shares", 400)

        elif lookup(request.form.get("symbol").upper()) == None:
            return apology("symbol not found", 400)

        elif re.search(pattern, request.form.get("shares")):
            return apology("no decimals", 400)

        elif int(request.form.get("shares")) < 0:
            return apology("invalid number", 400)

        user_cash_request = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = user_cash_request[0]["cash"]
        stock_request = lookup(request.form.get("symbol"))
        stock_price = stock_request["price"]
        share_request = request.form.get("shares")

        share_multiply = int(share_request) * stock_price

        if user_cash < share_multiply:
            return apology("not enough cash", 400)

        buy_operation =  user_cash - share_multiply
        db.execute("UPDATE users SET cash = ? WHERE id = ?", buy_operation, session["user_id"])

        db.execute("INSERT INTO transactions (transact_id, symbol, share, price, total) VALUES(?, ?, ?, ?, ?)", session["user_id"], request.form.get("symbol"), int(request.form.get("shares")), stock_price, share_multiply)
        return redirect("/")

    return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rowzsh = db.execute("SELECT symbol, share, price, transacted FROM transactions WHERE transact_id = ?", session["user_id"])

    return render_template("history.html", histories=rowzsh)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        stock_symbol = lookup(request.form.get("symbol").upper())

        if stock_symbol == None:
            return apology("stock not found", 400)

        return render_template("/quoted.html", name = stock_symbol['symbol'], price = stock_symbol['price'])

    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords do not match!", 400)

        name = request.form.get("username")
        if len(db.execute("SELECT * FROM users WHERE username = ?", name)) != 0:
            return apology("username already exists", 400)

        password = request.form.get("password")
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", name, generate_password_hash(password))

        sql_row = db.execute("SELECT * FROM users WHERE username = ?", name)

        session["user_id"] = sql_row[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
            symbol = request.form.get("symbol")
            if symbol is None:
                return apology("symbol not found", 400)

            rowz = db.execute("SELECT symbol, SUM(total), SUM(share) AS sum, price FROM transactions WHERE transact_id = ? AND symbol = ? GROUP BY symbol HAVING SUM(total) > 0" , session["user_id"], symbol.lower())
            user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            pattern = "[@/.a-zA-Z]"
            lookz = lookup(request.form.get("symbol"))

            if lookz is None:
                return apology("symbol not found", 400)


            if not request.form.get("shares"):
                return apology("Input a number", 400)

            elif re.search(pattern, request.form.get("shares")):
                return apology("Invalid number", 403)

            elif int(request.form.get("shares")) <= 0:
                return apology("too little shares", 403)

            user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            total_sell = lookz["price"] * int(request.form.get("shares"))
            sell_operation = user_cash[0]["cash"] + total_sell

            db.execute("UPDATE users SET cash = ? WHERE id = ?", sell_operation, session["user_id"])
            db.execute("INSERT INTO transactions (transact_id, symbol, share, price, total) VALUES(?, ?, ?, ?, ?)", session["user_id"], symbol, -(int(request.form.get("shares"))), rowz[0]["price"], -(total_sell))

            return redirect("/")

    else:
        show_stock = db.execute("SELECT symbol, SUM(total), SUM(share), price FROM transactions WHERE transact_id = ? GROUP BY symbol HAVING SUM(total) > 0" , session["user_id"])

        return render_template("sell.html", stocks=show_stock)


@app.route("/changepass", methods=["GET", "POST"])
@login_required
def changepass():
    """Sell shares of stock"""
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        password = request.form.get("new_password")

        if not request.form.get("old_password") or not request.form.get("new_password"):
            return apology("enter passwords", 403)
        elif not check_password_hash(rows[0]["hash"], request.form.get("old_password")):
            return apology("invalid old password", 403)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(password), session["user_id"])

        return redirect("/logout")

    else:
        return render_template("changepass.html")
