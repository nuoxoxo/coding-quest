package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	_ "sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var nums []int
	temp := strings.Fields(scanner.Text())
	fmt.Println("/temp", temp[:11], reflect.TypeOf(temp))
	for _, s := range temp {
		n, _ := strconv.Atoi(s)
		nums = append(nums, n)
	}
	R, C, N := 6, 10, len(nums)
	if N > 100 {
		R, C = 80, 100
	}
	fmt.Println("/nums", nums[:11], reflect.TypeOf(nums), R, C)
	A := make([]string, R*C)
	i := 0
	for i < R*C {
		A[i] = "."
		i++
	}
	curr, idx := 0, 0
	for idx < N-1 {
		l, r := nums[idx], nums[idx+1]
		curr += l
		i = curr
		for i < curr+r {
			A[i] = "@"
			i++
		}
		printer(A, R, C)
		idx += 2
		curr += r
	}
	printer(A, R, C)
}

func printer(A []string, R int, C int) {
	r, c := 0, 0
	for r < R {
		c = 0
		for c < C {
			fmt.Print(A[c+r*C] + " ")
			c++
		}
		fmt.Println()
		r++
	}
	fmt.Println("/end")
}
