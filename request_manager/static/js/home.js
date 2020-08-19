document.getElementById("requestbtn").addEventListener('click', ()=>{
    window.location = `${window.origin}/home/requests`
})

document.querySelector('table').addEventListener('click', (e)=>{
    if(e.target.id){
    console.log(e.target.id)
    window.location = `${window.origin}/home/request/${e.target.id}`}
})