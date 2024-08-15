package main

import (
	"fmt"
	// "strconv"
)

func StringToNumber(str string) (int, error) {
	num, err := fmt.Println(str) // strconv.Atoi(str)
	if err != nil {
		return 0, err
	}
	return num, nil
}

func main() {
	StringToNumber("1234")
	num, err := StringToNumber("1234")
	if err != nil {
		// handle error
		return
	}
	fmt.Println(num)
}
