# LDA - Linear Discriminant Analysis #

## I.	 INTRODUÇÃO ##
Esse projeto tem como objetivo exemplificar a aplicação do algorítimo LDA, também chamado de FLD (Fisher's Linear 
Discriminant) utilizado em estatiística para reconhecimento de padrão, classificação, discriminação de classes e 
redução de dimensionalidade.

## II.	FUNDAMENTAÇÃO TEÓRICA ##

### A.	MÉTODO DOS MÍNIMOS QUADRADOS ###


## III.	METODOLOGIA ##
Para o projeto vigente foi utilizado python juntamente com o Notebook Jupyter para prototipar o modelo do
algorítimo. A base do algorítimo foi feita utilizando Numpy e o Pandas, todas as entradas de dados nos métodos da
classe é feito via DataFrames.
Tendo como base a fundamentação teórica abordada em II, o modelo do algorítimo esta proposto em <b>"./lda.py"</b>.
Para o teste e análise do algorítimo utilizou-se o dataset proposto por Fisher, Iris Dataset, na qual o objetivo é
discriminar entre três tipos de classes: Setosas, Virginicas e Versicolor; com os seguintes dados de entrada:
comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala.
Inicialmente tem-se uma abordagem dos dados de entrada puros, utilizando apenas o LDA. A segunda abordagem proposta
é a utilização de PCA (Principal Component Analisys) para redução da dimensionalidade dos dados, devido a correlação
entre os dados de entrada.

## IV. RESULTADOS ##
Os detalhes das implementações dos problemas propostos na metodologia pode ser analisados em <b>"./LDA.ipynb"</b> 
ou <b>"LDA.html"</b>.<br>
O Primeiro experimento foi feito utilizando o Iris Dataset, na qual temos a utilização do LDA para um espaço bidimensional
plotado nos gráficos a seguir.<br>
O primeiro gráfico é o resultado da redução da dimensionalidade proposta pelo LDA na qual busca maximizar a distância
entre as classes e minimizar a distância dos dados dentro da mesma classe.

![Alt text](images/ex1-graph01.png?)

O segundo gráfico plota os valores das classes em um espaço bidimensional, sem nenhum tipo de segmentação.

![Alt text](images/ex1-graph02.png?)

O terceiro gráfico plota os valores sepados em três classes utilizando o k-mean.

![Alt text](images/ex1-graph03.png?)

O segundo experimento foi feito pré-processando os dados de entrada utilizando PCA com uma, duas e três componentes
principais para, posteriormente, utilizar o LDA.

A seguir tem-se os gráficos dos experimentos seguindo a mesma ordem no primeiro experimentos.<br><br>
Utilização de uma componente principal.

![Alt text](images/ex2-pc1-graph01.png?)<br>
![Alt text](images/ex2-pc1-graph02.png?)

Utilização de duas componente principal.

![Alt text](images/ex2-pc2-graph01.png?)<br>
![Alt text](images/ex2-pc2-graph02.png?)<br>
![Alt text](images/ex2-pc2-graph03.png?)

Utilização de três componente principal.

![Alt text](images/ex2-pc3-graph01.png?)<br>
![Alt text](images/ex2-pc3-graph02.png?)<br>
![Alt text](images/ex2-pc3-graph03.png?)


## V. CONCLUSÃO ##
Dado os resultados vistos em IV podemos inferir que o LDA chegou ao resultado esperado e graficamente é possível inferir
que o erro de classificação é relativamente baixo.<br>
Como não foi utilizado nenhum indicador de performance dos métodos abordados, podemos avaliar a difenreça entre os
experimentos apenas de forma visual.<br>

Um ponto muito nítido na avaliação é que as Virginicas são muito próximas das Versicolor e que dependendo dos valores
de sépala e de pétala elas podem se confundir, porém as Setosas diferenciam-se bem dentro dos dados propostos.<br>

O dataset proposto tem dados de pétala e de sépala e seu comprimento é proporcional a largura, ou seja, são variáveis
altamente correlacionadas. Quando utiliza-se o PCA com uma componente principal, pode-se ver claramente que as classes
de Virginicas e Versicolor se confundem mais, provavelmente, devido ao fato de existirem duas variaveis com informações
relevantes para o modelo. Porém a não utilização do PCA, utilização de duas ou três componentes principais são muito
semelhante entre si, relembrando que essa inferencia é puramente qualitativa devido a não utilização de indicadores de
performance para os modelos abordados.

## VI. AGRADECIMENTOS ##

Agradecimentos especiais a CAPES e ao Centro Universitário FEI por financiar o mestrado que está em curso; 
ao professor Reinaldo Bianchi por proporcionar visões sobre o mundo acadêmico e orientar trabalhos científicos 
com o objetivo de lapidar os conhecimentos abordados em sala; aos meus pais e a minha família que sempre me 
apoiaram em meio a dificuldades.

## VII. REFERÊNCIAS ##

[1] <br>
[2]	R. Bianchi, Tópicos Especiais em Aprendizagem, 2019, ppt slide Centro Universitário FEI.