$(function() {
	DB.redraw();

	$("#toolbox").accordion({
		collapsible: true,
		active: false,
		heightStyle: "content"
	});

	$("#add_table_btn").click(function() {
		// Adding the name and id attribute to the table
		var name = $('#table_name').val();
		var app_name = $('#app_name').val();
		var tb = DB.createTable(name, app_name);

		$("#edit_form").empty();
		$("#table_name").val("");
		//$("#toolbox").accordion({active: false});

	});	

	$("#rapapp").click(function() {
		content = DB.toSQL();
	});

});