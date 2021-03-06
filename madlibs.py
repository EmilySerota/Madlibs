"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    person = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=person,
                           compliment=compliment)

@app.route('/game') #directs to /game after it's exicuted. Connected with compl.html file by the same path.(/game)
def show_madlib_form():

    answer = request.args.get("answer")#taking an answer from compliment.html

    if answer == 'no':
        return render_template("goodbye.html", answer=answer)# if no, got to ...html
    else:
        return render_template("game.html", answer=answer)

@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")

    name = request.args.get("name")

    noun = request.args.get("noun")

    adjective = request.args.get("adjective")

    return render_template("madlib.html",
                           color=color,
                           name=name,
                           noun=noun,
                           adjective=adjective)

# @app.route('/goodbye')
# def say_goodbye():
#     if answer ==

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
