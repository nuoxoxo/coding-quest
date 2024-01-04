{
    C = 0
    for (c=1;c<=NF;c++) {
        if ($c != "") {
            rows[NR, c] = hex_to_dec($c)
        }
        cols[c,NR] = hex_to_dec($c)
        C++ # C is len(cols) counts to len(last_col) minus 1
    }
    R++ # R is len(rows) counts to len(last row) 
}
END {
    # ~ for g in G
    for (r=1;r<=R - 1;r++) { # so we substract one

        checksum_row = 0
        for (c=1;c<=C;c++) { # no need to -1 for C
            #print "r,c/",r,c,"rows[r,c]/",rows[r,c]," "
            checksum_row += rows[r,c]
        }

        checksum_row %= 256
        #print "checking rows/ l/",checksum_row,"r/",rows[r,c]

        if (checksum_row != rows[r,c]) {
            R_wrong = r
            RR = checksum_row - rows[r,c]
            RR = RR < 0 ? RR+256 : RR
        }
    }
    # ~ for g in zip(*G)
    for (c=1;c<=C;c++) {

        checksum_col = 0
        for (r=1;r<=R - 1;r++) {
            #print "c,r/",c,r,"cols[c,r]/",cols[c,r]," "
            checksum_col += cols[c,r]
        }

        checksum_col %= 256
        #print "checking cols/ l/",checksum_col,"r/",cols[c,r]

        if (checksum_col != cols[c,r]) {
            C_wrong = c
            CC = checksum_col - cols[c,r]
            CC = CC < 0 ? CC+256 : CC
        }
    }
    print "wrong index @", R_wrong,C_wrong
    print "res from row/",((rows[R_wrong,C_wrong] - RR) * rows[R_wrong,C_wrong])
    print "res from col/",((rows[R_wrong,C_wrong] - CC) * rows[R_wrong,C_wrong])
}

function hex_to_dec(hex) {
    dec = 0
    len = length(hex)
    for (i = 1; i <= len; i++) {
        digit = substr(hex, i, 1)
        val = index("0123456789abcdef", tolower(digit)) - 1
        dec = dec * 16 + val
    }
    return dec
}

