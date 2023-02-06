

function signalListAppend(list) {
    signalMenu.textContent = '';

    let btn1 = document.createElement("button");
    btn1.type = 'submit';
    btn1.textContent = 'prueba';
    btn1.style.display = 'none';
    signalMenu.appendChild(btn1);

    let signalDiv = document.getElementById("signalList");

    let arrayLength = list.length;
    for (let i = 0; i < arrayLength; i++) {
        let radiobox = document.createElement('input');
        radiobox.type = 'radio';
        radiobox.required = true;
        radiobox.value = list[i];
        radiobox.id = list[i];
        radiobox.name = 'signalName';

        let label = document.createElement('label');
        label.htmlFor = list[i];
        label.textContent = list[i];

        signalMenu.appendChild(radiobox);
        signalMenu.appendChild(label);
        signalMenu.appendChild(document.createElement('BR'));
    }
}


// Signal Divs

function createSignalDiv(value) {

    let divExists = document.getElementById(value.value);
    if (divExists) {
        divExists.parentElement.style = 'block'
    } else {

        const plotDiv = document.createElement('div');
        const h3 = document.createElement('h3');
        const signalDiv = document.createElement('div');

        plotDiv.classList.add('plotDiv')
        signalDiv.style['width'] = '400px';
        signalDiv.style['height'] = '300px';
        signalDiv.style.backgroundColor = 'black';
        signalDiv.id = value.value
        h3.innerHTML = value.dataset.name

        plotDiv.appendChild(h3);
        plotDiv.appendChild(signalDiv);
        plotsSection.insertAdjacentElement('beforeend', plotDiv);
    }

};

function removeSignalDiv(value) {
    let divExists = document.getElementById(value.value);
    if (divExists) {
        divExists.parentElement.style.display = 'none';
    } else {
        console.log('doesnt exist')
    }
};
