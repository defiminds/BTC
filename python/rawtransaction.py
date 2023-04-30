import json
import requests
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Connect to the Bitcoin node with RPC access
rpc_user = "YOUR_RPC_USERNAME"
rpc_password = "YOUR_RPC_PASSWORD"
rpc_port = "YOUR_RPC_PORT"
rpc_url = "http://%s:%s@127.0.0.1:%s" % (rpc_user, rpc_password, rpc_port)
rpc_connection = AuthServiceProxy(rpc_url)

# Specify the transaction inputs, outputs, and fees
inputs = [{"txid": "0000000000000000000000000000000000000000000000000000000000000000", "vout": 0}]
outputs = [{"address": "ADDRESS_1", "amount": 100000000}, {"address": "ADDRESS_2", "amount": 50000000}]
fees = 10000

# Create the raw transaction
tx_inputs = []
for input in inputs:
    tx_inputs.append({"txid": input["txid"], "vout": input["vout"]})
tx_outputs = {}
for i, output in enumerate(outputs):
    tx_outputs[output["address"]] = output["amount"]
raw_tx = rpc_connection.createrawtransaction(tx_inputs, tx_outputs)
signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)

# Save the raw transaction as a file
with open("raw_tx.json", "w") as f:
    json.dump(signed_tx, f)

print("Raw transaction saved to raw_tx.json")
