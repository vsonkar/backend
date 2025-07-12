from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    name = data.get('name')
    age = data.get('age')
    return jsonify({"message": f"Hello {name}, age {age} received successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
