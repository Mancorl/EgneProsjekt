package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	fmt.Println("Site loaded")
	http.HandleFunc("/Hent_antall_videoer", List_number_of_videos)
	http.HandleFunc("/Hent_videoer", List_vids)
	http.Handle("/", http.FileServer(http.Dir("./Static")))
	http.ListenAndServe(":3000", nil)
}

func List_vids(s http.ResponseWriter, r *http.Request) {
	streng := r.URL.String()
	fmt.Println(streng)

	fil, err := os.Open("Data/Video/" + streng)
	if err != nil {
		fmt.Println(err)
	}

	s.Header().Set("Content-Type", "video/mp4")
	s.Header().Set("Content-Disposition", "inline;filename="+fil.Name())
	_, err = io.Copy(s, fil)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Print(fil)
	fmt.Println("i am called")

}

func List_number_of_videos(s http.ResponseWriter, r *http.Request) {
	Data, err := os.ReadDir("Data/Video")
	liste := []string{}
	if err != nil {
		fmt.Println(err)
	}
	for i := range Data {
		liste = append(liste, Data[i].Name())

	}

	s.Header().Set("Content-Type", "application/json")
	fmt.Println(liste)
	fmt.Println("i am called")
	json.NewEncoder(s).Encode(liste)
}
