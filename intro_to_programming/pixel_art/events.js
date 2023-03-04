let designGrid = document.getElementById('designGrid');
let gridHeight = document.getElementById('gridHeight');
let gridWidth = document.getElementById('gridWidth');
let pickColor = document.getElementById('pickColor');
let theButton = document.querySelector('button');

theButton.addEventListener('click', function() {
    checkChild(designGrid);
});


/** 
 * mkgrid(): Create a grid of squares.
 * Add table element to HTML,
 * Insert rows using gridHeight value from input,
 * insert cells on each row using gridWidth value from input,
 * then change color of square when clicked on.
 */

function mkgrid() {
    createTable = document.createElement('table');
    designGrid.appendChild(createTable);
    for (x = 0; x < gridHeight.value; x++) {
        row = createTable.insertRow(x);
        for (y = 0; y < gridWidth.value; y++) {
            let squareColor = row.insertCell(y);
            squareColor.addEventListener('click', function() {
                squareColor.style.background = pickColor.value;
            });
        }
    }
}

/**
 * checkChild(): Check element to determine whether an old table needs to be
 * erased before creating a new one.
 */

function checkChild(element) {
    if (element.children.length >= 1) {
        while (element.firstChild) {
            element.removeChild(element.firstChild);
        }
        mkgrid();
    } else {
        mkgrid();
    }
};
