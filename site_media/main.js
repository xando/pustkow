$(function() {

    $('#gallery a img').hover( 
	function() {
	    $(this).addClass('hover')
	},
	function() {
	    $(this).removeClass('hover')
	}
    );
    
});
