{
    qty = $2
    key = $3
    D[key] = key in D ? D[key] + qty : qty
    print qty,key
} END {
    res=1
    for (key in D)
        res *= D[key] % 100
    print "res/",res
}
