package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"time"
)

func main() {
	fmt.Println("Site loaded")
	http.HandleFunc("/Hent_antall_videoer", List_number_of_videos)
	http.HandleFunc("/Hent_videoer", List_vids)
	http.Handle("/", http.FileServer(http.Dir("./Static")))
	http.ListenAndServe(":3000", nil)
}

func List_vids(s http.ResponseWriter, r *http.Request) {
	streng, err := strconv.Atoi(r.FormValue("video"))
	if err != nil {
		print(error(err))
	}
	fmt.Println(streng)
	Vidlist, err := os.ReadDir("Data/Video")
	if err != nil {
		print(error(err))
	}
	var fil *os.File
	for i := range Vidlist {
		if i == streng {
			fil, err = (os.Open(filepath.Join("Data/Video", Vidlist[i].Name())))
			if err != nil {
				print(error(err))
			}
			print(fil.Name())
			break
		}

	}
	defer fil.Close()
	fmt.Println(fil.Name())
	s.Header().Set("Content-Type", "video/mp4")
	s.Header().Set("Content-Disposition", "inline;filename="+filepath.Base(fil.Name()))
	http.ServeContent(s, r, fil.Name(), time.Now(), fil)
	fmt.Println("i am called")

}

func List_number_of_videos(s http.ResponseWriter, r *http.Request) {
	Data, err := os.ReadDir("Data/Video")
	liste := []string{}
	if err != nil {
		print(error(err))
	}
	for i := range Data {
		liste = append(liste, Data[i].Name())

	}

	s.Header().Set("Content-Type", "application/json")
	fmt.Println(liste)
	fmt.Println("i am called")
	json.NewEncoder(s).Encode(liste)
}
