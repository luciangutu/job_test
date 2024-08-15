package main

import (
	"fmt"
)

func Grow(arr []int) int {
	sum := 1
	for _, v := range arr {
		// or sum *= v
		sum = sum * v
	}
	return sum
}

func main() {
	myResult := Grow([]int{1, 2, 3, 4})
	fmt.Println(myResult)
}
