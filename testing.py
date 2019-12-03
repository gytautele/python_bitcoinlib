from bitcoin.rpc import RawProxy

p = RawProxy()

txid = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"

raw_tx = p.getrawtransaction(txid)

decoded_tx = p.decoderawtransaction(raw_tx)

in_tx_id = []
in_id = []

for output in decoded_tx['vin']:
        in_tx_id.append(output['txid'])
        in_id.append(output['vout'])

sent = []
k = 0

for out in in_tx_id:
        raw_tx = p.getrawtransaction(out)
        decoded_tx = p.decoderawtransaction(raw_tx)
        sent.append(decoded_tx['vout'][in_id[k]]['value'])
        k += 1

got = []

raw_tx = p.getrawtransaction(txid)

decoded_tx = p.decoderawtransaction(raw_tx)

for output in decoded_tx['vout']:
        got.append(output['value'])

print("Issiunte:")

for a in sent:
        print(a)

print("Gavo: ")

for a in got:
        print(a)

print("Mokestis: ")

a = 0
for b in sent:
        a += b

for b in got:
        a -= b

print(a)


