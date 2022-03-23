# coding=utf-8
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import Flask


authenticator = IAMAuthenticator('Z7MXBCtNoUIZ3kSuAZdkRlWIFjU6kKmPyeoEfUBeO-VW')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/647b0c08-1ce1-4f79-93de-4f429afd49c5')





translation = language_translator.translate(
    text=input('Hello, type and I will translate it french?  '),
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=0, ensure_ascii=False))

  
translation = language_translator.translate(
    text=input('Bonjour, type et je vais le traduire en anglais?  '),
    model_id='fr-en').get_result()
print(json.dumps(translation, indent=0, ensure_ascii=False))




app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"