from cbc import cbc_enc, cbc_dec
from ctr import ctr_enc, ctr_dec
from sys import path
path.append('..')
from common import extract_iv

def main():
    cbc_key = '140b41b22a29beb4061bda66b6747e14'
    ctr_key = '36f18357be4dbd77f050515c73fcf9f2'
    cbc_ct1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
    cbc_ct2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
    ctr_ct1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
    ctr_ct2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
    cbc_key = cbc_key.decode('hex')
    ctr_key = ctr_key.decode('hex')
    cbc_ct1 = cbc_ct1.decode('hex')
    cbc_ct2 = cbc_ct2.decode('hex')
    ctr_ct1 = ctr_ct1.decode('hex')
    ctr_ct2 = ctr_ct2.decode('hex')
    # CBC.
    cbc_iv1, cbc_ct1_cln = extract_iv(cbc_ct1)
    cbc_pt1 = cbc_dec(cbc_key, cbc_iv1, cbc_ct1_cln)
    assert(cbc_enc(cbc_key, cbc_iv1, cbc_pt1) == cbc_ct1)
    print cbc_pt1 # "Basic CBC mode encryption needs padding."
    cbc_iv2, cbc_ct2_cln = extract_iv(cbc_ct2)
    cbc_pt2 = cbc_dec(cbc_key, cbc_iv2, cbc_ct2_cln)
    assert(cbc_enc(cbc_key, cbc_iv2, cbc_pt2) == cbc_ct2)
    print cbc_pt2 # "Our implementation uses rand. IV"
    # CTR.
    ctr_iv1, ctr_ct1_cln = extract_iv(ctr_ct1)
    ctr_pt1 = ctr_dec(ctr_key, ctr_iv1, ctr_ct1_cln)
    assert(ctr_enc(ctr_key, ctr_iv1, ctr_pt1) == ctr_ct1)
    print ctr_pt1 # "CTR mode lets you build a stream cipher from a block cipher."
    ctr_iv2, ctr_ct2_cln = extract_iv(ctr_ct2)
    ctr_pt2 = ctr_dec(ctr_key, ctr_iv2, ctr_ct2_cln)
    assert(ctr_enc(ctr_key, ctr_iv2, ctr_pt2) == ctr_ct2)
    print ctr_pt2 # "Always avoid the two time pad!"
# main

if __name__ == '__main__':
    main()
# if