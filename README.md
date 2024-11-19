# Graph-Database
O projeto consiste na criação e conversação de um modelo de faculdade desenvolvido em banco de dados relacional e posteriormente convertido para um banco de dados do tipo Graph-database.

O projeto foi desenvolvido utilizando neo4j Desktop e o as arquivos csv para criação do modelo. Para execução do projeto, é preciso realizar o download dos arquivos csv do projeto anterior e mover para a pasta raiz do neo4j Desktop, dessa forma será possível realizar a conversão para modelo em grafo. Para conferência o projeto antigo realizado em modelo relacional foi deixado na pasta Projeto_Anterior caso queira exportar os arquivos você mesmo.

Para executar o projeto primeiro crie um projeto no neo4j desktop, após isso transfira todos os arquivos csv presentes na pasta extracao_csv para a pasta raiz do neo4j Desktop geralmente fica em \.Neo4jDesktop\relate-data\dbmss\<Seu_Projeto_Criado>\import caso esteja utilizando outro sistema operacional, é possível que o caminho mude, este foi o caminho utilizando windows como sistema operacional.

1- Execute cada comando cypher presente no arquivo Criacao.txt, neste arquivo estão todos os comandos cypher para leitura dos arquivos csv e criação dos nós e arestas modelo em grafo.

2 - Como o arquivo esta em formato txt, deixarei uma ordem a ser seguida para a execução dos comandos, execute cada um em ordem no prompt do neo4j Browser para que não ocorra nenhuma inconsistência na criação do modelo.

3 - Para as consultas basta executar qualquer um dos comandos presentes no arquivo Returns.txt, no arquivos existem as 5 consultas pedidas na descrição do projeto.


Integrantes do Projeto:

Vinicius Henrique Silva - 22.122.063-5

Caue Jacomini Zanatti - 22.122.024-7

luan Moreno - 22.122.076-7


