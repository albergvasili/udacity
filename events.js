let designGrid = document.getElementById('designGrid');
let gHeight = document.getElementById('gridHeight');
let gWidth = document.getElementById('gridWidth');
let theButton = document.querySelector('button')

theButton.addEventListener('click', function(){
	checkChild(designGrid);
	console.log('Ca marche');
});


function mkgrid() {
	atable = document.createElement('table');
	designGrid.appendChild(atable);
	for (x = 0; x < gHeight.value; x++){
		row = atable.insertRow(x);
		for (y = 0; y < gWidth.value; y++){
			let cellColor = row.insertCell(y);
			cellColor.addEventListener('click', function(){
				cellColor.style.background = 'blue';

			});
		}
	}
};

function checkChild(element){
	if (element.children.length >= 1){
		while (element.firstChild) {
			element.removeChild(element.firstChild);
		}
		mkgrid();
	} else {
		mkgrid();
	}
};
		
