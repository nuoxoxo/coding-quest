package main

import (
  "fmt"
  "bufio"
  "os"
  "strconv"
)

func main () {

  var A[]int
  var DG int = 60

  scanner := bufio.NewScanner( os.Stdin )
  fmt.Println( "here" )
  for scanner.Scan() {
    line := scanner.Text()
    num, _ := strconv.Atoi( line )
    A = append(A, num)
    
    // DBG
    fmt.Println ("/dbg:line num len :", line, num, len(A) )
  }

  res := 0

  window := Slice_Sum( A[: DG] )
  avg := window / DG
  if avg < 1500 || avg > 1600 {
    fmt.Println(window)
    res++
  }
  L := len(A)

  for i := 1; i + (DG-1) < L; i++ {
    window = window - A[ i - 1 ] + A[ i + (DG-1) ]
    avg = window / DG
    if avg < 1500 || avg > 1600 {
      res++
    }
  }

  fmt .Println("/res", res )

  // Assert
  if res != 6248 && res != 10 {

    fmt.Println( res, 6248,"/AssertionError" )
  }
}

func Slice_Sum(arr[]int) int {

  res := 0

  for _, n := range arr {
    res += n
  }
  return res
}

