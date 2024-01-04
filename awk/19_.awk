BEGIN {
    epar_cnt = 0
    epar_sum = 0
}

{
    b = $0
    bins = ""
    n = b
    while (n > 0) {
        bins = n % 2 bins
        n = int(n / 2)
    }
    # prefix missing 0 to form 16-bit binstr:
    while (length(bins) != 16) {
        bins = "0" bins
    }
    temp = bins
    ones = gsub(/1/, "", temp)
    if (ones % 2 == 0) {
        result = "0" substr(bins,2)
        epar[b] = bin_to_dec( result )
        epar_sum += bin_to_dec( result )
        epar_cnt++
    }
}

END {
    if (epar_cnt < 1) {
        print "interesting/"
    }

    res = int(epar_sum / epar_cnt + 0.5)
    print "res/",res

    for (ee in epar) {
        print "ee/",ee,"[]/",epar[ee]
    }

}

function bin_to_dec(binstr) {
    dec = 0
    for (n = 1; n <= length(binstr); n++) {
        char = substr(binstr, n, 1)
        dec = dec * 2 + char
    }
    return dec
}
