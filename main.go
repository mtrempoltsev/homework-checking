package main

import (
    "io/ioutil"
    "fmt"
    "log"
    "math/rand"
    "net/http"
    "os"
    "os/exec"
    "time"
)

func main() {
    rand.Seed(time.Now().Unix())

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        http.ServeFile(w, r, "html/index.html")
    })
    
    http.HandleFunc("/result", func(w http.ResponseWriter, r *http.Request){
        if r.Method == "POST" {
            err := r.ParseForm()
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }

            homework := r.FormValue("homework")
            code := []byte(r.FormValue("code"))

            id := fmt.Sprintf("%x.%x", time.Now().Unix(), rand.Int())

            path, err := ioutil.TempDir("/tmp", id)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }

            defer os.RemoveAll(path)

            file, err := os.Create(path + "/main.cpp")
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }
            file.Write(code)
            file.Close()

            log.Println("session temp dir:", path)

            out, err := exec.Command("bash", "-c", fmt.Sprintf("./run.sh %s %s %s", homework, path, id)).CombinedOutput()
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }

            fmt.Fprintf(w, string(out))
        } else {
            http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
        }
    })

    log.Fatal(http.ListenAndServe(":2018", nil))
}
