{
    lines[NR] = $0
} END {
    for (i=1;i<length(lines);i++) {
        split(lines[i], p1, " ")
        split(lines[i+1], p2, " ")
        res += int( sqrt( \
            (abs(p1[1] - p2[1]))**2 + \
            (abs(p1[2] - p2[2]))**2 + \
            (abs(p1[3] - p2[3]))**2)\
        )
    }
    print "res/",res
}
function abs (n) { return n > 0 ? n : -n }
