$(function(){
	$('input:checkbox').on('change', function() {

		var $checkedBox 	= $(this),
			checkedBoxLabel	= $checkedBox.parent('label').text(),
			checkedValue	= $checkedBox.val()
			alreadyChecked	= !$checkedBox[0].checked;

		console.log(checkedBoxLabel)

		if(alreadyChecked){

		}else{
			var targ = event.target || event.srcElement;
    		document.getElementById("id_content").value += checkedValue;
		}

		

	});
});