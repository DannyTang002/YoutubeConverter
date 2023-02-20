
class AllSongs{
    constructor(id, list=[]){
        this.list = document.getElementById(id)
        list = ["id","title"]

    }
    getData(){
        fetch("/converter/get-videos")
        .then((response)=>response.json())
        .then((data)=>{
            console.log("he")
            for(let i = 0; i<data.length;i++){
                let datas = JSON.stringify(data[i]);
                let jsondata = JSON.parse(datas);
                this.appendList(jsondata.id + " "  + jsondata.title);
                console.log(data[i]);
            }
        })
    }

    appendList(data){
        let node = document.createElement('li');
        node.appendChild(document.createTextNode(data));
        listOfSongs.appendChild(node)
    }
}



const songs = new Songs("songs");
let slug = url => new URL(document.URL).pathname.match(/[^\/]+/g)
let showSongs = document.getElementById("addSong");
const allsongs = new AllSongs("listOfSongs")


document.querySelectorAll('#songs td').forEach(e => e.addEventListener("change", clickHandler));


function clickHandler() {
    console.log("clicked")     
}




showSongs.addEventListener("click", async(e)=>{
    e.preventDefault();
    allsongs.getData();
});


