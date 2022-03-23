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


def english_to_french(text1):
    """
    This function translates english to french
    """

    frenchtranslation = language_translator.translate(
                                text=text1,
                                model_id='en-fr'
                            ).get_result()

    return frenchtranslation.get('translations')[0].get('translation')

def french_to_english(text1):
    """
    This function translates french to english
    """

    englishtranslation = language_translator.translate(
                                text=text1, model_id='fr-en'
                            ).get_result()

    return englishtranslation.get('translations')[0].get('translation')