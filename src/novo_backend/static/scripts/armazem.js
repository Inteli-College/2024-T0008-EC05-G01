function carregarKits(){
    var url = window.location.href;
    var url = new URL(url);
    var kit = url.searchParams.get("kit");
    
    fetch('/kits/'+ kit, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao buscar kit');
        }
        return response.json();
    }).then(data => {
        let kit_db = data["kit"]
        kit_db.medicamentos.forEach(medicamento => {
            console.log(medicamento)});
    }).catch(error => {
        console.error('Erro ao buscar kit:', error);
    });
}