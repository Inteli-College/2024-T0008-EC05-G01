function novoKit() {
    var nome;

    while (true) {
        nome = prompt("Digite o nome do kit:");

        if (nome === null) {
            console.log('Operação cancelada pelo usuário.');
            return;
        }

        if (nome.trim() === "") {
            alert("Por favor, preencha todos os campos.");
        } else {
            break;
        }
    }

    var dados = {
        nome: nome,
        medicamentos: []
    };

    fetch('/kits', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(async response => {
        if (!response.ok) {
            throw new Error('Erro ao criar kit');
        }
        window.location.href = "/kit?kit=" + nome;
    })
    .catch(error => {
        console.error('Erro ao criar kit:', error);
    });
}

function atualizarDados() {
    var medicamentoSelecionado = document.getElementById("medicamentosSelect").value;
    var quantidadeDigitada = document.getElementById("quantidadeInput").value;

    alert("Medicamento selecionado: " + medicamentoSelecionado + "\nQuantidade digitada: " + quantidadeDigitada);

    var dados = {
        medicamento: medicamentoSelecionado,
        quantidade: quantidadeDigitada
    };

    fetch('/addMedicamento', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao adicionar medicamento');
        }
        return response.json();
    })
    .then(data => {
        console.log('Medicamento adicionado com sucesso:', data);
    })
    .catch(error => {
        console.error('Erro ao adicionar medicamento:', error);
    });
}
