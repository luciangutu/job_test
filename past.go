package main

func Past(h, m, s int) (int, error) {
	milliseconds := (h*3600 + m*60 + s) * 1000

	return milliseconds, nil
}

func main() {
	milliseconds, err := Past(0, 1, 1)
	if err != nil {
		// Handle the error if needed
	}
	println(milliseconds)
}
