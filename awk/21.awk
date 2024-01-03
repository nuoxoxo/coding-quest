{

    p = $0
    checksum = 0
    checksum2 = 0
    if (substr(p, 1, 4) != "5555") {
        next
    }

    idx = 4 + 8 + 1
    ship_hex = substr(p, 5, idx - 5)
    ship = hex_to_dec(ship_hex)

    idx += 2
    order_hex = substr(p, 5, idx - 5)
    order = hex_to_dec(order_hex)

    idx += 2
    if (idx != 16+1) {
        print "err/idx/",idx
        next
    }

    checksum_hex = substr(p, 5, idx - 5)
    checksum = hex_to_dec(checksum_hex)

    #print "check1/hex/",checksum_hex,"check1/",checksum

    msg = substr(p, idx)
    if (length(msg) != 192 / 4) {
        print "err/len/",length( msg )
        next
    }

    #print "msg/",msg

    decoded = ""
    for (j = 1; j <= length(msg); j += 2) {
        char = hex_to_dec(substr(msg, j, 2))
        checksum2 += char
        decoded = decoded sprintf("%c", char)
        #print "in loop/:char/",char," decoded/",decoded
    }

    #print "decoded/",decoded
    #print "check1/",checksum,"%256/", checksum % 256
    #print "check2/",checksum2,"%256/",checksum2 % 256

    if (checksum % 256 != checksum2 % 256) {
        next
    }

    inbox[order] = decoded

} END {

    #print "len/inbox/",length( inbox )

    for (order in inbox) {
        res = res inbox[order]
        print "[?]sorted/ order/",order,"[order]/",inbox[ order ]
    }

    print "res/",res

}

function hex_to_dec(hex) {

    res = 0
    len = length(hex)

    for (i = 1; i <= len; i++) {
        digit = substr(hex, i, 1)
        res *= 16
        res += hex_digit_to_dec(digit)
        #print "hex2dec/",res,"digit/",digit
    }
    return res
}

function hex_digit_to_dec (char) {

    charset = "0123456789abcdef"
    return index(charset, char) - 1
}

