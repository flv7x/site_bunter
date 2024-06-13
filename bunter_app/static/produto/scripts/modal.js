document.addEventListener('DOMContentLoaded', function() {
    const produtoForm = document.getElementById('produtoForm');

    produtoForm.addEventListener('submit', function(event) {
        event.preventDefault(); 

        const formData = new FormData(this);

        fetch('/cadastrar_produto/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            this.reset();

            const container = document.querySelector('.container');
            const card = `
                <div class="card" style="width: 18rem;">
                    <img src="${data.imagem}" class="card-img-top" alt="${data.descricao}">
                    <div class="card-body">
                        <h5 class="card-title">${data.descricao}</h5>
                        <p class="card-text">Marca: ${data.marca}</p>
                        <p class="card-text">Custo: R$ ${data.custo}</p>
                        <p class="card-text">Preço de Venda: R$ ${data.preco_venda}</p>
                        <!-- Adicione mais informações do produto conforme necessário -->
                    </div>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', card);
        })
        .catch(error => console.error('Erro ao cadastrar produto:', error));
    });
});
