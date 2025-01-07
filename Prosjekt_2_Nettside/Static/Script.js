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
            const response = await fetch("/Data/Video");
            data = await response.json();
            document.getElementById("center").innerHTML = data;
            

        }catch(error){
            console.error(error);
        }
        
    }
});





