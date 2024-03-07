package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	_ "reflect"
	"sort"
	"strconv"
	"strings"
)

type GLX interface {
	name() string
	a() float64
	b() float64
	c() float64
}

func main() {
	A := [][]string{}
	scanner := bufio.NewScanner(os.Stdin)
	SEP := "\n\t"
	for scanner.Scan() {

		line := scanner.Text()
		if strings.HasPrefix(line, "System   ") {
			continue
		}
		fmt.Println("/str", line)
		P := strings.Fields(line)
		N := len(P)
		temp := []string{strings.Join(P[:N-4], " "), P[N-3], P[N-2], P[N-1]}
		A = append(A, temp)
		fmt.Println("/glx", temp)
		fmt.Println("/end \n")
	}
	END := [][]string{}
	N := len(A)
	i := 0
	for i < N-1 {
		L := A[i][0]
		a, _ := strconv.ParseFloat(A[i][1], 64)
		b, _ := strconv.ParseFloat(A[i][2], 64)
		c, _ := strconv.ParseFloat(A[i][3], 64)
		fmt.Println("/compare", L, SEP, a, b, c)
		j := i + 1
		for j < N {
			R := A[j][0]
			x, _ := strconv.ParseFloat(A[j][1], 64)
			y, _ := strconv.ParseFloat(A[j][2], 64)
			z, _ := strconv.ParseFloat(A[j][3], 64)
			fmt.Println("/against", R, SEP, x, y, z)
			aa, bb, cc := a-x, b-y, c-z
			dist := math.Sqrt(aa*aa + bb*bb + cc*cc)
			dist_str := strconv.FormatFloat(dist, 'f', -1, 64)
			END = append(END, []string{dist_str, L, R})
			j++
		}
		i++
		fmt.Println()
	}
	// sort.Float64s(END)
	sort.SliceStable(END, func(l, r int) bool {
		L, _ := strconv.ParseFloat(END[l][0], 64)
		R, _ := strconv.ParseFloat(END[r][0], 64)
		return L < R
	})
	for _, line := range END[:5] {
		fmt.Println(line)
	}
}
