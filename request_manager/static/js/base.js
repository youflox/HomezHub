document.querySelector('.header').addEventListener('click', (e)=>{
    window.location = `${window.origin}/${(e.target.id)}`
})