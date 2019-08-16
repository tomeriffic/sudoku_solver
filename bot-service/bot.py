from flask import Flask, request, jsonify


app = Flask(__name__) 


#STATES
ASK_NAME = 0
GREETING = 1
FIRST_ROUND_QUESTIONING = 2


def greeting(message_received):
    if "hey" in message_received:
        return True
    if "hello" in message_received:
        return True
    if "ite" in message_received:
        return True


def main():
    state = request.json["state"]
    message_received = request.json["message"].lower()

    is_greeting(message_received)


    return True


@app.route('/bot', methods=["POST"])
def bot_api():
    main()



if __name__ == "__main__":
    app.run(host="0.0.0.0")