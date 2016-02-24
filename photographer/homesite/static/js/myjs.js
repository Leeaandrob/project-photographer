$(document).ready(function () {
	var div = document.getElementById('nav-mobile'), nav = document.getElementsByClassName('nav-holder')[0];
	div.addEventListener('click', function (e){
		nav.style.display = "block";
	});
});
