let designGrid = document.getElementById('designGrid');
let gHeight = document.getElementById('gridHeight');
let gWidth = document.getElementById('gridWidth');
let forme = document.querySelector("table");
let theButton = document.querySelector("button")

theButton.addEventListener('click', function(){
	mkgrid();
	console.log("Ca marche");
});


function mkgrid() {
		icell = document.createElement("tr");
		forme.appendChild(icell);
			
};
