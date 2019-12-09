
from bitcoin.rpc import RawProxy
import sys
import hashlib
def myFunction(hex):
    string = "";

    ilgis = range(0,int(len(hex) - 1),2)

    for x in ilgis:
        a = hex[x]
        b = hex[x+1]
        a = str(a)
        b = str(b)
        string = string + b + a;

    string = string[::-1]
    return string;


p = RawProxy()

# The block height where Alice's transaction was recorded
blockheight = 125552

# Get the block hash of block with height 277316
blockhash = p.getblockhash(blockheight)

# Retrieve the block by its hash
block = p.getblock(blockhash)
version = block['versionHex']
version =  myFunction(version)
hashPrevBlock = block['previousblockhash']
hashPrevBlock = myFunction(hashPrevBlock)
hashMerkleRoot = block['merkleroot']
hashMerkleRoot = myFunction(hashMerkleRoot)
time = hex(block['time'])
time = time.replace('0x', '')
time = myFunction(time)
bits = block['bits']
bits = myFunction(bits)
nonce = hex(block['nonce'])
nonce = nonce.replace('0x', '')
nonce = myFunction(nonce)

header_hex = (version + hashPrevBlock + hashMerkleRoot + time + bits + nonce)

header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash.encode('hex_codec')
print(hash[::-1].encode('hex_codec'))
