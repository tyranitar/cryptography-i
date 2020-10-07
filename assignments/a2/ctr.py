from sys import path
path.append('..')
from common import strxor, get_blocks, aes_enc

def ctr_enc(key, iv, pt):
    return iv + ctr_dec(key, iv, pt) # Since CTR encryption and decryption both use AES encryption.
# ctr_enc

def ctr_dec(key, iv, ct):
    blocks = get_blocks(ct)
    iv_int = int(iv.encode('hex'), 16)
    # For each block, add i to iv_int, convert the sum to hex code, convert the hex code to string, then xor with the AES encryption.
    return ''.join([strxor(block, aes_enc(key, '{:02x}'.format(iv_int + i).decode('hex'))) for i, block in enumerate(blocks)])
# ctr_dec