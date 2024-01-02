BEGIN {

    ORS=""
    R = 10; C = 50
    for (i = 1; i <= R; i++)
        for (j = 1; j <= C; j++)
            G[i, j] = "."
} {

    printer()
    for (r = $2 + 1; r <= $2 + $4; r++)
        for (c = $1 + 1; c <= $1 + $3; c++)
            G[r, c] = (G[r, c] == ".") ? "#" : "."
} END {
    printer()
}

function printer() {

    for (i = 1; i <= R; i++) {
        for (j = 1; j <= C; j++) {
            print G[i,j],""
        }
        print "\n"
    }
    print "\n"
}

