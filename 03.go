package main

import (
  "fmt"
  "os"
  "bufio"
  "strconv"
  "strings"
  "math"
)

func main () {

  sc := bufio.NewScanner( os.Stdin )
  last := []float64{}
  var res float64 = 0.0
  for sc.Scan() {
    nums := strings.Fields( sc.Text() )
    coor := [3]float64{}
    for i, s := range nums {
      num, _ := strconv.ParseFloat( s, 64 )
      coor [i] = num
    }
    if len(last) == 0 {
      last = coor[:]
      continue
    }
    // dbg
    // fmt.Println( "/coor", coor )

    x, y, z := coor[0], coor[1], coor[2]
    a, b, c := last[0], last[1], last[2]

    f := math.Abs(x - a)
    g := math.Abs(y - b)
    h := math.Abs(z - c)

    res += math.Floor( math.Sqrt(f*f + g*g + h*h) )
    last = coor[:]
  }
  fmt.Println( "/res,", int(res) )
}
