from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)


# Creating the login page with conditions.
@app.route('/login/<name>')
def login_page(name):
    admin = ['Godwin', 'Jason', 'Thapelo']
    students = ['Zoe', 'Ronald', 'Brent', 'Anneqah', 'Adam']
    # If an admin logs in they are redirected to the admin page
    if name in admin:
        return redirect(url_for('admin_page', name=name))
    # If a student logs in they are redirected to the student page
    elif name in students:
        return redirect(url_for('student_page', name=name))
    # Anyone else is redirected to the guest page
    else:
        return redirect(url_for('guest_page', name=name))


# Creating the admin page with a welcoming message
@app.route('/admin/<name>')
def admin_page(name):
    return 'Welcome to the Life Choices admin page %s.' % name


# Creating the student page with a welcoming message
@app.route('/student/<name>')
def student_page(name):
    return 'Welcome to the LifeChoices student page %s.' % name


# Creating the guest page with a welcoming message
@app.route('/guest/<name>')
def guest_page(name):
    return 'Welcome to LifeChoices Coding Academy %s! You are on the guest page.' % name


# Creating a payment page with conditions
@app.route('/payment/<float:sal>')
def payment_page(sal):
    # If the user has the specified amount they receive a message on their screen
    if sal >= 10500.50:
        return 'You are wealthy!'
    # If the user has less than the specified amount they are redirected to a loan site
    else:
        return redirect('https://www.sahomeloans.com/')


# Ensures the app can run if everything is correctly coded
if __name__ == '__main__':
    app.debug = True
    app.run()