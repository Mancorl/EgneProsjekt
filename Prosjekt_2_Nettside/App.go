package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("Site loaded")
	http.HandleFunc("/Data/Video", List_vids)
	http.Handle("/", http.FileServer(http.Dir("./Static")))
	http.ListenAndServe(":3000", nil)
}

type teststruct struct {
	Svar string
}

func List_vids(s http.ResponseWriter, r *http.Request) {
	test := &teststruct{Svar: "hei"}
	s.Header().Set("Content-Type", "application/json")
	fmt.Println(test)
	fmt.Println("i am called")
	json.NewEncoder(s).Encode(test)
}
