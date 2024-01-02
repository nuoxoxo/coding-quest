{
    Q [NR] = $1
    sum += $1
    if ( NR >= 60 ) {
        if ( NR != 60 ) {
            sum -= Q[ NR - 60 ]
        }
        avg = sum / 60
        if ( avg > 1600 || avg < 1500 ) {
            count++
        }
    }
} END {
    print "res/" count
}
