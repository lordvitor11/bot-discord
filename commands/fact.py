from random import randint

def run():
    fatos =  [
        "Thiago é melhor que o nerd", "KITNET É RUIM", "Milena não tem sal", "O ADM é chato",
        "Carol é uma delicinha", "Ailton pedófilo", "Falta umildad no grupo", 
        "Digite PEDREIRO e veja a mágica acontecer", "Carlin é depressivo",
        "As Anas são tão presentes quanto pais de orfãos", "A mãe do Jorge é uma tremenda gostosa", 
        "O ADM bebe leite puro", "Prima foi feita pra não comer a irmã", "ADM é o gadão guerreiro", "Thigazz se delecia da mãe de ruan", 'O grelo de "certas" pessoas tem 17 cm'
    ]

    return fatos[randint(0, len(fatos) - 1)]