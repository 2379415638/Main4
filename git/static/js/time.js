function getTime() {
	var current = new Date();
	var time = current.toLocaleTimeString();
	document.getElementById("time").innerHTML =time;
}
setInterval("getTime();",1000/60);
