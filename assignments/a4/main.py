from padding_oracle import PaddingOracle
from random import randint
from sys import path
path.append('..')
from common import get_blocks, strxor

def decrypt(ct, po):
    # The head will be 15 bytes at most, since at least 1 byte is for the guess.
    random_block = ''.join([chr(randint(0, 255)) for i in xrange(15)])
    blocks = get_blocks(ct)
    guesses = []
    current = 0
    total = len(ct) - 16 # Subtract IV length.
    print 'progress: [' + ' ' * total + ']\r',
    for b in xrange(len(blocks) - 1):
        block0 = blocks[b]
        block1 = blocks[b + 1]
        guess = '' # The running guess.
        for i in xrange(16):
            guess_xored = strxor(guess, chr(i + 1) * i) # XOR the running guess by the correct pad.
            # Head needs to be random to prevent inadvertently providing the correct pad.
            # This is especially true for the last block, whose plaintext will have pads.
            # Note that if the first guess is faulty, so are all the subsequent guesses.
            head = random_block[:15 - i]
            head = head.encode('hex')
            tail = strxor(block0[16 - i:], guess_xored) + block1
            tail = tail.encode('hex')
            c = ord(block0[15 - i]) # The character we're modifying.
            for g in xrange(256):
                q = chr(c ^ g ^ (i + 1))
                q = q.encode('hex')
                query = head + q + tail
                if po.query(query):
                    guess = chr(g) + guess
                    current += 1
                    print 'progress: [' + '#' * current + ' ' * (total - current) + ']\r',
                    break
                # if
                if g == 255:
                    print ''
                    raise Exception('none of the guesses were correct')
                # if
            # for
        # for
        guesses.append(guess)
    # for
    print ''
    return ''.join(guesses)
# decrypt

def main():
    ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
    ct = ct.decode('hex')
    po = PaddingOracle()
    print decrypt(ct, po) # "The Magic Words are Squeamish Ossifrage"
# main

if __name__ == '__main__':
    main()
# if