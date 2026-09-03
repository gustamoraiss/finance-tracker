async function carregarGrafico() {
    const resposta = await fetch('/api/gastos-categoria');
    const dados = await resposta.json();
    const categorias = dados.map(item => item.categoria);
    const totais = dados.map(item => item.total);

    new Chart(document.getElementById('graficoCategorias'), {
            type: 'pie',
            data: {
                labels: categorias,
                    datasets: [{
                    data: totais
                }]
            },
            options: {
                maintainAspectRatio: false
            }
    });
}

carregarGrafico();