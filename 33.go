package main

import (
	"bufio"
	"fmt"
	"os"
    "math"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
    lines := []string{}
    for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
            continue
        }
        rhs := strings.Trim(strings.Split(line, ":")[1], " ")
        fmt.Println("/line", line)
        fmt.Println("/rhs ", rhs)
        lines = append(lines, rhs)
    }

    // parsing 2 elements from input
    key, cipher := lines[0], lines[1]
    fmt.Println("/", key, "/", cipher)

    // prepare playfair grid (1/2) - string
    S := [26]bool{}
    PF := []string{}
    for _, c := range key {
        pos := c - 'a'
        if !S[pos] {
            S[pos] = true
            PF = append(PF, string(c))
        }
    }
    fmt.Println("/playfair.pre -", PF)
    for i, boo := range S {
        if !boo {
            c := i + 'a'
            if c != 'j' {
                PF = append(PF, string(c))
                S[i] = true
            }
        }
    }
    fmt.Println("/playfair.str -", PF)

    // prepare playfair grid (2/2) - 2D grid
    G := [][]string{}
    edge := int(math.Sqrt( float64(len(PF))))
    i := 0
    for i < edge {
        temp := []string{}
        j := 0
        for j < edge {
            temp = append(temp, PF[ i * 5 + j ])
            j++
        }
        G = append(G, temp)
        i++
    }
    fmt.Println("/grid: \n ", G)

    // pre-processing playfair - space positions, original string (charset) & a copy (msgarr)
    msgarr := []string{}
    spaces := []int{}
    charset := []string{}
    for i, c := range cipher {
        if c == ' ' {
            spaces = append(spaces, i)
        } else {
            charset = append(charset, string(c))
        }
    }
    msgarr = append(msgarr, charset...)
    fmt.Println("/spaces: \n", spaces)
    fmt.Println("/charset: \n", charset)
    fmt.Println("/msgarr: \n", msgarr)
    fmt.Printf("/charset: %p\n", charset)
    fmt.Printf("/replica: %p\n", msgarr)

    // do playfair
    i = 0
    N := len( charset )
    for i < N - 1 {
        finder := func(char string) []int {
            r := 0
            for r < edge {
                c := 0
                for c < edge {
                    if G[r][c] == char {
                        return []int{r, c}
                    }
                    c++
                }
                r++
            }
            return []int{}
        }
        a, b := charset[i], charset[i+1]
        A := finder(a)
        r, c := A[0], A[1]
        B := finder(b)
        rr, cc := B[0], B[1]
        var sub1, sub2 string
        if r != rr && c != cc {
            sub1 = G[r][cc]
            sub2 = G[rr][c]
        } else if r == rr {
            sub1 = G[r][edge-1]
            if c != 0 {
                sub1 = G[r][c-1]
            }
            sub2 = G[rr][edge-1]
            if cc != 0 {
                sub2 = G[rr][cc-1]
            }
        } else if c == cc {
            sub1 = G[edge-1][c]
            if r != 0 {
                sub1 = G[r-1][c]
            }
            sub2 = G[edge-1][cc]
            if rr != 0 {
                sub2 = G[rr-1][cc]
            }
        }
        msgarr[i] = sub1 
        msgarr[i+1] = sub2
        i += 2
    }

    // recover original spaces
    res := ""
    for _, char := range msgarr {
        res += char
    }
    for _, i := range spaces {
        res = res[:i] + " " + res[i:]
    }
    fmt.Println("/res", res)
}

