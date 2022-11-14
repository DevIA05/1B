//const departMinutes = 5 //localStorage.getItem("temps")== null ? 5 : localStorage.getItem("temps")
let temps = departMinutes * 60

const timerElement = document.getElementById("timer")

setInterval(() => {
  let minutes = parseInt(temps / 60, 10)
  let secondes = parseInt(temps % 60, 10)

  minutes = minutes < 10 ? "0" + minutes : minutes
  secondes = secondes < 10 ? "0" + secondes : secondes

  timerElement.innerText = `${minutes}:${secondes}`
  temps = temps <= 0 ? 0 : temps - 1
}, 1000)


// window.addEventListener('beforeunload', function (e) {
//   e.preventDefault();
//   val = document.getElementById("timer").textContent;
//   s   = val.split(':');
//   localStorage.setItem('temps', s[0]+s[1]/60)
// });