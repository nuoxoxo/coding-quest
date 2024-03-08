package main

import (
	"bufio"
	"fmt"
	_ "math"
	"os"
	_ "reflect"
	_ "sort"
	"strconv"
	"strings"
)

func main() {
	A := [][]string{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		A = append(A, parts)
	}
	idx := 0
	for i, a := range A {
		if len(a) == 0 {
			idx = i
			break
		}
	}
	Up, Down := A[:idx], A[idx+1:]
	for _, a := range Up {
		fmt.Println("/up", a)
	}
	for _, a := range Down {
		fmt.Println("/down", a)
	}
	head := Up[0]
	R, C := len(Up), len(Up[0])
	adj := map[string]int{}
	fmt.Println(R, C)
	r := 1
	for r < R {
		col := Up[r][0]
		c := 1
		for c < C {
			row := head[c-1]
			name := col + row
			n, _ := strconv.Atoi(Up[r][c])
			adj[name] = n
			c++
			fmt.Println(name, adj[name])
		}
		r++
	}
	for k, v := range adj {
		fmt.Println(k, v)
	}
	// TODO : parse this
	// /down [Rover 1 route: base -> cx22 -> ta00 -> base -> xj84 -> base]
}
