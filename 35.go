package main

import (
	"fmt"
	"math/big"
)

//func Solution_correct(amount int, coins []int) int {
	func Solution_correct(amount int, coins []int) *big.Int {
	C := len(coins)
	// dp := make([]int, amount + 1)
	dp := make([]big.Int, amount + 1)
	// dp[0] = 1
	dp[0].SetInt64(1)
	a := 1
	for a < amount + 1 {
		c := 0
		for c < C {
			if a - coins[c] >= 0 {
				// dp[a] += dp[a - coins[c]]
				dp[a].Add( & dp[a], & dp[a - coins[c]] )
			}
			c++
		}
		a++
	}
	return ( & dp[amount])
}

func main() {
	// var res int
	var res * big.Int
	{
		amount, coins := 5, []int{1, 2, 3}
		res = Solution_correct(amount, coins)
		fmt.Println("/res", res)
	}
	{
		coins, amount := []int{1, 2, 12, 40}, 856
		res = Solution_correct(amount, coins)
		fmt.Println("/res", res)
	}
}
