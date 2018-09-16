from flask import Flask, request, jsonify
from brand import detect_brand

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Works!</h1>'


@app.route('/brand', methods=['GET'])
def brand():
    image_uri = request.args.get('image_uri')
    detected_brand = detect_brand(image_uri)
    return jsonify({'brand': detected_brand})


if __name__ == '__main__':
    app.run()
