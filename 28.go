package main

import (
    "fmt"
    "os"
    "bufio"
    "strconv"
    "strings"
    "sort"
)

func main () {

    ADD := []string{"seat", "meal", "meals", "luggage", "fee", "tax"}
    SUB := []string{"discount", "rebate"}
    D := make(map[string]int)
    scanner := bufio.NewScanner( os.Stdin )
    for scanner.Scan() {
        F := strings.Fields( scanner.Text() )
        name, cost := F[0][:len(F[0])-1], strings.ToLower( F[1] )
        for _, cat := range ADD {
            if cost == cat {
                temp, err := strconv.Atoi( F[2] )
                if err == nil {
                    _, ok := D[name]
                    if ok {
                        D[name] += temp
                    } else {
                        D[name] = temp
                    }
                }
                break
            }
        }
        for _, cat := range SUB {
            if cost == cat {
                temp, err := strconv.Atoi( F[2] )
                if err == nil {
                    _, ok := D[name]
                    if ok {
                        D[name] -= temp
                    } else {
                        D[name] = -temp
                    }
                }
                break
            }
        }
    }
    var keys []string
    for key := range D {
        keys = append(keys, key)
    }
    sort.SliceStable(keys, func(l, r int)bool{
        return D[keys[ l ]] < D[keys[ r ]]
    })
    for _, key := range keys {
        fmt.Println("/", D[key], key)
    }
    fmt.Println("/res", keys[0], D[keys[0]])
    if D[keys[0]] != 191274 {
        fmt.Println("/assertError")
    }
}

