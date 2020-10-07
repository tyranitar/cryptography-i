from sys import path
path.append('..')
from common import strxor, get_blocks, aes_enc, aes_dec

def cbc_enc(key, iv, pt):
    blocks = get_blocks(pt, pad=True)
    ret = []
    prev_block = iv
    for block in blocks:
        prev_block = aes_enc(key, strxor(block, prev_block))
        ret.append(prev_block)
    # for
    return iv + ''.join(ret)
# cbc_enc

def cbc_dec(key, iv, ct):
    blocks = get_blocks(ct)
    ret = []
    prev_block = iv
    for block in blocks:
        ret.append(strxor(aes_dec(key, block), prev_block))
        prev_block = block
    # for
    padding = int(ret[-1][-1].encode('hex'), 16)
    return ''.join(ret)[:-padding]
# cbc_dec