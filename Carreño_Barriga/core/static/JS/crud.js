let el, i;
let data = [
    { firstname: "Mauricio", lastname: "Sevilla" },
    { firstname: "Jorge", lastname: "Barón" },
    { firstname: "Andrés", lastname: "Espinoza" },
    { firstname: "Rafael", lastname: "Pérez" }
];

let panel = document.querySelector("#panel");

//Crear Usuario
function create() {
    let fn = document.querySelector("#fname").value;
    let ln = document.querySelector("#lname").value;
    data = [...data, { firstname: fn, lastname: ln }];
    clearForm();
    console.log(data)
    renderItem();
}
//Actualizar Usuario
function update() {
    data[i].firstname = document.querySelector("#fname").value;
    data[i].lastname = document.querySelector("#lname").value;
    renderItem();
}
//Elimiar Usuario
function deleteItem() {
    data.splice(i, 1);
    renderItem();
}

function renderItem() {

    panel.textContent = "";
    data.forEach(x => {
        el = document.createElement("option");
        el.innerText = `${x.firstname} ${x.lastname}`;
        panel.append(el);
    });
}

function panelClick() {
    i = panel.selectedIndex;
    document.querySelector("#fname").value = data[i].firstname;
    document.querySelector("#lname").value = data[i].lastname;
}

function clearForm() {
    document.querySelector("#fname").value = "";
    document.querySelector("#lname").value = "";
}

renderItem();