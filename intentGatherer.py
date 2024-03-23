import requests
import pytest

class AzureCLU:
    def __init__(self, endpoint, subscription_key):
        self.endpoint = endpoint
        self.subscription_key = subscription_key

    def predict_intent(self, query):
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }
        params = {
            'query': query,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
        }
        response = requests.get(self.endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()['prediction']['topIntent']

# Example test cases
@pytest.fixture
def azure_clu():
    subscription_key = '9415d33f563d4171b73c572d318da3a7'
    endpoint = 'https://conversationallanguageunderstanding.cognitiveservices.azure.com/'
    return AzureCLU(endpoint, subscription_key)

def test_predict_intent(azure_clu):
    query = 'How to make lasagna?'
    intent = azure_clu.predict_intent(query)
    assert intent == 'getRecipe'

def test_predict_intent_invalid_query(azure_clu):
    query = ''
    with pytest.raises(requests.HTTPError):
        azure_clu.predict_intent(query)