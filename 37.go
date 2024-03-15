package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	x, o   = "x", "o"
	tokens = []string{o, x}
	side   = 20
	DIR    = [][]int{
		{0, -1},  // U
		{1, -1},  // UR
		{1, 0},   // R
		{1, 1},   // DR
		{0, 1},   // D
		{-1, 1},  // DL
		{-1, 0},  // L
		{-1, -1}, //UL
	}
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	G := [][]string{}
	for scanner.Scan() {
		temp := scanner.Text()
		lines := strings.Split(temp, " ")
		G = append(G, lines)
	}
	if len(G) < 10 {
		side = 6
	}
	fmt.Println(side, len(G))
	p1, p2 := 0, 0
	for _, moves := range G {
		B := playRound(moves)
		p1 += countTokens(B, 0)
		p2 += countTokens(B, 1)
	}
	fmt.Println("/res", p1, p2)
}

// ^ Drive

// v Helpr

func playRound(moves []string) [][]string {
	B := makeBoard(side)
	for i, move := range moves {
		player := i % 2
		temp := parseMove(move) // Player 1 is Even-indexed
		r, c := temp[0], temp[1]
		if !isMoveValid(B, player, move) {
			break
		}
		B[r][c] = tokens[player]
		for _, dir := range DIR {
			dr, dc := dir[0], dir[1]
			offset := 1
			for -1 < r+dr*offset && r+dr*offset < side &&
				-1 < c+dc*offset && c+dc*offset < side &&
				B[r+dr*offset][c+dc*offset] == tokens[1-player] {
				offset++
			}
			endr, endc := r+dr*offset, c+dc*offset
			if !(-1 < endr && endr < side) ||
				!(-1 < endc && endc < side) ||
				B[endr][endc] != tokens[player] { // my remote token not found
				endr, endc = -1, -1
			}
			offset = 1
			if endr == -1 || endc == -1 {
				continue
			}
			for -1 < r+dr*offset && r+dr*offset < side &&
				-1 < c+dc*offset && c+dc*offset < side &&
				B[r+dr*offset][c+dc*offset] == tokens[1-player] {
				B[r+dr*offset][c+dc*offset] = tokens[player] // placing my token
				offset++
			}
		}
		printBoard(B)
		fmt.Println("/move", move)
	}
	return B
}

func makeBoard(side int) [][]string {
	B := make([][]string, side)
	r := 0
	for r < side {
		row := make([]string, side)
		c := 0
		for c < side {
			row[c] = "."
			c++
		}
		B[r] = row
		r++
	}
	mid := side / 2
	B[mid-1][mid-1], B[mid][mid] = o, o
	B[mid-1][mid], B[mid][mid-1] = x, x
	return B
}

func printBoard(B [][]string) {
	for _, b := range B {
		fmt.Println(b)
	}
}

func parseMove(s string) []int {
	r := int(s[0] - 'a')
	c, _ := strconv.Atoi(s[1:])
	return []int{r, c - 1}
}

func countTokens(B [][]string, player int) int {
	res := 0
	for _, r := range B {
		for _, c := range r {
			if c == tokens[player] {
				res++
			}
		}
	}
	return res
}

func isMoveValid(B [][]string, player int, move string) bool {
	temp := parseMove(move)
	r, c := temp[0], temp[1]
	if r < 0 || r > side-1 || c < 0 || c > side-1 || B[r][c] != "." {
		return false
	}
	for _, dir := range DIR {
		dr, dc := dir[0], dir[1]
		offset := 1
		for -1 < r+dr*offset && r+dr*offset < side &&
			-1 < c+dc*offset && c+dc*offset < side &&
			B[r+dr*offset][c+dc*offset] == tokens[1-player] {
			offset++
		}
		if -1 < r+dr*offset && r+dr*offset < side &&
			-1 < c+dc*offset && c+dc*offset < side &&
			B[r+dr*offset][c+dc*offset] == tokens[player] {
			return true
		}
	}
	fmt.Println("/👆invalid move", move)
	fmt.Println("/player", tokens[player], "/pos", r, c)
	return false
}
