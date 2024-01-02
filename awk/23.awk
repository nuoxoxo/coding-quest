BEGIN {

    window = 60
    bound = 100
    t = 3600
}

{

    split($0, field, " ")
    lines[NR, "c"] = field[1]
    lines[NR, "r"] = field[2]
    lines[NR, "dc"] = field[3]
    lines[NR, "dr"] = field[4]
}

END {

    for (i = 0; i < bound; i++)
        for (j = 0; j < bound; j++)
            S[i, j] = 1

    for (line = 1; line <= NR; line++) {
        c = lines[line, "c"]
        r = lines[line, "r"]
        dc = lines[line, "dc"]
        dr = lines[line, "dr"]
        sr = dr * t + r
        sc = dc * t + c

        for (sec = 0; sec <= window; sec++) {
            R = dr * sec + sr
            C = dc * sec + sc
            R = int(R)
            C = int(C)

            if (-1 < R && R < bound && -1 < C && C < bound) {
                S[R, C] = 0
            }
        }
    }

    for (i = 0; i < bound; i++) {
        for (j = 0; j < bound; j++) {
            if (S[i, j] == 1) {
                print j ":" i
                exit
            }
        }
    }
}

