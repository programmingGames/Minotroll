# data base pre-defenida padrao para armazenar dados ppor enquanto
class Hysto:
    # Aqui a iniciação da instancia
    def __init__(self):
        # Tens de ir a historia do jogo e copiar paragrafos de texto e colocar em uma posição no vector
        self.text = [["Noutros tempos, nas profundezas de uma densa floresta, existia uma aldeia de trolls e golems que se  encontrava constantemente em guerra por território com os minotauros, mas o que eles não esperavam era que haveria um terceiro inimigo, que mais tarde atacou as duas aldeias, fazendo uma dizimação por completo."],
                        # exemplo ["era uma vez tata tata tata ...."]
                     ["Com esse ataque do inimigo em comum inesperado, os trolls e os minotauros quase foram exterminados do planeta, mas no meio da confusão GILIA (Mulher do comandante chefe da aldeia dos Trolls) conseguiu escapar com os seus três filhos pelas traseiras da aldeia, mas na tentativa de fuga o seu terceiro,filho, Trister, foi morto por um inimigo,  restando assim só os outros dois filhos que conseguiram fugir com ela, Golem e Graveler.  Golem o filho mais velho desde do seu nascimento os trolls constataram que ele tinha em si a alma e o poder de um guerreiro, visto que as suas habilidades como troll eram muito percetíveis."],
                     ["Durante o fuga não demorou muito para que o inimigo pegasse o rastro de Gilia e os seus filhos e, após três dias, eles foram descobertos no interior da densa floresta e foram capturados pelo inimigo que em seguida os levou a uma base. Após uma noite na base, depois de todos os maus tratos, e trabalhos forçados  Gilia morreu deixando aos seus filhos a mensagem de que eles teriam de unir forças e permanecerem fortes de modo que um dia conseguissem escapar da base, e regressar a aldeia para à reconstruir de forma prospera como de antes de ser destruida pelos inimigos"],
                     ["Depois de um tempo, Golem e Graveler já desgastados com os trabalhos forçados e com o sentimento de vingança e raiva eles escavaram durante semanas um buraco de fuga no fundo da cela onde estavam, e planearam a fuga deles muito minuciosamente. Mas no dia da fuga pelo buraco, somente Golem conseguir  escapar, isto porque, um dos guardas da base deu pela falta deles na cela. Graveler foi capturado mesmo antes de conseguir sair da parte exterior do buraco. Então Golem consegui escapar pela parte exterior da floresta, despistando os guardas, mas prometeu a si mesmo que um dia voltaria para traz em busca do seu irmão, e honraria a mensagem que a sua mãe lhes teria deixado. E no dia em que ele decidisse voltar ele estaria mais forte e com poderes suficientes para conseguir libertar Graveler."]
                     ]
        # Fazer isso ate a historia terminal e depos contar quantos vetores deu 
        # e defenir o numero de funções com o conteuda do numero de def de partes
        # expmplo 5 vetores sera igual a 5 def de partes 
        # cada def parts returnara o vector contido nessa parte
    def part1(self):
        p = self.text[1]
        return p[0]

    def part2(self):
        return self.text[2]

    def part3(self):
        return self.text[3]

    def part4(self):
        return self.text[4]

