    import Songs from "./songs.js/";
const songs = new Songs("songs");

let register = document.getElementById("addSong");



register.addEventListener("click", async(e)=>{
    e.preventDefault();
    songs.getData();
});