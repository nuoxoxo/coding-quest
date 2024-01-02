{
    split($0, set, " ")
    qty = set[2]
    key = set[3]
    print qty,key
    D[key] = key in D ? D[key] + qty : qty
} END {
    res = 1
    for (key in D) {
        res *= D[key] % 100
    }
    print "res/",res
}
