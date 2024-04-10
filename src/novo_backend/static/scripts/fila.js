function adicionar(){
    var fila = [];
    while (true) {
        var nome = prompt("Digite o nome do kit que deseja executar ou clique em 'Cancelar' para parar: ");
        if (nome === null) {
            break;
        }
        fila.push(nome);
    }

    console.log(fila);

    var dados = {
        fila: fila
    };

    fetch('/fila', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(async response => {
        if (!response.ok) {
            throw new Error('Erro ao adicionar kit na fila');
        }
        if (response.ok) {
            alert("Kit adicionado com sucesso!");
            console.log('Kit adicionado com sucesso:', dados);
            window.location.href = "/auxiliar";
        }
    })
}