function rvalue(val) {
    return val ~ /^-?[0-9]+$/ ? val : D[val]
}

BEGIN {
    i = 1
}
{
    lines[NR] = $0
    SIZE++
}
END {
    while (i) {
        split(lines[i], expr, " ")
        sizeof = length(expr)
        assert (sizeof==1 || sizeof==2 || sizeof==3)#, "err/")
        if (sizeof==1) { # cmd is END
            break
        }
        cmd = expr[1]
        if (cmd == "OUT") {
            print "out/",rvalue(expr[2])
            res = rvalue(expr[2])
        } else if (cmd == "JIF" && cmp || cmd == "JMP") {
            i = (i + rvalue(expr[2])) % (SIZE+1)
            continue
        } else if (cmd == "MOV") {
            D[expr[2]] = rvalue(expr[3])
        } else if (cmd == "ADD") {
            D[expr[2]] += rvalue(expr[3])
        } else if (cmd == "CEQ") {
            cmp = D[expr[2]] == rvalue(expr[3])
        } else if (cmd == "CGE") {
            cmp = D[expr[2]] >= rvalue(expr[3])
        } else if (cmd == "MOD") {
            #assert (rvalue(expr[3]) != 0)#, "mod by 0")
            D[expr[2]] %= rvalue(expr[3])
        } else if (cmd == "DIV") {
            #assert (rvalue(expr[3]) != 0)#, "div by 0")
            D[expr[2]] /= rvalue(expr[3])
        }
        i++
    }
    print "res/",res
}
