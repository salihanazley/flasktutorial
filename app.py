from flask import Flask, url_for,redirect, request, render_template


# Flask is a python class, we are going to create an instance of the flask class
# And assign it to a variable
# We can also creating an object of flask class
app = Flask(__name__) # To tell that this program is the main program

# In flask, function are decorated by @app.route
# route is the mapping of url to python function
@app.route("/")
def hello_world():
    return """
    <html>
    <head>
    <h1>
    Welcome to Lazada
    </h1>
    </head>
    <body>
        <h2>Click the link to browse product</h2>
        <a href="/products">Products</a>
    </body>
    </html>
    """

@app.route("/products")
def products():
    return """
    <html>
    <head>
    <h1>
    Products
    </h1>
    </head>
    <body>
        <h2><a href="/products/television">Television</a></h2>
        <ol>
            <li>Television</li>
            <li>Radio</li>
            <li>Speaker</li>
        </ol>
        
    </body>
    </html>
    """
@app.route("/products/television")
def television():
        return """
    <html>
    <head>
    <h1>
    Television
    </h1>
    </head>
    <body>
        <ol>
        <li>Brand: Sony</li>
        <li>Price: RM1455.55</li>
        <li>Warranty: 1 Year</li>
        </ol>
        
    </body>
    </html>
    """

# Passing the argument to our function using url
# URL http://127.0.0.1:5000/greeting/john
# greeting refers to the function john is an argument => greeting("john")
# the route configuration will be /greeting/<name>
@app.route("/greeting/<name>") # <> means variable
def greeting(name): 
    return f"""
    <html>
    <head>
    <h1>
    Hello! {name}. Welcome to Lazada Shopping website.
    </h1>
    </head>
    <body>
        <h2>Click the link to browse product</h2>
        <a href="/products">Products</a>
    </body>
    </html>
    """

# the parameters are always string
@app.route("/simpleinterest/<principle>/<period>/<rate>")
@app.route("/simpleinterest/<int:principle>/<int:period>/<int:rate>") #can mention datatype
@app.route("/calcsimpleinterest/<int:principle>/<int:period>/<int:rate>")
@app.route("/simpleinterest/<int:principle>/<int:period>/", defaults={'rate':6}) # optional parameter with default
def simpleInterest(principle, period, rate):
     interest = (principle * period * rate) / 100
     return f"""
        <html>
        <head>
            <a href="/">Home</a>
            <h1>Interest Calculator</h1>
        </head>
        <body>
            <table>
                <tr>
                    <td>
                        Principle:
                    </td>
                    <td>
                        {principle}
                    </td>
                </tr>
                <tr>
                    <td>
                        Period
                    </td>
                    <td>
                        {period}
                    </td>
                </tr>
                <tr>
                    <td>
                        Rate:
                    </td>
                    <td>
                        {rate}
                    </td>
                </tr>
                <tr>
                    <td>
                        Interest Amount:
                    </td>
                    <td>
                        {interest}
                    </td>
                </tr>
                <tr>
                    <td>
                        Total Amount to be paid:
                    </td>
                    <td>
                        {interest + principle}
                    </td>
                </tr>
            </table>
        </body>
        </html>
    """
@app.route('/demoredirect')
def demoredirect():
    return redirect(url_for('greeting', name="Peter"))

@app.route('/login')
def login():
    return """
            <html>
        <head>
            <title>
                Login
            </title>
        </head>
        <body>
            <form action="/verifylogin" method="post">
                <tr>
                    <td>
                        Username:
                    </td>
                    <td>
                        <input type="text" name="emailaddress" id="emailaddress"/>
                    </td>
                </tr>
                    <td>
                        Password:
                    </td>
                    <td>
                        <input type="password" name="password" id="password"/>
                    </td>
                <tr>
                    <td>
                        <input type="submit" name="submitbtn" value="Login"/>
                    </td>
                </tr>
            </form>
        </body>
        </html>
"""
@app.post('/verifylogin')
def verifylogin():
    emailaddress = request.form['emailaddress']
    password = request.form['password']
    if (emailaddress == "admin@gmail.com" and password == "pwd123"):
        return f"""
            <html>
                <head>
                    <title>
                        Verify Login
                    </title>
                </head>
                <body>
                    <h2> Verify Login </h2>
                    <h6> Email Address: {request.form['emailaddress']} </h6>
                    <h6> Password: {request.form['password']} </h6>

                </body>
            </html>
            """
    else:
         return redirect(url_for('login'))

@app.route("/goodlookinglogin")
def goodLookingLogin():
    return render_template('login.html')