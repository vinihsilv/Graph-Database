create sequence cod_disci start with 1;
CREATE TABLE DISCIPLINAS (
    cod_disc int NOT NULL DEFAULT nextval('cod_disci'),
    nome_disc varchar(255),
    PRIMARY KEY (cod_disc)
);

create sequence cod_curso start with 1;
create table CURSOS(
cod_curso int NOT NULL DEFAULT nextval('cod_curso'),
nome_curso varchar (255),
primary key (cod_curso)
);

CREATE TABLE MATRIZ_CURSOS (
    cod_curso serial NOT NULL,
    cod_disc serial NOT NULL,
    FOREIGN KEY (cod_curso) REFERENCES CURSOS(cod_curso),
    FOREIGN KEY (cod_disc) REFERENCES DISCIPLINAS(cod_disc)
);

create sequence id_aluno start with 1;
create table ALUNO(
id_alunos int NOT NULL DEFAULT nextval('id_aluno'),
nome_aluno varchar(255),

primary key(id_alunos)

);

create sequence dep_id start with 1;
CREATE TABLE DEPARTAMENTO (
    dep_id int NOT NULL DEFAULT nextval('dep_id'),
    nome_dep VARCHAR(255),
    chefe_dep_id INT,
    PRIMARY KEY (dep_id)
);

create sequence id_professor start with 1;
create table PROFESSOR(
id_professor int NOT NULL DEFAULT nextval('id_professor'),
nome_professor varchar (255),
dep_id int,

foreign key(dep_id) references DEPARTAMENTO(dep_id),
primary key(id_professor)

);


CREATE TABLE PROFESSOR_AULAS (
    id_professor INT NOT NULL,
    id_curso INT NOT NULL,
    cod_disc INT NOT NULL,
    semestre INT NOT NULL,
    ano INT NOT NULL,
    
    PRIMARY KEY (id_professor, id_curso, cod_disc, semestre, ano),
    FOREIGN KEY (id_professor) REFERENCES PROFESSOR(id_professor),
    FOREIGN KEY (id_curso) REFERENCES CURSOS(cod_curso),
    FOREIGN KEY (cod_disc) REFERENCES DISCIPLINAS(cod_disc)
);

CREATE TABLE ALUNOS_CURSANDO (
    id_aluno INT NOT NULL,
    id_curso INT NOT NULL,
    cod_disc INT NOT NULL,
    semestre INT NOT NULL,
    ano INT NOT NULL,
    nota INT NOT NULL,
    PRIMARY KEY (id_aluno, id_curso, cod_disc, semestre, ano),
    FOREIGN KEY (id_aluno) REFERENCES ALUNO(id_alunos),
    FOREIGN KEY (id_curso) REFERENCES CURSOS(cod_curso),
    FOREIGN KEY (cod_disc) REFERENCES DISCIPLINAS(cod_disc)
);

CREATE TABLE ALUNOS_TCC (
    id_aluno INT NOT NULL,
    cod_curso INT NOT NULL,
    id_tcc INT NOT NULL,
    id_professor INT NOT NULL,
    PRIMARY KEY (id_aluno, cod_curso, id_professor, id_tcc),
    FOREIGN KEY (id_aluno) REFERENCES ALUNO(id_alunos),
    FOREIGN KEY (cod_curso) REFERENCES CURSOS(cod_curso),
    FOREIGN KEY (id_professor) REFERENCES PROFESSOR(id_professor)
);

ALTER TABLE DEPARTAMENTO
ADD CONSTRAINT fk_chefe_dep FOREIGN KEY (chefe_dep_id) REFERENCES PROFESSOR(id_professor);