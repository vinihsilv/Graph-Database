--SELECT 1

select ac.id_aluno, a.nome_aluno, ac.cod_disc,d.nome_disc , ac.ano, ac.nota  from alunos_cursando ac join aluno a 
on a.id_alunos = ac.id_aluno join disciplinas d on
ac.cod_disc = d.cod_disc;

--SELECT 2
select pa.id_professor , p.nome_professor , pa.cod_disc ,d.nome_disc ,pa.semestre ,pa.ano  
from professor_aulas pa join professor p 
on p.id_professor = pa.id_professor 
join disciplinas d 
on d.cod_disc = pa.cod_disc;

--SELECT 3
select AC.ID_ALUNO, a.nome_aluno ,d.cod_disc ,d.nome_disc, ac.ano, ac.semestre , ac.nota
from alunos_cursando AC join aluno a 
on ac.id_aluno = a.id_alunos join disciplinas d 
on d.cod_disc = ac.cod_disc
where NOTA>5;

--SELECT 4
select p.id_professor , p.nome_professor , d.dep_id , d.nome_dep  from departamento d 
join professor p 
on d.chefe_dep_id = p.id_professor; 

--SELECT 5
select a.id_alunos , a.nome_aluno , p.id_professor ,p.nome_professor ,at.id_tcc
from alunos_tcc at join aluno a 
on a.id_alunos = at.id_aluno join professor p 
on p.id_professor = at.id_professor;