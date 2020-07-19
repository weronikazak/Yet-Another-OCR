var selDiv = "";
	
document.addEventListener("DOMContentLoaded", init, false);

function init() {
	document.querySelector('#file').addEventListener('change', handleFileSelect, false);
	selDiv = document.querySelector("#selectedfiles");
}
	
function handleFileSelect(e) {
	
	if(!e.target.files) return;
	
	selDiv.innerHTML = "";
	
	var files = e.target.files;
	for(var i=0; i<files.length; i++) {
		var f = files[i];
		
		selDiv.innerHTML += '<li class="list-group-item d-flex justify-content-between align-items-center">'
		+ f.name + '<span class="close" onclick="removeImage($(this))">x</span><li/>';
	}
}

function removeImage(item) {
	//alert(item);
	 item.parent().remove();
  }

$( document ).ready(function(){
	if($("#alert").length){
		$('#alert').fadeIn('slow', function(){
			$('#alert').delay(5000).fadeOut(); 
		});
	}
});