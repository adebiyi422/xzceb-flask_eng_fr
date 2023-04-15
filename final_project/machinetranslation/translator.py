"""This Python code translates both English and French text""" #docustring, you happy? :)

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

apikey = '6Y60kdEFU821dHb96rUhNENriEDltzXQZXCRh4mmVLUF'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ce09bf24-267b-4655-8367-ee2ebc41993c'
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """This function translates English text to Francois :)""" #functiondocustring
    #write the code here
    translation =language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """This function translates French text to Anglais""" 
    #write the code here
    translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']

    return english_text
