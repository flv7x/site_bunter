document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        const cpfInput = document.getElementById('id_cpf');
        const cpf = cpfInput.value.replace(/[^\d]/g, ''); // Remove todos os caracteres não numéricos
        if (!validarCPF(cpf)) {
            event.preventDefault();
            document.getElementById('cpf-error').classList.remove('d-none');
        } else {
            document.getElementById('cpf-error').classList.add('d-none');
        }
    });

    // Adiciona formatação ao CPF enquanto o usuário digita
    document.getElementById('id_cpf').addEventListener('input', function() {
        const cpfInput = document.getElementById('id_cpf');
        let cpf = cpfInput.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        if (cpf.length > 3) {
            cpf = cpf.substring(0, 3) + '.' + cpf.substring(3);
        }
        if (cpf.length > 7) {
            cpf = cpf.substring(0, 7) + '.' + cpf.substring(7);
        }
        if (cpf.length > 11) {
            cpf = cpf.substring(0, 11) + '-' + cpf.substring(11);
        }
        cpfInput.value = cpf;

        // Verifica se o CPF é válido e exibe mensagem de erro se for inválido
        if (cpf.length === 14) {
            const cpfValido = validarCPF(cpf.replace(/\D/g, ''));
            if (!cpfValido) {
                document.getElementById('cpf-error').classList.remove('d-none');
            } else {
                document.getElementById('cpf-error').classList.add('d-none');
            }
        }
    });
});

function validarCPF(cpf) {
    let soma = 0;
    let resto;
    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;
    for (let i = 1; i <= 9; i++) soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) resto = 0;
    if (resto !== parseInt(cpf.substring(9, 10))) return false;
    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    resto = (soma * 10) % 11;
    if ((resto === 10) || (resto === 11)) resto = 0;
    if (resto !== parseInt(cpf.substring(10, 11))) return false;
    return true;
}