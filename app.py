from flask import Flask , request , jsonify
import requests
from rasa.cli.utils import print_success
from rasa.nlu.model import Interpreter
from rasa.nlu.utils import json_to_string
rasa_model_path = "./nlu"
interpreter = Interpreter.load(rasa_model_path)
responses={'greet':'Hey! How are you?','goodbye':'Bye','mood_great':'Great, carry on!','mood_unhappy':'Here is something to cheer you up','bot_challenge':'I am a bot, powered by Rasa.','deny':'Bye','affirm':'Great, carry on!'}
app = Flask(__name__)
@app.route('/',methods=['GET'])
def API():
    a = str(request.args['Query'])
    message = str(a).strip()
    result = interpreter.parse(message)
    answer=result['intent']['name']
    return jsonify(responses[answer])
if __name__ == '__main__':
    app.run(debug=True)
