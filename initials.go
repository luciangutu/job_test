package main

import (
	"fmt"
	"strings"
)

func main() {
	myResult := processText("hello world")
	fmt.Println(myResult)
}

func processText(text string) string {
	var myResult string
	words := strings.Split(text, " ")
	// the best solution below  
	// return strings.ToUpper(string(words[0][0])) + "." + strings.ToUpper(string(words[1][0]))
	for _, word := range words {
		myResult += strings.ToUpper(string(word[0]))
		myResult += "."
	}
	return strings.TrimSuffix(myResult, ".")
}
