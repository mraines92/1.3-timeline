
from flask import Flask
from flask import request

app = Flask(__name__)


input = request.args.get('one')
print(input)

# open file for reading, 'r'
# file is saved to variable
index_file = open('index.html', 'r')
# read contents of the file
my_html = index_file.read()

if input:
    # add use input back into the html
    my_html = my_html.replace("{{left}}", input)

# close the file out when you're done
index_file.close()

return my_html
