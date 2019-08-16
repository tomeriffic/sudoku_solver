from flask import Flask, request, jsonify


app = Flask(__name__) 






def main():
    return True


@app.route('/validate', methods=["POST"])
def validate_api():
    main()



if __name__ == "__main__":
    app.run(host="0.0.0.0")