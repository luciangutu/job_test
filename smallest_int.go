package main

import (
	"fmt"
	"math"
)

func findSmallest(arr []int) int {
	smallest := math.MaxInt64
	for _, num := range arr {
		if num < smallest {
			smallest = num
		}
	}
	return smallest
}

func main() {
	arr1 := []int{34, 15, 88, 2}
	arr2 := []int{34, -345, -1, 100}
	fmt.Println("Smallest integer in arr1:", findSmallest(arr1)) // Output: 2
	fmt.Println("Smallest integer in arr2:", findSmallest(arr2)) // Output: -345
}
