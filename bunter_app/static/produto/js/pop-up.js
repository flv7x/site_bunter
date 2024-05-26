$(document).ready(function() {
    // Quando o botão "Mais informações" é clicado
    $('.mais-informacoes').click(function(e) {
        e.preventDefault(); // Evita que o link seja seguido

        // Abre o modal correspondente
        $($(this).data('target')).modal('show');
    });
});