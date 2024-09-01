const PrecoDaHora = require("precodahora-api");
const client = new PrecoDaHora();

(async () => {
    const res = await client.sugestao({ item: "ABACAXI" });
    if (res.data.codigo == 80) {
        console.log("Resultado da busca para o produto: ");
        console.log(res.data.resultado);
    } else {
        console.log("Ocorreu um erro");
    }
})();

(async () => {
    const res = await client.produto({
        gtin: 7891055317303, //obrigatório
        horas: 72,
        latitude: -12.2733, //obrigatório
        longitude: -38.9556, //obrigatório
        raio: 15,
        precomax: 0,
        precomin: 0,
        ordenar: "preco.asc",
        pagina: 1,
        processo: "carregar",
        totalRegistros: 0,
        totalPaginas: 0,
        pageview: "lista",
    });
    if (res.data.codigo == 80) {
        console.log("Resultado da busca para o produto: ");
        console.log(res.data.resultado);
    } else {
        console.log("Ocorreu um erro");
    }
})();
