package main

import (
	"bufio"
	"fmt"
	"os"
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
	for _, arr := range Up {
		fmt.Println("/up", arr)
	}
	for _, arr := range Down {
		fmt.Println("/down", arr)
	}
	head := Up[0]
	R, C := len(Up), len(Up[1])
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
			fmt.Println("/mapped", name, adj[name])
		}
		r++
	}

	dist := []int{}
	for _, arr := range Down {
		names := arr[3:]
		N := len(names)
		i := 0
		temp := 0
		for i < N-2 {
			name := names[i] + names[i+2]
			temp += adj[name]
			i += 2
		}
		dist = append(dist, temp)
	}
	res := 0
	for _, n := range dist {
		res += n
	}
	fmt.Println("/res", res)
	if 2467159258920 % res != 0 {
		fmt.Println("/check your answer")
	}
}
