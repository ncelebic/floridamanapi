from flask import Flask, render_template, request
from dateutil.parser import parse
from googlesearch import search

app = Flask(__name__)

site_blacklist = [
    'floridamanbirthdaychallenge.com',
    'reddit.com'
]

blacklist_string = ""

for site in site_blacklist:
    blacklist_string += "-site:%s " % site


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/get')
def getfloridaman():
    rawdate = request.args.get('date', type=str)
    parsed_date = parse(rawdate)
    actualdate = parsed_date.strftime('%B %d')
    search_string = "Florida Man %s %s" % (actualdate, blacklist_string)
    print(search_string)
    for result in search(search_string, num=1, stop=1):
        url = result
        break
    return url


if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
