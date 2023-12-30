todecode = open(0).read().strip()
charset = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"""
key = """Roads? Where We're Going, We Don't Need Roads."""

"""
offset = key.indexof(char)
'A' -> ( charset.indexof('A') + offset ) % len(charset)
"""

def DEC(key, charset, emsg) -> str:
    # get ending position in key
    keyindex = (len(emsg) - 1) % len(key)
    msgindex = len(emsg) - 1
    res = ''
    while msgindex > -1:
        msgchar = emsg[ msgindex ]
        if msgchar not in charset:
            res += msgchar
            msgindex -= 1
            keyindex = (keyindex - 1 + len(key)) % len(key)
            continue
        # get offset
        keychar = key[ keyindex ]
        keycharoffset = (charset.index(keychar) + 1) % len(charset)
        # move by offset then get the char
        msgcharindex = charset.index(msgchar)
        nextcharindex = (msgcharindex - keycharoffset + len(charset)) % len(charset)
        nextchar = charset[ nextcharindex ]
        res += nextchar
        msgindex -= 1
        keyindex = (keyindex - 1 + len(key)) % len(key)
    res = ''.join(reversed(res))
    print('Decoder/',res)
    return res

res=DEC(key, charset, todecode)

def ENC(key, charset, msg) -> str:
    keyindex = 0
    msgindex = 0
    res = ''
    while msgindex < len(msg):
        msgchar = msg[ msgindex ]
        if msgchar not in charset:
            res += msgchar
            msgindex += 1
            keyindex = (keyindex+1) % len(key)
            continue
        # get offset
        keychar = key[ keyindex ]
        keycharoffset = (charset.index(keychar) + 1) % len(charset)
        # move by offset then get the char
        msgcharindex = charset.index(msgchar)
        nextcharindex = (msgcharindex + keycharoffset) % len(charset)
        res += charset[ nextcharindex ]
        # wrap around curr index in key
        keyindex = (keyindex+1) % len(key)
        msgindex += 1
    print('Encoder/',res)
    return res

K='With great power comes great responsibility'
CS='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! \'()'
EM='lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(rzfwKXBMd'
res=DEC(K, CS, EM)
assert res == 'I could use this to pass secret notes in class!'

K='SECRET'
CS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
M='WE COME IN PEACE'
res=ENC(K, CS, M)
assert res == 'PJ UTGX LF JXFFW'

K='With great power comes great responsibility'
CS='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! \'()'
M='Are you enjoying coding quest?'
res=ENC(K, CS, M)
assert res == 'dAyevvMbfHgENFsy:fDqnGddIzfMqm'

K='With great power comes great responsibility'
CS='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! \'()'
M='I could use this to pass secret notes in class!'
res=ENC(K, CS, M)
assert res == 'lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(rzfwKXBMd'



