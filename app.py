from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from nonono import MY_SECRET_KEY
from forms import convertCurrency

app = Flask(__name__)

# Configuration for Flask app
app.config['SECRET_KEY'] = MY_SECRET_KEY
debug = DebugToolbarExtension(app)

# ------------------ #
#  Routes and views  #
# ------------------ #

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert_currency():
    """ Convert one currency to another """

    form = convertCurrency()
    if form.validate_on_submit():
        amount = form.amount.data
        from_currency = form.from_currency.data
        to_currency = form.to_currency.data
        
        # Here you would typically call a function to perform the conversion
        print(f'Converting {amount} from {from_currency} to {to_currency}')

        # For now, we will just flash a message and redirect
        flash(f'Converted {amount} from {from_currency} to {to_currency}', 'success')
        return redirect('/')

    return render_template('convert.html', form=form)

