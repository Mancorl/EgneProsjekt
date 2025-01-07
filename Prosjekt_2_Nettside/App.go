package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	fmt.Println("Site loaded")
	http.HandleFunc("/Hent_videoer", List_vids)
	http.Handle("/", http.FileServer(http.Dir("./Static")))
	http.ListenAndServe(":3000", nil)
}

func List_vids(s http.ResponseWriter, r *http.Request) {
	videolist := []string{}
	Data, err := os.ReadDir("Data/Video")
	if err != nil {
		fmt.Println(err)
	}

	for _, file := range Data {
		vl := file.Name()

		videolist = append(videolist, vl)

	}
	s.Header().Set("Content-Type", "application/json")
	fmt.Println(videolist)
	fmt.Println("i am called")
	json.NewEncoder(s).Encode(videolist)
}
