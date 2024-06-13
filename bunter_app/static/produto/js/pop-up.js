$(document).ready(function() {
    $('.mais-informacoes').click(function(e) {
        e.preventDefault();
        $($(this).data('target')).modal('show');
    });
});