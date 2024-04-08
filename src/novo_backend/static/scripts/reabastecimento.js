function passarUrll(){
    var url = window.location.href;
    var url = new URL(url);
    var item = url.searchParams.get("item");

    window.location.href = "/config?item=" + item;
}

console.log("hello world");
// Função para carregar dinamicamente as opções de medicamentos
function carregarMedicamentos() {
    fetch('/medicamentos')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('medicamentosSelect');

            select.innerHTML = '';
    
            const placeholderOption = document.createElement('option');
            placeholderOption.value = '';
            placeholderOption.text = 'Selecione um medicamento';
            placeholderOption.disabled = true;
            placeholderOption.selected = true;
            select.appendChild(placeholderOption);
    
            for (const key in data.medicamentos) {
                if (data.medicamentos.hasOwnProperty(key)) {
                    const medicamento = data.medicamentos[key];
                    const option = document.createElement('option');
                    option.value = medicamento.nome;
                    option.text = medicamento.nome;
                    select.appendChild(option);
                }
            }

        })
        .catch(error => console.error('Erro ao carregar medicamentos:', error));
}
carregarMedicamentos();

function novoItem() {
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

    fetch('/item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(async response => {
        if (!response.ok) {
            throw new Error('Erro ao criar item');
        }
        window.location.href = "/item?item=" + nome;
    })
    .catch(error => {
        console.error('Erro ao criar item:', error);
    });
}

function updateItem(item, dados) {
    var url = window.location.href;
    var url = new URL(url);
    var item = url.searchParams.get("item");

    fetch('/item/'+ item, {
        method: 'PUT',
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
        window.location.href = "/item?/item=" + item;
    })
    .catch(error => {
        console.error('Erro ao adicionar medicamento:', error);
    });
}

function atualizarDados() {
    var url = window.location.href;
    var url = new URL(url);
    var item = url.searchParams.get("item");

    var medicamentoSelecionado = document.getElementById("medicamentosSelect").value;
    var quantidadeDigitada = document.getElementById("quantidadeInput").value;

    alert("Medicamento selecionado: " + medicamentoSelecionado + "\nQuantidade digitada: " + quantidadeDigitada + "\nItem: " + item);
    
    var novo_medicamento = {
        nome: medicamentoSelecionado,
        quantidade: quantidadeDigitada,
        altura: 0,
        pos: {
            "x": 0, 
            "y": 0, 
            "z": 0, 
            "r": 0
        }
    };

    fetch('/item/'+ item, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao buscar item');
        }
        return response.json();
    }).then(data => {
        let item_db = data["item"]
        item_db.medicamentos.push(novo_medicamento);
        updateItem(item, item_db);
    }).catch(error => {
        console.error('Erro ao buscar kit:', error);
    });
}