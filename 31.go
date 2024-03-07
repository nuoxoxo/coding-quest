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
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println("/line", line)
		P := strings.Fields(line)
		fmt.Println("/pts", P)
		temp := []string{strings.Join(P[:4], " "), P[2], P[3], P[4]}
		A = append(A, temp)
		/*
			a, _ := strconv.ParseFloat(P[2], 64)
			b, _ := strconv.ParseFloat(P[3], 64)
			c, _ := strconv.ParseFloat(P[4], 64)
		*/
		fmt.Println("/glx", temp)
		fmt.Println("/end")
	}
	END := []float64{}
	N := len(A)
	fmt.Println(N, END)
	i := 0
	for i < N-1 {
		L := A[i]
		a, _ := strconv.ParseFloat(A[i][1], 64)
		b, _ := strconv.ParseFloat(A[i][2], 64)
		c, _ := strconv.ParseFloat(A[i][3], 64)
		fmt.Println("/compare", L, a, b, c)
		j := i + 1
		for j < N {
			R := A[j]
			x, _ := strconv.ParseFloat(A[j][1], 64)
			y, _ := strconv.ParseFloat(A[j][2], 64)
			z, _ := strconv.ParseFloat(A[j][3], 64)
			fmt.Println("/against", R, x, y, z)
			aa, bb, cc := a-x, b-y, c-z
			res := math.Sqrt(aa*aa + bb*bb + cc*cc)
			fmt.Println("/res", res)
			END = append(END, res)
			j++
		}
		i++
	}
	sort.Float64s(END)
	fmt.Println(END[0])
}
