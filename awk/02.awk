BEGIN {
    line = "12 48 30 95 15 55 97"
    D [3] = 1
    D [4] = 10
    D [5] = 100
    D [6] = 1000
    res = 0
}
{
    wins = 0
    for (i = 1; i <= NF; i++){
        if ( index(line, $i) > 0 ) {
            wins++
        }
    }
    res += D[wins]
    if (D[wins] != 0) {
        print "line/" $0 " win/" wins " D[wins]/" D[wins] 
    }
}
END {
    print res
}
