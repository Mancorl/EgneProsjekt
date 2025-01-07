document.addEventListener("DOMContentLoaded", ()=>{
    console.log("test");
    function hei(){
        event.preventDefault();
        alert("hei");
        remove_content()
        list_videos()
    };
    document.getElementById("ListProjects").onclick = hei;
    console.log("JavaScript is working!");


    function remove_content(){
        document.getElementById("center").innerHTML = ''
    }

    async function list_videos(){
        try {
            const response = await fetch("/Hent_videoer");
            data = await response.json();
            const videodiv = document.createElement("div")
            videodiv.id = "videoliste";

            console.log(data);
            window.alert(data);
            for (let i =0; i<data.length;i++){
                videodiv.append(data[i])
            }
            document.getElementById("center").appendChild(videodiv)
            

        }catch(error){
            console.error(error);
        }
        
    }
});





