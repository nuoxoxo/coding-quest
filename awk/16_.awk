{
    C = 0
    for (c=1;c<=NF;c++) {
        if ($c != "") {
            rows[NR, c] = hex_to_dec($c)
        }
        cols[c,NR] = hex_to_dec($c)
        C++
    }
    R++
}
END {
    for (r=1;r<=R - 1;r++) {
        checksum_row = 0
        for (c=1;c<=C;c++) {
            checksum_row += rows[r,c]
        }
        checksum_row %= 256
        if (checksum_row != rows[r,c]) {
            R_wrong = r
            RR = checksum_row - rows[r,c]
            RR = RR < 0 ? RR+256 : RR
        }
    }
    for (c=1;c<=C;c++) {
        checksum_col = 0
        for (r=1;r<=R - 1;r++) {
            checksum_col += cols[c,r]
        }
        checksum_col %= 256
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
    for (i = 1; i <= length( hex ); i++) {
        digit = substr(hex, i, 1)
        val = index("0123456789abcdef", digit) - 1
        dec = dec * 16 + val
    }
    return dec
}
