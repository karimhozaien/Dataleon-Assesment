# Dataleon-Assesment

# AzureCLU - Python Wrapper for Azure Cognitive Language Understanding Service

This Python module provides a convenient interface to interact with the Azure Cognitive Language Understanding (CLU) service, allowing users to predict intents from textual queries.

## Installation

To use this module, ensure you have Python 3.x installed on your system. You can install the required dependencies using pip:

```bash
pip install requests pytest
```

## Usage

First, import the `AzureCLU` class from the module:

```python
from azure_clu import AzureCLU
```

Create an instance of the `AzureCLU` class by providing the endpoint URL and subscription key:

```python
subscription_key = 'your_subscription_key'
endpoint = 'your_endpoint_url'
azure_clu = AzureCLU(endpoint, subscription_key)
```

You can now use the `predict_intent` method to predict the intent of a given query:

```python
query = 'How to make lasagna?'
intent = azure_clu.predict_intent(query)
print(intent)  # Output: 'getRecipe'
```

## Example

```python
import pytest
from azure_clu import AzureCLU

# Set up fixture for AzureCLU instance
@pytest.fixture
def azure_clu():
    subscription_key = 'your_subscription_key'
    endpoint = 'your_endpoint_url'
    return AzureCLU(endpoint, subscription_key)

# Test case to predict intent for a valid query
def test_predict_intent(azure_clu):
    query = 'How to make lasagna?'
    intent = azure_clu.predict_intent(query)
    assert intent == 'getRecipe'

# Test case to ensure proper handling of invalid query
def test_predict_intent_invalid_query(azure_clu):
    query = ''
    with pytest.raises(requests.HTTPError):
        azure_clu.predict_intent(query)
```

## Note

- Ensure that you replace `'your_subscription_key'` and `'your_endpoint_url'` with your actual Azure subscription key and endpoint URL respectively.
- The `predict_intent` method expects a non-empty query. Make sure to provide valid input to get accurate intent predictions.
- Handle exceptions appropriately, especially when dealing with network requests using `requests`.

## License

This module is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
