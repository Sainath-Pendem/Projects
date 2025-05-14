console.log("Lets start js")


let masterplay=document.getElementById('masterplay')
let progess=document.getElementById('progess')
let gif=document.getElementById('gif');
let audioElement=new Audio("songs/3.mp3");
let mastersong=document.getElementById("sname");
let songitem=Array.from(document.getElementsByClassName('songs1'))

let songsList=[
    {songName:'Lets Listen1',filepath:"songs/1.mp3"},
    {songName:'Lets Listen2',filepath:'song/2.mp3'},
    {songName:'Lets Listen3',filepath:'song/3.mp3'},
    {songName:'Lets Listen4',filepath:'song/4.mp3'},
    {songName:'Lets Listen5',filepath:"songs/5.mp3"},
    {songName:'Lets Listen6',filepath:'song/6.mp3'},
    {songName:'Lets Listen7',filepath:'song/7.mp3'},
    {songName:'Lets Listen8',filepath:'song/8.mp3'},
    {songName:'Lets Listen9',filepath:'song/9.mp3'},
    {songName:'Lets Listen10',filepath:'song/10.mp3'}
]

songitem.forEach((element, i) => {
    element.getElementsByClassName('songname')[0].innerText=songsList[i].songName;
})



//play & pause 
masterplay.addEventListener('click',()=>{
    if(audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        masterplay.classList.remove('fa-play-circle');
        masterplay.classList.add('fa-pause-circle');
        gif.style.opacity=1;
    }else{
        audioElement.pause();
        masterplay.classList.remove('fa-pause-circle');
        masterplay.classList.add('fa-play-circle');
        gif.style.opacity=0;
    }
})



//time update add event listener
audioElement.addEventListener('timeupdate',()=>{
    p=parseInt((audioElement.currentTime/audioElement.duration)*100);
    progess.value=p;
})

progess.addEventListener('change',()=>{
    audioElement.currentTime=progess.value*audioElement.duration/100;
})

const makeallplays = ()=>{
    Array.from(document.getElementsByClassName('splay')).forEach((element)=>{
        element.classList.remove('fa-pause-circle');    
        element.classList.add('fa-play-circle');
        masterplay.classList.remove('fa-pause-circle');
        masterplay.classList.add('fa-play-circle');
    })

}

Array.from(document.getElementsByClassName('splay')).forEach((element)=>{
    element.addEventListener('click',(e)=>{
        makeallplays();
        const songIndex=parseInt(e.target.id);
        e.target.classList.remove('fa-play-circle');    
        e.target.classList.add('fa-pause-circle');
        audioElement.src = `songs/${songIndex + 1}.mp3`;
        audioElement.currentTime=0;
        audioElement.play();
        mastersong.innerText=songsList[songIndex].songName;
        masterplay.classList.remove('fa-play-circle');
        masterplay.classList.add('fa-pause-circle');
    });
})

document.getElementById('prevbtn').addEventListener('click',()=>{
    if(songIndex<=0){
        songIndex=9;
    }else{
        songIndex-=1;
    }
        audioElement.src = `songs/${songIndex + 1}.mp3`;
        audioElement.currentTime=0;
        audioElement.play();
        mastersong.innerText=songsList[songIndex].songName;
        masterplay.classList.remove('fa-play-circle');
        masterplay.classList.add('fa-pause-circle');
});
document.getElementById('nextbtn').addEventListener('click',()=>{
    if(songIndex>=9){
        songIndex=0;
    }else{
        songIndex+=1;
    }
        audioElement.src = `songs/${songIndex + 1}.mp3`;
        audioElement.currentTime=0;
        audioElement.play();
        mastersong.innerText=songsList[songIndex].songName;
        masterplay.classList.remove('fa-play-circle');
        masterplay.classList.add('fa-pause-circle');
});