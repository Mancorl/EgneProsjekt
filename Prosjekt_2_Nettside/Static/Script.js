document.addEventListener("DOMContentLoaded", ()=>{
    //Kjøres når siden er lastet inn
    console.log("test");
    function hei(){
        event.preventDefault();
        alert("hei");
        remove_content()
        list_videos()
    };
    document.getElementById("ListProjects").onclick = hei;
    console.log("JavaScript is working!");

    //Fjerner innhold i div
    function remove_content(){
        document.getElementById("center").innerHTML = ''
    }

    //Lister opp videoene som er lastet opp
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
                actiondiv.value=data[i];
                //Lager en onclick funcksjon som er unik til hvert element,
                //Dette lar hver listing hente ut den korresponderende videoen
                actiondiv.onclick=function(){Visvideo(i)};
                actiondiv.append(data[i]);
                videodiv.append(actiondiv);
                
                document.getElementById("center").append(videodiv);
            }


        }catch(error){
            console.error(error);
        }
        
    }

    //Spiller av videoen som er valgt
    async function Visvideo(i){
        //Dersom videoen trenger litt tid, viser vi at noe skjer
        document.getElementById("center").textContent="";
        document.getElementById("center").textContent="Video is loading, please wait";
        //Henter ut video fra backend
        let response = await fetch("/Hent_videoer",{
            method:"POST",
            headers:{
                "content-type":"application/x-www-form-urlencoded",
            },
            body:`video=${i}`,
        });
        //Stremer videoen som blob
        data = await response.blob()
        let videoelement = document.createElement("video")
        videoelement.src = URL.createObjectURL(data)
        videoelement.type="video/mp4"
        videoelement.setAttribute("controls", true)
        videoelement.setAttribute("width","360px")

        document.getElementById("center").textContent=""
        document.getElementById("center").appendChild(videoelement)


    }
});





