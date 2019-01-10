
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():


input = request.args.get('one')
print(input)

if input = 'one'

# open file for reading, 'r'
# file is saved to variable
index_file = open('index.html', 'r')
# read contents of the file
my_html = index_file.read()

my_value = ""

if input:
    # add use input back into the html
    my_html = my_html.replace("{{left}}", input)

# close the file out when you're done
index_file.close()

print('my_html')