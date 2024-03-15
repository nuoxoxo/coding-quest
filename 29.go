package main

import (
	"bufio"
	"fmt"
	"os"
	_ "reflect"
	_ "sort"
	"strconv"
	"strings"
)

func main() {
	Is := "192.168.0.0"
	Ie := "192.168.254.254"
	Ps := "10.0.0.0"
	Pe := "10.0.254.254"
	IN, OUT := 0, 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		S := parserIP( line[24:32] )
		D := parserIP( line[32:] )
		N, _ := strconv.ParseInt(line[4:8], 16, 64)
		if inside(S, Is, Ie) || inside(D, Is, Ie) {
			IN += int(N)
		} else if inside(S, Ps, Pe) || inside(D, Ps, Pe) {
			OUT += int(N)
		} else {
			fmt.Println("/?bug", S, D)
		}
	}
	fmt.Print("/res ", IN, "/", OUT, "\n")
}

func parserIP(line string) []int {
	res := []int{}
	i := 0
	for i < 7 {
		Hex := line[i : i+2]
		Dec, _ := strconv.ParseInt(Hex, 16, 64)
		res = append(res, int(Dec))
		i += 2
	}
	return res
}

func inside(line []int, s string, e string) bool {
	temp := strings.Split(s, ".")
	var ss []int
	for _, s := range temp {
		n, _ := strconv.Atoi(s)
		ss = append(ss, n)
	}
	temp = strings.Split(e, ".")
	var ee []int
	for _, s := range temp {
		n, _ := strconv.Atoi(s)
		ee = append(ee, n)
	}
	i := 0
	for i < 4 {
		if !(ss[i] <= line[i] && line[i] <= ee[i]) {
			return false
		}
		i++
	}
	return true
}
