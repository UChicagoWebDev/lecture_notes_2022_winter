from flask import Flask, request, jsonify
app = Flask(__name__)

verses = [
    "Row row row your boat",
    "Gently down the stream",
    "Merrily merrily merrily merrily",
    "Life is but a dream"
]

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # if request.method == 'POST': # Do some stuff
    return jsonify(verses)

# curl -d '{"verse":"Row row your canoe"}' -H 'Content-Type: application/json' localhost:5000
