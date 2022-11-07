const elemInContainer = document.querySelector(".container-question");

const r = document.createElement("div");
singleAnswer = `name="groupe"`
for (let i = 0; i < 3; i++) {
    r.innerHTML += `<input type="checkbox" ${singleAnswer} value="r${i}"/> <label for="r${i}"> réponse ${[i]} </label>`
} 
r.innerHTML = `
    <div class="reponse">
    ${r.innerHTML}
    </div>
` 
const q = document.createElement("div");
q.innerHTML = `
    <div class="question">
        <p> test </p>
    </div>
    <div class="img">
        image
    </div>
    ${`${r.innerHTML}`}
`;

elemInContainer.appendChild(q);
