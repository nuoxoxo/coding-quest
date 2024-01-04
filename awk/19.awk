{
    B[NR] = $0
}
END {
    epar_count = 0
    epar_sum = 0
    for (i = 1; i <= length(B); i++) {
        b = B[i]
        print b,i
        #bins = sprintf("%016s", b)  
        #bins = sprintf("%016s", gsub(/^0b/, "", b))


        bins = ""
        temp = b
        while (temp > 0) {
            bins = temp % 2 bins
            temp = int(temp / 2)
        }

        print " before/ ",length(bins),bins
        while (length(bins) != 16) {
            bins = "0" bins
        }
        print " after / ",length(bins),bins

        print bins
        ttemp = bins
        ones = gsub(/1/, "", ttemp)
        print ones
        if (ones % 2 == 0) {
            print "ones/",ones,bins
            split(bins, tttemp, "")
            #for (j = 1; j <= length(temp); j++) {
                #printf "%s ", substr(temp, j, 1)
            #}
            #ttttemp[1] = 0
            #result = ""
            #for (j = 1; j <= length(ttttemp); j++) {
                #result = result ttttemp[j]
            #}
            result = "0" substr(bins,2)
            print "result/",result
            epar[i] = binaryToDecimal( result )#strtonum(temp, 2)
            print "epar/i/",i,epar[i],binaryToDecimal( result )#strtonum(temp, 2)
            epar_sum += binaryToDecimal( result )#strtonum(temp, 2)
            epar_count++
        }
        print ""
    }
    if (epar_count > 0) {
        res = int(epar_sum / epar_count + 0.5)
        print "res/",res
    }
    for (ee in epar) {
        print "ee/",epar[ee]
    }
}
function binaryToDecimal(binary) {
    decimal = 0
    len = length(binary)
    for (n = 1; n <= len; n++) {
        #print "decimal/",decimal
        digit = substr(binary, n, 1)
        decimal = decimal * 2 + digit
    }
    return decimal
}
