from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/GuessingGame")
def GG():
    message = request.args.get('message')
    return render_template('index.html', message=message)

@app.route('/submit', methods=['POST'])
def submit():
    guess = request.form.get('Guess', '').strip()
    if not guess.isdigit():
        return redirect(url_for('GG', message="Please enter a valid number"))

    randnum = random.randint(1,10)
    print(randnum)
    guessnum = int(guess)
    if randnum == guessnum:
        message= f"Your guess was correct! You guessed {guess} and the random number was {randnum} "
    else:
        message= f"Your guess was wrong:( You guessed {guess} and the random number was {randnum}"
    
    return redirect(url_for('GG', message=message))

if __name__ == "__main__":
    app.run(debug=True)
