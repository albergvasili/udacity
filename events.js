let designGrid = document.getElementById('designGrid');
let gHeight = document.getElementById('gridHeight');
let gWidth = document.getElementById('gridWidth');
let theButton = document.querySelector("button")

theButton.addEventListener('click', function(){
	mkgrid();
	console.log("Ca marche");
});


function mkgrid() {
	atable = document.createElement("table");
	designGrid.appendChild(atable);
	for (x = 0; x < gHeight.value; x++){
		row = atable.insertRow(x);
		for (y = 0; y < gWidth.value; y++){
			row.insertCell(y);
		}
	}
};

		
