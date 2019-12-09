from bitcoin.rpc import RawProxy

p = RawProxy()

tx_value = 0
# Retrieve the raw transaction by ID
ID = input("ID:")

raw_tx = p.getrawtransaction(ID)
# Decode the transaction
decoded_tx = p.decoderawtransaction(raw_tx)
# Iterate through each output in the transaction
for output in decoded_tx['vout']:
    # Add up the value of each output
    tx_value = tx_value + output['value']


tx_value1 = 0;
vin_len = 0;

for output1 in decoded_tx['vin']:
    raw_tx1 = p.getrawtransaction(output1['txid'])
    decoded_tx1 = p.decoderawtransaction(raw_tx1)
    stop = output1['vout']
    tx_value1 = tx_value1 + decoded_tx1['vout'][stop]['value']

print("Tx value 1 :", tx_value1)
print("Tx value : ", tx_value)
print("Fee ", tx_value1 - tx_value  )
