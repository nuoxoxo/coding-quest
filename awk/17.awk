BEGIN {
    INFILE = "1724cf8567eb02c3d384b21a63f588c5fd0b87a65c03ea4534a3fbf47e9d7207ac2b3f409a570847d18fbf585670f58002394a99fd0afa3ae482e60f42e1eb24172c82ade8923eb2488702c2beb11ca5eb287aace8fe8b2648050c8423efd6236734c7eb0acfd0660861f4d3a5019bd1a7ac2b387aa2d724c421e9a860940f582633807bf4afe8923e85c3d12362087a36f5d397aace427924611f5970fae9cbdfa80632845bd6429cbd6529d71940413dfff"
}

NR == FNR {
    D[$2] = $1
    next
}

END {

    bstr = hex_to_bin( INFILE )
    print bstr
    l = 1
    res = ""
    while (l <= length(bstr) - 3) {
        r = l + 4
        char = substr(bstr, l, 4)
        print "chr/",char
        if ( ! (char in D)) {
            r++
            char = substr(bstr, l, r - l)# + 1)
        }
        print " chr/",char
        if ( ! (char in D)) {
            r += 2
            char = substr(bstr, l, r - l)# + 1)
        }
        print "  chr/",char
        if ( ! (char in D)) {
            print "    break@/",char
            break
        }
        res = res D[char]
        l = r
    }
    print res
}

function hex_to_bin(hex) {

    split("0 1 2 3 4 5 6 7 8 9 a b c d e f", charset, " ")
    res = ""
    for (i = 1; i <= length(hex); i++) {
        char = substr(hex, i, 1)
        for (j = 1; j <= 16; j++) {
            if (char == charset[j]) {
                idx = j - 1
                break
            }
        }
        for (j = 3; j >= 0; j--) {
            res = res sprintf("%01d", int(idx / 2^j) >= 1)
            idx = idx % 2^j
        }
    }
    return res
}

