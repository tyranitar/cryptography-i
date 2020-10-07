from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# xor two strings of different lengths
def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    # if
# strxor

def extract_iv(ct, block_size=16):
    return ct[:block_size], ct[block_size:]
# extract_iv

def get_blocks(text, pad=False, block_size=16):
    blocks = []
    # Each character is a byte.
    i = 0
    end = len(text)
    while i < end:
        blocks.append(text[i:i + block_size])
        i += block_size
    # while
    if pad:
        if len(blocks) == 0 or len(blocks[-1]) == block_size:
            blocks.append(''.join([chr(block_size)] * block_size))
        else:
            remainder = block_size - len(blocks[-1])
            blocks[-1] += ''.join([chr(remainder)] * remainder)
        # if
    # if
    return blocks
# get_blocks

def aes_enc(key, pt):
    return AES.new(key, AES.MODE_ECB).encrypt(pt)
# aes_enc

def aes_dec(key, ct):
    return AES.new(key, AES.MODE_ECB).decrypt(ct)
# aes_dec

def sha_256(text):
    return SHA256.new(text).hexdigest()
# sha_256