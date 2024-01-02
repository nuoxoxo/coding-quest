BEGIN {

    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
    
    # test decoder
    K = "With great power comes great responsibility"
    CS = charset
    EM = "lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(rzfwKXBMd"
    res = Decoder(K, CS, EM)
    assert res == "I could use this to pass secret notes in class!"
    print "decode/",res

    # test encoder
    # 1
    K = "SECRET"
    CS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    M = "WE COME IN PEACE"
    res = Encoder(K, CS, M)
    assert res == "PJ UTGX LF JXFFW"
    print "encode/",res

    # 2
    K = "With great power comes great responsibility"
    CS = charset
    M = "Are you enjoying coding quest?"
    res = Encoder(K, CS, M)
    assert res == "dAyevvMbfHgENFsy:fDqnGddIzfMqm"
    print "encode/",res

    # 3
    K = "With great power comes great responsibility"
    M = "I could use this to pass secret notes in class!"
    res = Encoder(K, charset, M)
    assert res == "lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(rzfwKXBMd"
    print "encode/",res
    print "assert/ all testcases passed!"

}{

    key = "Roads? Where We're Going, We Don't Need Roads."
    res = Decoder(key, charset, $0)
    print "result/",res
}

function Decoder(key, charset, emsg) {

    keyindex = (length(emsg) - 1) % length(key)
    msgindex = length(emsg) - 1
    res = ""

    while (msgindex > -1) {

        msgchar = substr(emsg, msgindex + 1, 1)
        if (index(charset, msgchar) == 0) {
            res = res msgchar
            msgindex = msgindex - 1
            keyindex = (keyindex - 1 + length(key)) % length(key)
            continue
        }
        keychar = substr(key, keyindex + 1, 1)
        keycharoffset = (index(charset, keychar) + 1) % length(charset)
        msgcharindex = index(charset, msgchar)
        nextcharindex = (msgcharindex - keycharoffset + length(charset)) % length(charset)
        nextchar = substr(charset, nextcharindex + 1, 1)
        res = nextchar res
        msgindex = msgindex - 1
        keyindex = (keyindex - 1 + length(key)) % length(key)
    }
    return res
}

function Encoder(key, charset, msg) {

    keyindex = 1
    msgindex = 1
    res = ""

    while (msgindex <= length(msg)) {

        msgchar = substr(msg, msgindex, 1)
        if (index(charset, msgchar) == 0) {
            res = res msgchar
            msgindex = msgindex + 1
            keyindex = (keyindex + 1) % length(key)
            continue
        }
        keychar = substr(key, keyindex, 1)
        keycharoffset = (index(charset, keychar) + 1) % length(charset)
        msgcharindex = index(charset, msgchar)
        nextcharindex = (msgcharindex + keycharoffset) % length(charset)
        res = res substr(charset, nextcharindex + 1, 1)
        keyindex = (keyindex + 1) % length(key)
        msgindex = msgindex + 1
    }
    return res
}

