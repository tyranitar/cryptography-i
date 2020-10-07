from gmpy2 import mpz, powmod

# NOTE: Arguments must be of type mpz.
def dlog(p, g, h, B):
    # h * g ** -x1 == g ** (B * x0)
    g_inv = powmod(g, -1, p)
    g_B = powmod(g, B, p)
    ht = {}
    lhs = h
    i = mpz(0)
    while i < B:
        ht[lhs] = i
        lhs = lhs * g_inv % p
        i += 1
    # while
    rhs = mpz(1)
    i = mpz(0)
    while i < B:
        if rhs in ht:
            return B * i + ht[rhs] # B * x0 + x1
        # if
        rhs = rhs * g_B % p
        i += 1
    # while
# dlog

def main():
    p = mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
    g = mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
    h = mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')
    B = mpz(2 ** 20)
    print dlog(p, g, h, B) # "375374217830"
# main

if __name__ == '__main__':
    main()
# if