function abs (n) { return n > 0 ? n : -n }

{
    lines[NR] = $0
} END {
    for (i=1;i<length(lines);i++) {
        split(lines[i], p1, " ")
        a = p1[1]
        b = p1[2]
        c = p1[3]
        split(lines[i+1], p2, " ")
        x = p2[1]
        y = p2[2]
        z = p2[3]
        print "/",a,b,c,":: /",x,y,z
        x = abs(x - a)
        y = abs(y - b)
        z = abs(z - c)
        res += int(sqrt(x*x + y*y + z*z))
    }
    print "res/",res
}
