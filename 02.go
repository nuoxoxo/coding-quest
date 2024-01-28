package main

import (
  "fmt"
  "bufio"
  "os"
  "regexp"
  "strings"
  "strconv"
  "math/rand"
  "time"
)

func main () {

  checks := [7]int{12, 48, 30, 95, 15, 55, 97}
  pts := map[int]int{3: 1, 4: 10, 5: 100, 6: 1000}

  // Solution array
  Solutions := []func([7]int, map[int]int)int{
    Solution_regex,
    Solution_strings_fields,
  }

  // xqt
  rand.Seed(time.Now().UnixNano())
  res := Solutions[ rand.Intn(len( Solutions)) ]( checks, pts )

  // Assert
  if res != 110 && res != 56 {
    fmt.Println( res, "/AssertionError" )
  }
}

// way 1

func Solution_strings_fields(checks[7]int, pts map[int]int) int {

  fmt.Println("/Solution_strings_fields")
  res := 0
  sc := bufio.NewScanner (os.Stdin)
  for sc.Scan() {
    line := sc.Text()
    words := strings.Fields( line )
    temp := 0
    for _, word := range words {
      num, _ := strconv.Atoi( word )
      for _, check := range checks {
        if num == check {
          temp++
          break
        }
      }
    }
    res += pts[ temp ]
  }
  fmt.Println("/res", res)
  return res
}

// way 2

func Solution_regex( checks [7]int, pts map[int]int )int{

  fmt.Println("/Solution_regex")
  res := 0
  sc := bufio.NewScanner (os.Stdin)
  for sc.Scan() {
    line := sc.Text()
    re := regexp.MustCompile( "[0-9]+" )
    matches := re.FindAllString( line, -1 )
    temp := 0
    for _, match := range matches {
      num, _ := strconv.Atoi( match )
      for _, check := range checks {
        if num == check {
          temp++
          break
        }
      }
    }
    res += pts[ temp ]
  }
  fmt.Println("/res", res)
  return res
}



