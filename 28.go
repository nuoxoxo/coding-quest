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
        temp, err := strconv.Atoi( F[2] )
        if err != nil {
            fmt.Println(err)
            continue
        }
        if contains(ADD, cost) {
            D[ name ] += temp
        } else if contains(SUB, cost) {
            D[ name ] -= temp
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

func contains(arr []string, name string)bool{
    for _, key := range arr {
        if name == key {
            return true
        }
    }
    return false
}

