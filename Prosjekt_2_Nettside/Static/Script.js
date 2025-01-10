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
            let response = await fetch("/Hent_antall_videoer");
            data = await response.json();
            


            console.log(data);
            window.alert(data);
            for (let i =0; i<data.length;i++){
                const videodiv = document.createElement("div");
                videodiv.id = i;
                const actiondiv = document.createElement("a");
                actiondiv.onclick=function(){Visvideo(i,actiondiv.value)};
                actiondiv.value=data[i];
                actiondiv.append(data[i]);
                videodiv.append(actiondiv);
                
                document.getElementById("center").append(videodiv);
            }


        }catch(error){
            console.error(error);
        }
        
    }

    function Visvideo(i,vid){
        window.alert(i)
        window.alert(vid)
    }
});





