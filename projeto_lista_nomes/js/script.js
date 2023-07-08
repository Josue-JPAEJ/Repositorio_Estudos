let nomes = [
    "jamilton",
    "jose",
    "letícia",
    "maria",
    "carlos",
    "pedro",
    "marcela",
    "carla",
    "carlos"
]

function pesquisarNome(){

    let nomePesquisa = document.getElementById('campoNome').value
    let itensLista =''

    if (nomePesquisa !== '') {

        for (indice in nomes) {
            let nome = nomes[indice]
            if (nomePesquisa === nome) {
                itensLista += `
                <li class="list-group-item">
                    ${nome}
                </li>`
            }
        }

        if(itensLista.length === 0) {
            itensLista += `
                <li class="list-group-item">
                    Nada encontrado ;(
                </li>`
        }

        document.getElementById('lista').innerHTML = itensLista

    }else{
        alert('Insira um nome para pesquisar!')
        document.getElementById('campoNome').focus()
    }

}

function carregarNomes(){

    document.getElementById('campoNome').value =''

    let itensLista = ''

    for(indice in nomes){
        let nome = nomes[indice]
        itensLista += `
            <li class="list-group-item">
                ${nome}
            </li>`
    }

    document.getElementById('lista').innerHTML = itensLista
}