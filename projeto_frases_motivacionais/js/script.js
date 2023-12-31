
function gerarFrase(){
    const frases = ["Até a jornada de mil milhas começa com um pequeno passo. – Provérbio Japonês",
                            "Só há um tempo em que é fundamental despertar. Esse tempo é agora. – Buda",
                            "A diferença entre ganhar e perder geralmente é não desistir. – Walt Disney",
                            "O homem começa a morrer na idade em que perde o entusiasmo. – Honoré de Balzac",
                            "A vida verdadeira é vivida quando pequenas mudanças acontecem. – Leo Tolstoy",
                            "A sabedoria é basicamente honestidade de pensamento. – Pam Brown",
                            "Mude a maneira como você vê as coisas e as coisas que você vê mudam. – Wayne W. Dyer",
                            "Mude seus pensamentos e mude seu mundo. – Norman Vincent Peale",
                            "Se você quiser mudar o mundo, pegue sua caneta e escreva. – Martinho Lutero",
                            "Quem olha para fora, sonha; quem olha para dentro, acorda. – Carl Jung",
                            "Se você pode sonhar, você pode fazer. – Walt Disney",
                            "Faça o que puder, com o que tiver, onde estiver. – Theodore Roosevelt",
                            "Você é muito poderoso, desde que saiba como você é poderoso. – Yogi Bhajan",
                            "Aja como se o que você faz, faz a diferença. Porque faz. – William James",
                            "Não sei aonde vou, mas já estou no caminho. – Carl Sandburg",
                            "Feliz aquele que transfere o que sabe e aprende o que ensina. – Cora Coralina",
                            "Você pode tudo se tiver entusiasmo. – Henry Ford",
                            "Cada sonho que você deixa para trás é um pedaço do seu futuro que deixa de existir. – Steve Jobs",
                            "A maior aventura que você pode viver é viver a vida dos seus sonhos. – Oprah Winfrey",
                            "Vença a si mesmo e terá vencido o seu próprio adversário. – Provérbio Japonês",
                            "Se você realmente quer que aconteça, vá atrás e não desista. – Carlos Adriano",
                            "Você não pode mudar o ontem, mas pode fazer o amanhã melhor. – Chico Xavier",
                            "Por mais longa que seja a caminhada, o mais importante é dar o primeiro passo. – Vinícius de Moraes",
                            "Acredite, você tem forças para chegar onde quiser. Basta querer. –  Valmir P. Pires",
                            "Aprenda a amar, sem esperar muito dos outros. – Augusto Cury",
                            "Seja conhecido pelo seu jeito bonito de ver a vida. – Um cartão",
                            "Imagine uma nova história para a sua vida e acredite nela. – Paulo Coelho",
                            "Tudo o que é seu encontrará uma maneira de chegar até você. – Chico Xavier",
                            "Já experimentou acreditar em você? Tente! Você não faz ideia do que é capaz. – Rogério Stankevicz",
                            "Não erramos. Apenas aprendemos. –  Anne W. Schaef",
                            "A vida tem a cor que você pinta. – Mário Bonatti",
                            "Sucesso é o que temos quando transformamos a nossa motivação em atitude. – Guilherme Machado",
                            "Duvide do que vem fácil. E não desista do que é difícil. – Vagner Frizon",
                            "Agarre suas oportunidades, pois: a capacidade pouco vale sem oportunidade. – Napoleão Bonaparte",
                            "Motivação é o que movimenta o universo a conspirar sempre ao seu favor. – Gastão V. Hecke Jr.",
                            "Sucesso é o que temos quando transformamos nossa motivação em atitude – Guilherme Machado",
                            "Adote um estilo e escolha o seu caminho. Seja você mesmo antes de tudo. – José da Cunha",
                            "Você é do tamanho do seu sonho. – Fernando Pessoa",
                            "Que não se tenha pressa, mas que também não se perca tempo. – José Saramago",
                            "Tenha novos objetivos! Mas tenha também metas para realiza-los. – Juliana Goes",
                            "Sonhe. Lute. Conquiste. Tudo é possível. Você nasceu para vencer. – Andy Orlando",
                            "Uma vida não basta ser vivida. Ela precisa ser sonhada. – Mario Quintana",
                            "No meio da dificuldade encontra-se a oportunidade. – Albert Einstein",
                            "O amor é uma força que transforma o destino. – Chico Xavier",
                            "Todas as manhãs nós nascemos de novo. O que fazemos hoje é o que mais importa. – Buda",
                            "A vida é maravilhosa se não se tem medo dela. – Charles Chaplin",
                            "Tenho em mim todos os sonhos do mundo. – Fernando pessoa",
                            "Não existe o bom ou o mau, é o pensamento que os faz assim –  William Shakespeare",
                            "Nada na vida fará você ser feliz, até que você escolha ser feliz –  Ali",
                            "Nada é tão nosso quanto os nossos sonhos – Friedrich Nietzsche"]

    let numeroAleatorio= Math.floor(Math.random() * 50)
    document.getElementById('visor').innerHTML = frases[numeroAleatorio]
}