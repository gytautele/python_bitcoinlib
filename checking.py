import hashlib

from bitcoin.rpc import RawProxy

def swapOrder(data):
        x = ""
        k = len(data)/2
        for i in range(0, k):
                byte = data[2*i] + data[2*i+1]
                x = byte + x
        return x

p = RawProxy()

block_hash = p.getblockhash(605730)

block = p.getblock(block_hash)

header = (swapOrder(block["versionHex"]) + swapOrder(block["previousblockhash"]) + swapOrder(block["merkleroot"]) + swapOrder('{:08x}'.format(block["time"])) + swapOrder(block["bits"]) + swapOrder('{:08x$

header_bin = header.decode('hex')

check = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

print("Patikrintas hashas: ")
print check[::-1].encode('hex_codec')
print("Esamas hashas: ")
print block['hash']







