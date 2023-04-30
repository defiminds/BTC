import json
import requests

# Define the BlockCypher API endpoint
api_endpoint = "https://api.blockcypher.com/v1/btc/test3/txs/new"

# Specify the transaction inputs, outputs, and fees
inputs = [{"txid": "0000000000000000000000000000000000000000000000000000000000000000", "vout": 0}]
outputs = [{"address": "ADDRESS_1", "value": 100000}, {"address": "ADDRESS_2", "value": 50000}]
fees = 10000

# Create the raw transaction request
raw_tx_request = {
    "inputs": inputs,
    "outputs": outputs,
    "fees": fees
}

# Send the raw transaction request to BlockCypher
response = requests.post(api_endpoint, json=raw_tx_request)

# Get the partially-signed transaction and private key
response_json = response.json()
unsigned_tx = response_json["tosign"][0]
private_key = "YOUR_PRIVATE_KEY"

# Sign the transaction with the private key
signed_tx_request = {
    "tx": unsigned_tx,
    "keys": [private_key]
}
response = requests.post(api_endpoint + "/sign", json=signed_tx_request)

# Get the fully-signed transaction
response_json = response.json()
signed_tx = response_json["tx"]

# Save the partially-signed transaction as a file
with open("partially_signed_tx.json", "w") as f:
    json.dump({"unsigned_tx": unsigned_tx, "signed_tx": signed_tx}, f)

print("Partially-signed transaction saved to partially_signed_tx.json")
