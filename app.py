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

@app.route("/SortingHat")
def SH():
    message = request.args.get('message')
    return render_template('hat.html', message = message)

@app.route('/submit', methods=['POST'])
def submit():
    guess = request.form.get('Guess', '').strip()
    if not guess.isdigit():
        return redirect(url_for('GG', message="Please enter a valid number"))

    randnum = random.randint(1,10)
    print(randnum)
    guessnum = int(guess)
    print(guessnum)
    if randnum == guessnum:
        message= f"Your guess was correct! You guessed {guess} and the random number was {randnum} "
    else:
        message= f"Your guess was wrong:( You guessed {guess} and the random number was {randnum}"
    
    return redirect(url_for('GG', message=message))

@app.route('/submitHat', methods =['POST'])
def submitHat():
    q1 = request.form.get('q1', '').strip()
    q2= request.form.get('q2', '').strip()
    q3 = request.form.get('q3', '').strip()

    gryf=0
    sly=0
    huff=0
    rav=0
    print(q1,q2,q3)
    if q1 == "Dawn":
        gryf +=1
        rav+=1
    else:
        huff+=1
        sly+=1
    
    if q2 == "TheGood":
        huff+=2
    elif q2 =="TheGreat":
        sly+=2
    elif q2 == "TheWise":
        rav+=2
    else:
        gryf+=2
    
    if q3 == "TheViolin":
        sly+=4
    elif q3 =="TheTrumpet":
        huff+=4
    elif q3 == "ThePiano":
        rav+=4
    else:
        gryf+=4

    if gryf>sly and gryf>huff and gryf>rav:
        message = "GRYFFINDOR"
    elif sly>gryf and sly>huff and sly>rav:
        message = "SYTHERIN"
    elif huff>sly and huff>gryf and huff>rav:
        message ="HUFFLEPUFF"
    elif rav>sly and rav>gryf and rav>huff:
        message ="RAVENCLAW"

      
    return redirect(url_for('SH', message =message))


if __name__ == "__main__":
    app.run(debug=True)
