import random
import time

nomes = [
    "Maria", "Ana", "Laura", "Alice", "Valentina", "Sophia", "Helena", "Isabela", 
    "Manuela", "Júlia", "Luiza", "Giovanna", "Beatriz", "Isadora", "Mariana", 
    "Evelyn", "Camila", "Lara", "Clara", "Heloísa", "Lívia", "Emily", "Elisa", 
    "Cecília", "Larissa", "Milena", "Aurora", "Maitê", "Esther", "Rafaela", 
    "Sarah", "Elena", "Lorena", "Nicole", "Gabriela", "Emanuelly", "Rebeca", 
    "Letícia", "Analu", "Agatha", "Olívia", "Melissa", "Yasmin", "Antonella", 
    "Bianca", "Isis", "Pietra", "Maria Clara", "Isabel", "Clara","Miguel", 
    "Arthur", "Heitor", "Bernardo", "Théo", "Davi", "Gabriel", "Pedro", 
    "Samuel", "Lucas", "Benjamin", "Matheus", "Rafael", "Isaac", "Henrique", 
    "Guilherme", "Murilo", "Gustavo", "João", "Lucca", "Felipe", "Lorenzo", 
    "Vitor", "Enzo", "Vicente", "Daniel", "Leonardo", "Caio", "Eduardo", 
    "Nicolas", "Antônio", "Emanuel", "João Miguel", "Noah", "Thiago", "Yuri", 
    "Breno", "Diego", "Vinícius", "Pietro", "João Pedro", "Raul", "Francisco", 
    "Bruno", "João Lucas", "Caleb", "Tomás", "Anthony", "Davi Lucca", "Henry"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", 
    "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", 
    "Lopes", "Almeida", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", 
    "Dias", "Nunes", "Marques", "Machado", "Mendes", "Freitas", "Cardoso", 
    "Ramos", "Cavalcanti", "Teixeira", "Moreira", "Fonseca", "Nascimento", 
    "Araújo", "Campos", "Neves", "Pinto", "Cruz", "Reis", "Miranda", "Moura", 
    "Batista", "Gonçalves", "Araújo", "Borges", "Melo", "Farias", "Barros", 
    "Siqueira"
]

#INSERT RANDOM ALUNOS

verifier = []
contAlunos= 0

for i in range(50):
    rand =random.randint(1, 99)
    randSobrenome = random.randint(1,49)
    if verifier.count(nomes[rand]) <2:
        print ("INSERT INTO ALUNO VALUES(DEFAULT, '%s %s');" %(nomes[rand], sobrenomes[randSobrenome]))
        verifier.append(nomes[rand])
        contAlunos+=1
print()
print()
time.sleep(5)

#INSERT RANDOM PROFESSORES

verifier = []
cont=0
for i in range(50):
    rand =random.randint(1, 99)
    randSobrenome = random.randint(1,49)
    if verifier.count(nomes[rand]) <2:
        print ("INSERT INTO PROFESSOR VALUES(DEFAULT, '%s %s', %d);" %(nomes[rand], sobrenomes[randSobrenome],random.randint(1,10)))
        verifier.append(nomes[rand])
        cont+=1
print()
print()
time.sleep(5)


#INSERT RANDOM PROFESSORES_AULAS

for i in range(100):
    randProf = random.randint(1,cont)
    randCurso = random.randint(1,7)
    randDisc = random.randint(1,24)
    randSemestre = random.randint(1,4)
    randAno = random.randint(2000,2024)
    
    print('INSERT INTO PROFESSOR_AULAS VALUES(%d,%d,%d,%d,%d); ' %(randProf,randCurso,randDisc,randSemestre,randAno))


print()
print()
time.sleep(5)

#INSERT RANDOM ALUNOS CURSANDO

matrizCurricular= [[1,2,3,4,5,6,7],[5,8,9,10,12],[5,9,13,14,15,16],[8,17,18,19,20,21],
               [5,8,18,20,21,22,23],[5,8,18,20,21,22,23],[5,8,17,18,19,20]]

alunosCursando= []

for i in range(47):
    randCurso = random.randint(1,7)
    randSemestre = random.randint(1,4)
    randAno = random.randint(2010,2024)

    aluno =[i+1,randCurso]
    alunosCursando.append(aluno)

    luckyOne = random.randint(1,5)
    
    if luckyOne == 5:
        for j in range(len(matrizCurricular[randCurso-1])):
            randNota = random.randint(5,10)
            print('INSERT INTO ALUNOS_CURSANDO VALUES(%d,%d,%d,%d,%d,%d);' %(i+1,randCurso,matrizCurricular[randCurso-1][j]
                                                                         ,randSemestre,
                                                                         randAno,randNota))
    
    else:                                                                     
       for j in range(len(matrizCurricular[randCurso-1])):
           randNota = random.randint(0,10)
           print('INSERT INTO ALUNOS_CURSANDO VALUES(%d,%d,%d,%d,%d,%d);' %(i+1,randCurso,matrizCurricular[randCurso-1][j]
                                                                            ,randSemestre,
                                                                         randAno,randNota))

print()
print()
time.sleep(5)

#INSERT RANDOM ALUNOS TCC

professorTCC =[]
for i in range(25):
    randProfessor = random.randint(1,cont)
    professor = [i+1,randProfessor]

    professorTCC.append(professor)


for i in range(len(alunosCursando)):
    randTCC= random.randint(1,25)

    for j in range(len(professorTCC)):
        if professorTCC[j][0] == randTCC:
            print('INSERT INTO ALUNOS_TCC VALUES(%d,%d,%d,%d);' %(alunosCursando[i][0],alunosCursando[i][1],randTCC,professorTCC[j][1]))
print()
print()

#RANDOM CHEFE DE DEPARTAMENTO UPDATE
for i in range(10):
    randProfessorChefe = random.randint(1,47)

    print('UPDATE DEPARTAMENTO SET chefe_dep_id =%d where dep_id = %d;' %(randProfessorChefe,i+1))