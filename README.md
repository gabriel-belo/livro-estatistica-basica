# livro-estatistica-basica
Estudando estatística com o livro 'Estatística básica' do Wilton Bussab e Pedro Morettin

<h2>Capítulo 2- Resumo de dados</h2>

<h3>Problemas</h3>

<h5>Exercício 6</h5>

<p>Para gerar gráficos de dispersão utilizamos a função plt.scatter(eixo x, eixo y) do matplotlib. </p>
<p>Para que o fráfico seja unidimensional, usamos [1] * len(valores do eixo x), pois geramos uma lista que repete o valor 1 de acordo com a quantidade de valores da lista no eixo x</p>


<table>
      <tr>
            <th>Tipo de Gráfico</th>
            <th>Eixo X</th>
            <th>Eixo Y</th>
            <th>Quando Usar?</th>
      </tr>
      <tr>
            <td><b>Unidimensional</b></td>
            <td>Dados numéricos</td>
            <td>Um valor fixo (ex: Y=1)</td>
            <td>Comparação simples de distribuição</td>
      </tr>
      <tr>
            <td><b>Bidimensional</b></td>
            <td>Dados numéricos</td>
            <td>Dados numéricos</td>
            <td>Análise de correlação entre duas variáveis</td>
      </tr>
</table>

<h4>Exercicio 8</h4>
<p>Podemos também apresentar Histograma Acumulativo (cumulative=True) para exibir a distribuição acumulativa e Histograma Normalizado (density=True) se quiser exibir densidade de probabilidade em vez de contagem absoluta</p>

<h5>Histograma acumulativo</h5>

<p>Agora, se fizermos um histograma acumulativo, os valores são somados progressivamente:</p>

<p>Ou seja, no histograma acumulativo, o último valor sempre representa o total de dados analisados.</p>


<h5>Histograma Normalizado (density=True)</h5>
<ul>
      <li>Em vez de contar a frequência absoluta dos valores, ele exibe a densidade de probabilidade.</li>
      <li>A área total do histograma é normalizada para 1.</li>
      <li>Útil para comparar distribuições com diferentes tamanhos de amostra.</li>
      <li>O eixo Y não mostra contagens absolutas, mas sim a densidade de probabilidade.</li>
      <li>A soma das áreas das barras será 1, garantindo que o gráfico possa ser comparado com diferentes distribuições.</li>
      
</ul>

<p>A densidade de probabilidade é um conceito da estatística que representa a probabilidade relativa de um valor ocorrer dentro de um intervalo específico, especialmente para dados contínuos</p>
<p>Em um histograma normalizado (density=True), a densidade de probabilidade no eixo Y indica quão frequente cada valor ocorre em relação ao total de dados, de modo que a área total do histograma seja 1.</p>

<h5>Como Interpretar o Histograma Normalizado?</h5>
<ul>
      <li>O eixo Y não representa a contagem bruta dos valores.</li>
      <li>A área total das barras será igual a 1.</li>
      <li>O histograma normalizado pode ser comparado a uma função de distribuição de probabilidade.</li>
      <li>Ele permite comparar diferentes distribuições independentemente do tamanho da amostra.</li>
</ul>

<h4>Cálculo para densidade de probabilidade</h4>
Densidade= FrequEñcia absoluta/Tamanho do bin×Total de Elementos
​



<h5>Histograma Acumulativo (cumulative=True)</h5>
<ul>
      <li>Em vez de contar quantos valores caem em cada bin, ele soma os valores progressivamente.</li>
      <li>Mostra quantos dados estão abaixo de um certo valor.</li>
      <li>Se normalizado (density=True), a última barra terá valor 1, indicando 100% dos dados.</li>
      <li>Útil para visualizar a função de distribuição acumulada (CDF - Cumulative Distribution Function).</li>
      <li>Cada barra soma os valores das anteriores, formando uma curva crescente.</li>
      <li>O último valor atinge o total de dados (1000 neste caso).</li>
</ul>

<table border="1">
    <thead>
        <tr>
            <th>Tipo de Frequência</th>
            <th>O que significa?</th>
            <th>Quando usar?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Frequência Absoluta</td>
            <td>Contagem direta de valores.</td>
            <td>Quando queremos saber quantas vezes um valor ocorre.</td>
        </tr>
        <tr>
            <td>Frequência Relativa</td>
            <td>Razão entre a frequência absoluta e o total de elementos.</td>
            <td>Para comparar dados de diferentes tamanhos.</td>
        </tr>
        <tr>
            <td>Frequência Acumulada</td>
            <td>Soma progressiva das frequências absolutas.</td>
            <td>Para ver quantos valores estão abaixo de um certo limite.</td>
        </tr>
    </tbody>
</table>

<h3>Exemplos Computacionais</h3>
<p>Série temporal: são dados observados em instantes ordenados de tempo. Utilizado para observar relações em instantes de tempo diferente.</p>

<h3>Problemas e complementos</h3>

<h4>Exercicio 9</h4>
<p>plt.subplot(nlinhas, ncolunas, índice)</p>
<h5>Onde:</h5>
<ul>
      <li>nlinhas → Número de linhas na grade de subplots.</li>
      <li>ncolunas → Número de colunas na grade de subplots.</li>
      <li>índice → Qual gráfico está sendo desenhado (da esquerda para a direita, de cima para baixo).</li>
</ul>

<h4>Exercício 10- Intervalos de classes desiguais</h4>
Em dados de tabela de frequência pode ocorrer do uso de classes com tamanhos desiguais que podem passar a ideia de que estas apresentam um ponto de máxima, porém por abrangerem um espaço maior elas podem ter dados dertorcidos. Então para isso criamos uma coluna de Amplitude(Δi) que nada mais é que o espaço que aquela classe ocupa no todo. O segundo passo é a construção da coluna das densidade de frequência em cada classe, que é obtida dividindo as frequências(n) pela a amplitude (Δ), ou seja, a medida que indica qual a concentração por unidade da variável.
Para gerar a porcentagem (densidade da proporção) por unidade da variavel. proporção (f) / amplitude (Δ).

<h5>Densidade de proporção</h5>

A Densidade de Proporção normaliza os valores para que a área total do histograma seja igual a 1.
​
Essa medida é útil quando queremos comparar distribuições diferentes ou visualizar os dados como uma função densidade de probabilidade (PDF).

Isso permite que possamos comparar proporcionalmente os dados.

<table>
        <thead>
            <tr>
                <th>Conceito</th>
                <th>Fórmula</th>
                <th>Uso Principal</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Densidade de Frequência</strong></td>
                <td>f / largura do intervalo</td>
                <td>Histograma com intervalos desiguais</td>
            </tr>
            <tr>
                <td><strong>Densidade de Proporção</strong></td>
                <td>freq. relativa / largura do intervalo</td>
                <td>Histograma como uma função de densidade de probabilidade</td>
            </tr>
        </tbody>
    </table>

   
    

<h4>Exercicio 12 e 13</h4>
O histograma alisado é muito útil para ilustrar rapidamente qual o tipo de comportamento que se espera para a distribuição de uma dada variável.

No matplotlib, um histograma alisado pode ser obtido utilizando Kernel Density Estimation (KDE) com a biblioteca seaborn ou scipy.stats.gaussian_kde. Isso ajuda a visualizar a distribuição dos dados sem as restrições das barras discretas de um histograma tradicional.

A biblioteca seaborn facilita a criação de um histograma alisado com a opção kde=True:

<h4>Exercício 15</h4>
Outra medida muito usada para descrever dados quatitativos é a frequência acumulada, que indica quantos elementos, ou que porcentagem deles, estão abaixo de um certo valor. Ele faz a soma de todos os valores apresentados até aquele instante e os compara em relação ao resto dos valores.

<h4>Exercicio 16</h4>
Exercício A:
Para calcular a frequência acumulada no pandas, usamos o método .cumsum(), que soma os valores de forma cumulativa.

No pandas, você pode criar uma nova coluna com os dados manipulados de uma coluna existente sem alterar a original. Para isso, pode usar métodos como .apply(), operações vetorizadas ou funções personalizadas.

Exemplo 1: Usando .apply() com uma função personalizada, Mantemos a coluna "Idade" intacta e criamos uma nova coluna "Categoria de Idade" com os valores transformados:

import pandas as pd
<h5>Criando um DataFrame exemplo</h5>
df = pd.DataFrame({
    "Idade": [25, 30, 35, 40, 45]
})

<h5>Criando uma nova coluna transformando as idades em categorias</h5>
def categorizar_idade(idade):
    if idade < 30:
        return "Jovem"
    elif idade < 40:
        return "Adulto"
    else:
        return "Sênior"

<h5>Aplicando a função e criando uma nova coluna sem alterar a original</h5>
df["Categoria de Idade"] = df["Idade"].apply(categorizar_idade)

print(df)


Exemplo 2: Usando operações vetorizadas do pandas, Isso adiciona uma nova coluna "Idade ao Quadrado" sem modificar a coluna original:
python
Copiar
Editar
df["Idade ao Quadrado"] = df["Idade"] ** 2  # Eleva cada idade ao quadrado

<h1>Cap 3- Medidas-Resumo </h1>
<h3>Moda</h3>
A moda é definida como a realização mais frequente do conjunto de valores observados. Em alguns casos, pode haver mais de uma moda, ou seja, a distribuição dos valores pode ser bimodal, trimodal etc.

A mediana é a realização que ocupa a posição central da série de observações, quando estão ordenadas em ordem crescente. Quando o número de observações for par, usa-se como mediana a média aritmética das duas observações centrais.

Média aritmética é a soma das observações dividida pelo número delas.

1º Caso: Média Simples
Se temos 𝑥1, 𝑥2,...,𝑥𝑛 como os valores de uma variável 𝑋, a média aritmética simples é calculada pela soma de todos os valores dividida pelo número total de elementos:
 
Exemplo no mundo real:
Imagine que um aluno fez cinco provas e obteve as notas: 7, 8, 6, 9 e 10. A média aritmética da nota final será:

𝑋= (7 + 8 + 6 + 9 + 10)/5= 40/5 = 8

Ou seja, a média das notas é 8.

2º Caso: Média Ponderada (Frequência Absoluta)
Se tivermos n observações da variável 𝑋, mas algumas delas se repetem, podemos reescrever a média levando em conta a frequência absoluta (𝑛𝑖), ou seja, o número de vezes que cada valor aparece. Na media ponderada usamos uma forma mais resumidade calcular valores repetidos.
Exemplo no mundo real:
Suponha que em uma sala de aula os alunos tiraram as seguintes notas:

Nota 6: 3 alunos
Nota 7: 5 alunos
Nota 8: 2 alunos
A média das notas será:

𝑋=(3 × 6) + (5 × 7) + (2 × 8) / (3 + 5 + 2) =  
X= 69/10 =6.9

Ou seja, a média das notas é 6,9.

3º Caso: Média com Frequência Relativa
Se tivermos a frequência relativa (𝑓𝑖), que representa a proporção de cada valor em relação ao total, podemos reescrever a média assim:

𝑋=𝑥1.𝑓1 + 𝑥2.𝑓2 + ⋯ + 𝑥𝑘.𝑓𝑘
 
Sendo:
      𝑓𝑖= 𝑛𝑖/𝑛


onde 𝑓𝑖 indica a frequência relativa de 𝑥𝑖 no conjunto de dados. Nesta média utilizamos a multiplicação do valor sobre sua frequencia relativa para que não deixemos de fora a relatividade do peso(quantidade) sobre o todo.

Exemplo no mundo real:
Continuando com o exemplo anterior, temos:

Nota 6: 3 alunos → 𝑓1= 3/10= 0.3

Nota 7: 5 alunos → 𝑓2= 5/10 = 0.5

Nota 8: 2 alunos → 𝑓3 = 2/10 = 0.2

Agora, aplicamos na fórmula:

𝑋= (6 × 0.3) + (7 × 0.5) + (8 × 0.2)

𝑋= 1.8 + 3.5 +1.6 = 6.9

A média continua 6,9, mas agora foi calculada com frequência relativa.

Resumo e Relação com o Mundo Real
<ul>
      <li>A média simples é usada quando todos os valores têm o mesmo peso (ex: calcular a média das notas de um aluno).</li>
      <li>A média ponderada é útil quando alguns valores aparecem mais vezes (ex: calcular a nota média de uma turma considerando quantos alunos tiraram cada nota).</li>
      <li>A média com frequência relativa é uma outra forma de ver a média ponderada, expressando os pesos em forma de proporção.</li>
</ul>

As observações ordenadas como (3,4) são chamadas de estatística de ordem.

Para calcular a moda de uma variável, precisamos apenas da distribuição de frequências (contagem). Já para a mediana necessitamos minimamente ordenar as realizações da variavel. Já a média aritmética só pode ser calculada para variáveis quantitativas.

Para as variáveis nominais podemos somente trabalhar com a moda.Para as ordinais podemos utilizar tanto moda como mediana.

O resumo de um conjunto de dados por uma única medida representativa de posição central esconde toda a informação sobre a variabilidade do conjunto de observações.

A média, moda e mediana não informão sobre suas diferentes variabilidades. Um critério frequentemente usado para tal fim é aquele que mede a dispersão dos dados em torno de sua média, e duas medidas são mais usadas: desvio médio e variância.

O princípio básico é analisar os desvios das observações em relação à média dessas observações.


<h3>O que isso significa na prática 'Para qualquer conjunto de dados, a soma dos desvios é igual a zero':</h3>
Em um conjunto de dados, os valores acima da média possuem desvios positivos e os valores abaixo da média possuem desvios negativos.
Quando somamos esses desvios, os positivos e negativos se cancelam, resultando sempre em zero.
A média é o centro de equilíbrio dos dados.

A variância é uma medida de dimensão igual ao quadrado da dimensão dos dados(por exemplo, se os dados estão expressos em cm a variância sera expressa em cm²), isto pode causar porblemas de interpretação. Então costuma-se usar, o desvio padrão que é definido como a raiz quadrada da variância.

Quando temos um conjunto de dados, podemos representá-lo por uma única medida resumo, como a média aritmética. No entanto, nem todos os valores do conjunto são exatamente iguais à média, então há um "erro" ao substituir cada valor por ela.

Esse "erro" pode ser medido pelo desvio médio (DM) ou pelo desvio padrão (DP), que indicam o quanto, em média, os valores do conjunto diferem da média.

<h3>Desvio Absoluto Mediano (DAM)</h3>
O Desvio Absoluto Mediano (DAM) é uma medida de dispersão que indica o quão distante, em média, os valores de um conjunto de dados estão da mediana.

<h4>Fórmula do DAM:</h4>

𝐷𝐴𝑀= mediana(∣ 𝑥𝑖 − 𝑋∣)
onde:

𝑥𝑖 são os valores do conjunto de dados,

𝑋 é a mediana do conjunto,

∣xi − X∣ são os desvios absolutos em relação à mediana, O DAM é a mediana desses desvios absolutos.

<h4>Passo a Passo para Calcular o DAM</h4>
Exemplo:
Conjunto de dados: 3, 6, 7, 8, 10

<h4>Passo 1: Encontrar a mediana</h4>
A mediana é o valor central dos dados ordenados.

𝑋= 7

<h4>Passo 2: Calcular os desvios absolutos</h4>

∣3−7∣=4, ∣6−7∣=1, ∣7−7∣=0, ∣8−7∣=1, ∣10−7∣=3
Os desvios absolutos são: 4, 1, 0, 1, 3

<h4>Passo 3: Calcular a mediana desses desvios</h4>
Ordenando: 0, 1, 1, 3, 4
A mediana dos desvios absolutos é 1.
DAM = 1

<h4>Por que o DAM é útil?</h4>
<ul>
      <li>Menos sensível a outliers → O DAM é mais robusto do que o desvio padrão, pois usa a mediana em vez da média, o que o torna menos afetado por valores extremos.</li>      
      <li>Melhor para dados assimétricos → Se os dados têm valores muito grandes ou muito pequenos (distribuição enviesada), o DAM pode ser mais representativo do que o desvio padrão.</li>
</ul>

Resumo: O DAM mede a dispersão dos dados em relação à mediana, sendo mais resistente a valores extremos do que o desvio padrão.


<h3>Vamos comparar Desvio Médio, Desvio Padrão e Desvio Médio em relação à Moda.</h3>
 1️⃣ Desvio Médio

✅ Vantagens:
✔️ Fácil de calcular – envolve apenas valores absolutos, sem elevar ao quadrado.
✔️ Menos sensível a valores extremos do que o desvio padrão.
✔️ Interpretável diretamente como o desvio médio em relação à média.

❌ Desvantagens:
❌ Não é matematicamente conveniente para cálculos estatísticos avançados, como regressões.
❌ Não destaca grandes variações, pois não eleva as diferenças ao quadrado.
❌ Pode não ser tão útil para distribuições muito assimétricas.

2️⃣ Desvio Padrão 

✅ Vantagens:
✔️ Mais usado em estatística e probabilidade, sendo base para distribuições como a Normal.
✔️ Dá mais peso a valores extremos, pois eleva ao quadrado as diferenças.
✔️ Matematicamente mais conveniente para cálculos estatísticos e inferências.

❌ Desvantagens:
❌ Mais difícil de interpretar intuitivamente, pois eleva ao quadrado e tira a raiz.
❌ Muito sensível a valores extremos, o que pode distorcer a análise.
❌ Pode ser menos útil em distribuições altamente assimétricas.

3️⃣ Desvio Médio em relação à Moda 

✅ Vantagens:
✔️ Útil quando a moda é uma boa medida de tendência central, como em distribuições assimétricas.
✔️ Fácil de interpretar, já que indica a dispersão em torno do valor mais frequente.
✔️ Menos afetado por valores extremos do que o desvio padrão.

❌ Desvantagens:
❌ Nem sempre a moda é representativa, especialmente se houver múltiplas modas ou se os dados forem distribuídos uniformemente.
❌ Pode ser instável, já que a moda depende da frequência mais alta e pode mudar se um valor ligeiramente diferente aparecer mais vezes.
❌ Pouco usado em estatísticas avançadas, pois a moda não tem boas propriedades matemáticas para certos cálculos.

4️⃣ Desvio Absoluto Mediano (DAM)

✅ Vantagens:
✔️ Resistente a outliers, já que usa a mediana em vez da média.
✔️ Mais representativo para distribuições assimétricas.
✔️ Mais robusto que o desvio padrão e o desvio médio tradicional.

❌ Desvantagens:
❌ Menos utilizado em estatísticas clássicas, já que o desvio padrão é mais comum.
❌ Pode ser mais difícil de calcular manualmente, pois exige ordenar os valores.
❌ Não tem a mesma interpretação estatística que o desvio padrão para distribuições normais.

<h3>Qual escolher</h3>
<ul>
      <li>Desvio Médio (DM): Para análises simples e de fácil interpretação.	</li>
      <li>Desvio Padrão (DP): Para estatísticas inferenciais, quando a distribuição for normal ou próxima de normal.</li>
      <li>Desvio Médio com Moda (DMm): Quando a distribuição for muito assimétrica(significa que os dados estão mais concentrados em um dos lados) e a moda representar melhor os dados.</li>
      <li>Desvio Absoluto Mediano (DAM): Quando há muitos outliers e se deseja uma medida mais robusta.</li>
</ul>

<h3>Assimetria em Estatística 📊</h3>
A assimetria mede o grau de distorção ou inclinação da distribuição dos dados em relação a uma distribuição simétrica (como a Normal).

Se uma distribuição for simétrica, significa que os dados estão distribuídos de maneira equilibrada em torno da média. Já se houver assimetria, significa que os dados estão mais concentrados em um dos lados.

<h4>Tipos de Assimetria</h4>
1️⃣ Assimetria Positiva (ou à direita) → "Cauda longa à direita"
📈 A cauda direita (valores maiores) é mais longa, indicando que há alguns valores muito altos puxando a média para cima.
Exemplo: Salários em uma empresa, onde poucas pessoas ganham muito mais que a maioria.
Ordem típica das medidas centrais:

Moda < Mediana < Média

2️⃣ Assimetria Negativa (ou à esquerda) → "Cauda longa à esquerda"
📉 A cauda esquerda (valores menores) é mais longa, indicando que há valores muito baixos puxando a média para baixo.
Exemplo: Notas de uma prova muito fácil, onde poucos alunos tiram notas muito baixas.
Ordem típica das medidas centrais:

Média < Mediana < Moda

3️⃣ Distribuição Simétrica (Assimetria Zero) → "Forma de sino"
🔔 A distribuição é equilibrada, sem caudas mais longas de um lado do que do outro.
Exemplo: Altura da população adulta, onde os valores estão distribuídos de maneira equilibrada.
Ordem das medidas centrais:

Média = Mediana = Moda 

Como Medir a Assimetria?
A assimetria pode ser quantificada pelo coeficiente de assimetria de Pearson:

Assimetria= 3×( Média - Mediana)/𝜎

<ul>
      <li>Se for positivo, temos assimetria positiva.</li>
      <li>Se for negativo, temos assimetria negativa.</li>
      <li>Se for próximo de zero, a distribuição é aproximadamente simétrica.</li>
</ul>

Utilizando o pandas para calcular desvio médio e padrão:

df["valores"].mad() → Calcula o desvio médio (MAD no Pandas).

df["valores"].std(ddof=0) → Calcula o desvio padrão populacional. (Se for amostral, use ddof=1.)

<h3>Exercicio 5- Problemas</h3>
<p>Eu acredito que a mediana não seja uma boa forma de medir, pois o valor central não será capaz de apresentar toda a variação presente no conjunto de dados e a média será mais ideal porém acredito que irá apresentar um número muito alto, pois a assimetria é positiva tendo muito números extremos positivos.</p>

<h4>Resposta Chat GPT</h4>
Se você quer uma medida robusta que não seja afetada pelos extremos, prefira a mediana. Se você precisa da tendência central geral, mas pode lidar com distorções, a média pode ser útil.

<h3>Exercicio 6 C- Problemas</h3>
O problema para calcular a média é que não possuimos o valor exato de filhos da última linha da tabela só sabemos que 5 famílias tem mais de 5 filhos porém não sabemos a quantidade exata.

<h3>3.3 Quartis Empíricos</h3>
Tanto a média como o desvio padrão podem não ser medidas adequadas para representar um conjunto de dados, pois:
<ol>
      <li>Sâo afetados, de forma exagerada, por valores extremos.</li>
      <li>Apenas com estes dois valores não temos ideia da simetria ou assimetria da distribuição dos dados.</li>
</ol>

Podemos definir uma medida , chamada quantil de ordem p ou p-quartil, indicada por q(p), em que p é uma proporção qualquer, 0 < p < 1.

q(0,25)= q1: 1º Quartil = 25 Percentil

q(0,5)= q2: Mediana= 2º Quartil= 50 Percentil

q(0,75)= q3: 3ºQuartil= 75 Percentil

q(0,4): 4º Decil

q(0,95): 95º Percentil

O quartil não é um grupo de números, mas sim um valor específico que divide os dados em partes iguais.

<h4>Definição Correta:</h4>
Os quartis são valores específicos que indicam os pontos de separação da distribuição de dados:
<ul>
      <li>Q1 (1º quartil, 25%): É o valor abaixo do qual 25% dos dados estão localizados.</li>
      <li>Q2 (2º quartil, 50%): É a mediana, ou seja, o valor abaixo do qual 50% dos dados estão.</li>
      <li>Q3 (3º quartil, 75%): É o valor abaixo do qual 75% dos dados estão.</li>
</ul>
✅ Os quartis são valores únicos e não um grupo de números!

Dizemos que a mediana é resistente (ou robusta), no sentido que ela não é muito afetada pelo valor discrepante.

<h3>Uma forma de contar os quartis</h3>

Fórmulas para encontrar os quartis

Se temos um conjunto de dados ordenado de tamanho 𝑛:

O Q1 está na posição  𝑃= 𝑛+1/4

​O Q2 está na posição  𝑃=2(𝑛+1)/4 (ou seja, a mediana)

O Q3 está na posição 𝑃=3(𝑛+1)/4​
 
Se a posição encontrada for um número inteiro, usamos o valor exato. Se for um número decimal, fazemos uma interpolação entre os valores vizinhos, ou seja, procuramos a media entre os valores que ocupam essas posições.

<h3>Outra forma de obter os quantis</h3>
Se os dados estiverem agrupados em classes , podemos obter os quantis usando o histograma . Por exemplo, para obter a mediana, sabemos que ela deve corresponder ao valor da abscissa que divide a àrea do histograma em duas partes iguais(50% para cada lado).
Exemplo se pegarmos um histograma dividido em porcentagens e buscamos o ponto em que chegamos a metade dele, devemos analisar a somatória das classes, em um caso em que a soma das duas primeiras classes é igual a 61% sendo 28% da primeira barra e 33% da segunda, sabemos que a mediana esta na dentro da segunda barra. Então fazemos o cálculo:
12-8/ 33%= mediana- 8/ 22%

ou 

md-8= (22%/33%)x4

logo

md= 8+ 2.67= 10,67

O cálculo dos quantis pode ser feito de forma similar a este cálculo da mediana.

Exemplos:

1.q(0,25) esta na primeira classe, pois a proporção no primeiro retângulo é 0,28.

q(0,25)- 4/ 25%= 8-4/28%

logo

q(0,25)= 4+ (25/28) x 4= 7,57

Uma medida de dispersão alternativa ao desvio padrão é a distância interquartil, definida como a diferença entre o terceiro e primeiro quartis, ou seja: dq=q3- q1. É uma medida de dispersão que indica a amplitude da faixa central dos dados. IQR = Intervalo onde estão os 50% centrais dos dados.

A distância interquartil é a diferença entre o valor que possui 25% dos valores a baixo dele sobre 

A distância interquartil (IQR - Interquartile Range) é uma medida de dispersão estatística que indica a variação central de um conjunto de dados, excluindo valores extremos. Ela é calculada como a diferença entre o terceiro quartil (𝑄3) e o primeiro quartil (𝑄1)

O que são os quartis?
Os quartis dividem um conjunto de dados ordenado em quatro partes iguais:
<ul>
      <li>𝑄1(Primeiro Quartil): É o valor abaixo do qual estão 25% dos dados.</li>
      <li>𝑄2(Mediana): É o valor central, onde 50% dos dados estão abaixo e 50% acima.</li>
      <li>𝑄3(Terceiro Quartil): É o valor abaixo do qual estão 75% dos dados.</li>
</ul>

Para que serve o IQR?

Identificar outliers: Normalmente, valores abaixo de 𝑄1−1.5×IQR ou acima de Q3+1.5×IQR são considerados outliers.

<h4>Dispersão Inferior e Superior</h4>
🔸 O exercício está pedindo para você calcular a dispersão abaixo de Q1 e acima de Q3, geralmente usadas para identificar outliers.

👉 Dispersão Inferior
É a distância entre o primeiro quartil (Q1) e o limite inferior da "área de dados aceitável".

Fórmula do limite inferior: Limite Inferior = Q1 - 1.5 × IQR

Essa região abaixo de Q1 (até o limite inferior) é chamada de dispersão inferior.

👉 Dispersão Superior

É a distância entre o terceiro quartil (Q3) e o limite superior da "área de dados aceitável".

Fórmula do limite superior: Limite Superior = Q3 + 1.5 × IQR

Essa região acima de Q3 (até o limite superior) é chamada de dispersão superior.

✅ O que isso significa na prática?
Dispersão Inferior → Parte dos dados abaixo de Q1, especialmente se caírem abaixo do limite inferior → potenciais outliers inferiores.
Dispersão Superior → Parte dos dados acima de Q3, especialmente se estiverem acima do limite superior → potenciais outliers superiores.
Medir a dispersão central: Como o IQR exclui valores extremos, ele é mais robusto do que a amplitude total dos dados.

Exemplo de cálculo
Dado o conjunto ordenado de dados: [2,4,5,7,8,10,12,15,18,20]

Q1= 5.5 (média entre 5 e 7).
Q3= 14 (média entre 12 e 15).
IQR= 14- 5.5= 8.5

Dizemos que uma medida de localização ou dispersão é resistente quando for pouco afetada por mudanças de uma pequena porção dos dados.

Os cinco valores x1, q1, q2, q3 3 xn, são importantes para ter uma boa ideia da assimetria da distribuição dos dados. Para uma distrivbuição simétrica ou aproximadamente simétrica, deveriamos ter:
<ol>
      <li>q2- x1 ≈ xn - q2</li>
      <li>q2 - q1 ≈ q3 - q2</li>
      <li>q2 - x1 ≈ xn - q3</li>
      <li>Distância entre mediana e q1, q3 menor do que  distância entre os extremos e q1.</li>
</ol>

A diferença q2- x1 é chamada disperção inferior e xn - q2 é a dispersão superior.

A primeira condição nos diz que as duas dispersões devem ser aproximadamente iguais, para uma distribuição ser aproximadamente simétrica.

<h4>Tolerância</h4>
Quando comparamos as diferenças nos quartis para verificar a simetria de uma distribuição, queremos saber se essas diferenças são próximas o suficiente. Mas o que significa "próximo" em termos numéricos?

<h4>Por que definir uma tolerância?</h4>
<ul>
      <li>Pequenas variações sempre existirão devido a flutuações nos dados.</li>
      <li>Em distribuições reais, raramente teremos valores exatamente iguais, então precisamos definir um limite aceitável de diferença.</li>
</ul>

<h4>Cálculo da Tolerância</h4>
A amplitude total dos dados é a diferença entre o maior e o menor valor: Amplitude= Xn − X1, onde:

𝑋1 é o valor mínimo (menor dado).

𝑋𝑛 é o valor máximo (maior dado).

Uma boa regra prática para definir a tolerância é considerar um percentual da amplitude total. No código, usamos 10%:

tolerancia = 0.1 * (xn - x1)  # 10% da amplitude total

Isso significa que duas diferenças serão consideradas próximas se a diferença entre elas for menor que 10% da amplitude total dos dados.

Analisando a Simetria e Assimetria nos Cálculos
Os três cálculos fornecidos podem indicar simetria ou assimetria em pontos específicos da distribuição. Cada um deles analisa uma parte diferente da estrutura dos dados, o que permite detectar onde a assimetria ocorre.

1️⃣ <h4>Mediatriz da Distribuição:</h4>

𝑞2 −𝑥1 ≈ 𝑥𝑛 − 𝑞2
​
O que esse cálculo verifica?

Compara a distância da mediana (𝑞2) até o mínimo (𝑥1) com a distância da mediana até o máximo (𝑥𝑛).
 
Se os dois valores forem aproximadamente iguais, significa que a distribuição tem simetria geral.

Se houver uma diferença significativa, sugere uma assimetria global (skewness para a esquerda ou direita).

✅ Se q2 − x1 ≈ xn − q2→ Indica que os dados são simétricos em relação à mediana.
  
⚠️ Se q2−x1 ≠ xn− q2→ Pode indicar uma cauda mais longa de um lado (distribuição assimétrica).

🔹 Exemplo de Assimetria:
Se q2 − x1for muito menor que  xn − q3, significa que os valores maiores estão mais espalhados → assimetria à direita.


2️⃣ <h4>Simetria nos Quartis:</h4> 
𝑞2 − 𝑞1 ≈ 𝑞3 − 𝑞2
 
O que esse cálculo verifica?

Compara a distância entre a mediana e o primeiro quartil (q1) com a distância entre a mediana e o terceiro quartil (𝑞3).

Se essas distâncias forem iguais, os quartis estão simetricamente distribuídos em torno da mediana.

Se forem diferentes, a distribuição é assimétrica nos valores centrais.

✅ Se  𝑞2 − 𝑞1 ≈ q3 − q2 → Os dados próximos da mediana são simétricos.
  
⚠️ Se  q2 − q1≠ q3 − q2→ Há assimetria nos valores centrais.

🔹 Exemplo de Assimetria:
Se q2 − q1 for menor que q3 − q2, significa que há mais valores concentrados no lado esquerdo → assimetria à direita.

3️⃣ Equilíbrio Entre os Extremos e os Quartis: 
𝑞2 - 𝑥1 ≈xn − q3 
O que esse cálculo verifica?

Analisa a simetria entre a parte inferior e superior da distribuição.

Compara a distância entre o mínimo (𝑥1) e a mediana (𝑞2) com a distância entre o máximo (𝑥𝑛) e o terceiro quartil (𝑞3).

✅ Se 𝑞2 - 𝑥1 ≈ xn − q3 → Os extremos e quartis estão distribuídos de forma simétrica.
   
⚠️ Se  𝑞2 − 𝑥1 ≠ xn − q3 → Há assimetria nos extremos da distribuição.

🔹 Exemplo de Assimetria:
Se q2 − x1 for menor que  xn − q3, significa que há valores extremos mais espalhados para a direita → assimetria à direita.


<h3>Box Plots</h3>
É um diagrama que representa o esquema dos cinco números

Neste diagrama consideramos um retângulo em que estão representadas a mediana e os quartis. A partir do retângulo, para cima, segue uma linha até o ponto mais remoto que não exceda LS= q3 + 1.5 * IQR(dq), limite superior. De modo similar, da parte inderior do retângulo, para baixo, segue uma linha até o ponto mais remoto que não  seja menor do que LI= q1 - 1.5 * IQR(dq), limite inferior. As observações que estiverem compreendidas acima do limite superior ou abaixo do limite inferior estabelecidos serão chamados pontos exteriores e representados por círculos ou asteriscos.

A posição central é dada pela mediana(q2) e a dispersão por dq.

Do ponto de vista estatístico, um outlier pode ser produto de um erro de obsercvação ou de arredondamento, ou simplesmente, são valores muito discrepantes.

Para dados com uma distribuição normal(simétrica), os pontos exteriores constituirão cerca de 0,7% da distribuição.

<h3>3.5 Gráficos de Simetria</h3>
Os quantis podem ser úteis para verificar se a distribuição dos dados é simétrica (ou aproximadamente simétrica)

Se um conjunto de observações for perfeitamente simétrico devemos ter:

q(0,5) - x(i) = x(n+ 1 - i) - q(0,5)

Em que i= 1,2, ..., n/2, se n for par e i= 1, 2, ..., (n+1)/2, se n for ímpar.

Se os quantis da direita esão mais afastados da mediana, do que os da esquerda, os dados serão assimétricos à direita. Se ocorrer o contrário os dados serão assimétricos a esquerda. Assimetria a direita normalmente ocorre com os números positivos.

Exemplo em código em praticas/calculoSimetria

<h3>3.6 Transformações</h3>
Vários procedimentos estatísticos são baseados na suposição de que os dados provem de uma distribuição normal (em forma de sino) ou então mais ou menos simétrica. Mas em muitas situações de interesse prático, a distribuição dos dados da amostra é assimétrico.

Se quisermos utilizar tais procedimentos, o que se propõe é efetuar uma transformação das observações, de modo a se obter uma distribuição mais simétrica e próxima da normal. Uma família de transformações frequentemente utilizada é:

A fórmula:

x^(p) = 
    x^p       , se p > 0
    ln(x)     , se p = 0
    -x^p      , se p < 0

    
Essa fórmula pertence à família das transformações de potência (ou Power Transformations), usada para:
<ul>
      <li>Corrigir a assimetria de uma distribuição de dados;</li>
      <li>Tornar dados mais parecidos com a distribuição normal (o famoso "bell curve");</li>
      <li>Melhorar a performance de modelos estatísticos ou machine learning que assumem normalidade.</li>
</ul>

A distribuição normal (ou curva de sino, "bell curve") é uma das distribuições mais importantes da estatística. Ela é simétrica, com a maior parte dos dados concentrados no centro (na média) e poucas ocorrências nos extremos (nas caudas).

Ela altera a escala dos dados de forma não linear, para que distribuições assimétricas (com caudas longas de um lado) fiquem mais simétricas. Alterar a escala de forma não linear quer dizer que você está mudando a distância entre os dados, mas não proporcionalmente.

<h4>Como ela funciona</h4>
É uma família de funções controladas por um parâmetro p que você pode ajustar para diferentes efeitos:

Quando p > 0: Você eleva os dados a uma potência p.
Exemplo:
<ul>
      <li>Se p = 0.5, você está extraindo a raiz quadrada dos valores (diminui a diferença entre valores grandes e pequenos, suavizando caudas à direita).</li>
      <li>Se p = 2, você acentua os valores grandes, alongando a cauda à direita.</li>
</ul>

Quando p = 0: Você aplica o logaritmo natural aos dados.
O log(x) suaviza bastante valores altos, puxando-os para baixo. 
Isso é útil quando você tem cauda longa à direita (assimetria positiva).


Quando p < 0: Você eleva x à potência p (como se fosse o caso positivo), mas inverte o sinal, ou seja, você reflete os valores.
Exemplo:
Se p = -1, você faz -x^-1 = -(1/x), invertendo os valores.
Essa inversão ajuda com distribuições com cauda longa à esquerda (assimetria negativa).

Normalmnete, o que se faz é experimentar valores de p na sequência:
..., -3, -2, -2, -1, -1/2, -1/3, 0, 1/3, 1/2, 1, 2, 3, ...

E para cada valor de p obtemos gráficos apropriados(histograma, box plot ...) para os dados originais e transformados, de modo a escolhermos o valor mais adequado de p.
<h4>Por que isso ajuda?</h4>
Essas transformações ajustam a curtose (achatamento) e assimetria dos dados.
Elas podem aproximar a normalidade, que é um pré-requisito para muitos procedimentos estatísticos como:
<ul>
   <li>ANOVA</li>
   <li>Regressão linear clássica</li>
   <li>Testes paramétricos</li>
</ul>


<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th>Valor de p</th>
      <th>Efeito esperado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>p &gt; 1</td>
      <td>Para distribuições assimétricas a esquerda</td>
    </tr>
    <tr>
      <td>0 &lt; p &lt; 1</td>
      <td>Diminui assimetria à direita (caudas positivas)</td>
    </tr>
    <tr>
      <td>p = 0</td>
      <td>Aplica log, reduz assimetria à direita ainda mais</td>
    </tr>
    <tr>
      <td>p &lt; 0</td>
      <td>Corrige assimetria à esquerda (caudas negativas), refletindo os dados</td>
    </tr>
  </tbody>
</table>

<h4>Isso é parte de:</h4>
<ul>
      <li>Box-Cox Transformation (requer dados positivos)</li>
      <li>Yeo-Johnson Transformation (aceita zero e valores negativos)</li>
</ul>

Ambas são versões estendidas dessa lógica de potência, usadas em estatística e machine learning!

<h3>3.8 Problemas e Complementos</h3>
<h4>Exericio 14</h4>
a)
1. Σ(𝑥𝑖−𝑥)=0
Quando aplicar?
<ul>
      <li>Essa é uma propriedade fundamental da média aritmética.</li>
      <li>Sempre é verdadeira quando você calcula a média simples de qualquer conjunto de dados.</li>
</ul>


Onde usar?
<ul>
      <li>Prova de que a média é o ponto de equilíbrio dos dados.</li>
      <li>Verificação de cálculos: quando você calcula todas as diferenças entre os valores e a média, e soma tudo, o resultado tem que ser zero.</li>
      <li>Mais conceitual, não se usa para calcular variância/desvio, mas para entender a média.</li>
</ul>

b)
2.Σ(xi− x)²= Σxi² − nx² = Σxi²− ((Σxi)²/n)

Quando aplicar?
<ul>
      <li>Para calcular a soma dos quadrados dos desvios em relação à média.</li>
      <li>Antes de calcular a variância ou o desvio padrão em um conjunto de dados simples (não agrupado).</li>
</ul>


Onde usar?
<ul>
      <li>Quando você tem todos os valores individuais 𝑥𝑖.</li>
</ul>

Você já tem:
<ul>
      <li>A soma dos valores Σ𝑥i</li>
      <li>A soma dos quadrados dos valores Σ𝑥𝑖²</li>
      <li>O número de elementos n</li>
</ul>

Atalho para variância:
Depois de calcular isso, divide por 𝑛 ou n−1 para ter a variância.

c)
3.Σni (xi - x)²  =Σni xi² − nx²

Lado esquerdo: Σni (xi - x)² 

Representa a soma dos quadrados dos desvios da média ponderada.

<ul>
      <li>É a parte bruta do cálculo para variância e desvio padrão.</li>
      <li>𝑛𝑖: frequência de cada valor 𝑥𝑖.</li>
      <li>(𝑥𝑖 − 𝑥)²: o desvio quadrado em relação à média.</li>
</ul>

d)
4.Σfi(xi − x)² =Σfi.xi²− x²

O que ela significa?
<ul>
      <li>Lado esquerdo: é a soma dos quadrados dos desvios em relação à média (ponderada pelas frequências (𝑓𝑖).</li>
      <li>Lado direito: é uma forma alternativa de calcular essa soma usando:</li>
      <ul>
            <li>Soma dos produtos das frequências pelos quadrados dos valores</li>
            <li>E o quadrado da média aritmética ponderada.</li>
      </ul>
</ul>

Importante: Essa fórmula não te dá a variância direto. Ela te dá a soma dos quadrados dos desvios.
👉 Depois você tem que dividir pelo total de frequências (n ou n−1, se for amostra) para achar a variância.

Quando usar essa fórmula?

1. Dados agrupados (com frequências): Sempre que você estiver lidando com dados agrupados em uma distribuição de frequência.

2. Para calcular a variância ou o desvio padrão de dados agrupados:
<ul>
      <li>Você vai precisar da soma dos quadrados dos desvios.</li>
      <li>Essa fórmula evita que você tenha que calcular (𝑥𝑖− x)² para cada linha da tabela.</li>
</ul>

👉 Mais prático, principalmente quando você já tem Σ𝑓ixi².
 
Lado direito (a parte que facilita a vida):Σfi.xi²− x²

👉 Representa a mesma coisa, só que sem precisar calcular os desvios um por um.
 
​<h3>Exercicio 16</h3>
<h4>Exercicio C</h4>
Fórmula do Desvio Padrão para Dados Agrupados: 𝜎 = ∑𝑓⋅(𝑥𝑖 − 𝑥)² / ∑𝑓 
​
Onde:

f = frequência absoluta de cada classe.

𝑥𝑖= ponto médio da classe. 

x = média ponderada que você já calculou (deu 51.2).

<h4>Exercicio D</h4>
O que significa a expressão x - 2s e x + 2s?

    x é a média dos dados.
    s é o desvio padrão dos dados.
    x - 2s é dois desvios padrão abaixo da média.
    x + 2s é dois desvios padrão acima da média.

🔸 Intervalo:
👉 O intervalo [x - 2s, x + 2s] representa a faixa de valores que ficam até dois desvios padrão de distância da média.

Quer saber quantos dados (ou qual a porcentagem das observações) caem dentro desse intervalo.


<h4>Exercicio 17</h4>
de acordo com valor total(n) podemos usar esta formula para descrever os quantis
Fe(xi)= i/9, dado que i= 1, 2, 3, ... 9.
Então n = 9 neste caso.

Em particular Fe(md)= F(x5)= Fe(8)= 5/9= 0,556. Portanto, ou mudamos nossa definição de mediana ou Fe(.) não pode ser usada para definir precisamente mediana ou, em geral, um quantil q(p).

Explicação do porque devemos mudar a forma com que consideramos mediana ou procurar outra forma neste caso:
Eles estão usando Fe(xi) = i / n como uma aproximação para definir a frequência acumulada.
Mas com n pequeno, como n = 9, isso não encaixa bem com o que esperamos de uma mediana.
Se você seguir essa lógica, o 5º valor já tem uma frequência acumulada de 0,556, passando do 0,5, o que pode gerar imprecisão na definição da mediana.

<h4>Exercício 20</h4>
Utilizando a função .apply() para aplicar funções def específicas sobre colunas em um data frame, exemplo:
dados['Frequência absoluta']= dados['Frequência relativa'].apply(frequenciaAbsoluta)

Utlizamos também a função findall biblioteca re para converter os valores da linhas que estavam em strings em lista com os valores separados e depois transformamos os valores em inteiros, exemplo: 
numeros = re.findall(r'\d+', intervalo)

A expressão r'\d+' procura todos os números inteiros (um ou mais dígitos) na string. \d significa "qualquer dígito de 0 a 9". + significa "um ou mais desses dígitos".


<h4>Exercicio 24 D</h4>
Calculo da média ponderada para dados agrupados:
X=∑(Xi​×fi​)/N​

Onde:
<ul>
      <li>Xi​ = Ponto médio da classe</li>
      <li>fi​ = Frequência absoluta da classe</li>
      <li>N = Total de observações (soma das frequências absolutas)</li>
</ul>


Cálculo da variância para classes agrupadas:
σ²=∑fi​(Xi​−Xˉ)²/

<h4>Exercicio 25 D</h4>
Função de distribuição acumulada(FDA):A Função de Distribuição Acumulada (FDA) de uma variável aleatória representa a probabilidade acumulada de que um valor seja menor ou igual a um determinado valor. A FDA nos dá a probabilidade cumulativa até um certo valor.

Seja X uma variável aleatória, a FDA é definida como:
F(x)=P(X≤x)

🔹 Frequência Relativa → mostra a proporção individual de cada classe.
🔹 Distribuição Acumulada → soma cumulativa das frequências relativas.

<h4>Exercício 26</h4>
Buscando a moda em em dados agrupados em classes:

classe_modal = dados.loc[dados['Frequência'].idxmax(), 'Faixa Salarial']

Aqui acontece o seguinte:
dados['Frequência'].idxmax()
🔹Retorna o índice da maior frequência.
📌 Exemplo: Como 15 é o maior valor na coluna "Frequência", o índice retornado é 1.

dados.loc[1, 'Faixa Salarial']
🔹 Localiza a classe salarial correspondente a esse índice.
📌 No exemplo, retorna "[2-4)", que é a classe modal.


<h4>Exercicio 27 D</h4>
Cálculo para percentil em dados agrupados:
Pk​=L+(((N⋅k/100)−Fa​​)/f)×h

Onde:
<ul>
      <li>Pk​ = Percentil desejado (exemplo: P25P25​ para o 1º quartil).</li>
      <li>L = Limite inferior da classe que contém o percentil.</li>
      <li>N = Total de observações (soma das frequências absolutas).</li>
      <li>k = Percentil desejado (por exemplo, 25 para P25P25​).</li>
      <li>Fa​ = Frequência acumulada antes da classe que contém o percentil.</li>
      <li>f = Frequência absoluta da classe que contém o percentil.</li>
      <li>h = Amplitude da classe.</li>
      
</ul>

<h4>Exercicio 28 B</h4>
A fórmula utilizada foi:
2dp(X)/ √​n

Significado de cada parte:
<ul>
      <li>dp(X): É o desvio padrão da variável aleatória X. Representa o grau de dispersão (ou variabilidade) dos dados em relação à média.</li>
      <li>√n : É a raiz quadrada do tamanho da amostra. O n representa o número de observações (tamanho da amostra).</li>
      <li>dp(X)/√n: É o erro padrão da média. Ele mede o quanto a média amostral tende a variar de amostra para amostra. Quanto maior a amostra, menor o erro padrão.</li>
      <li>Multiplicação por 2:
      Esse "2" é um valor aproximado correspondente ao nível de confiança de 95% em uma distribuição normal padrão. Mais precisamente, seria cerca de 1,96, mas muitas vezes arredonda-se            para facilitar os cálculos. Isso define a "largura" do intervalo de confiança.</li>
</ul>

A expressão representa a margem de erro para um intervalo de confiança de 95% da média de uma amostra.

Exemplo de aplicação dessa fórmula:

Você está medindo o tempo (em segundos) que uma lâmpada demora para acender em 10 testes.

Os tempos foram:
1.8, 2.1, 2.0, 1.9, 2.2, 2.0, 2.1, 2.0, 1.9, 2.2

Calcular média:
media= 2.02

Calcular desvio padrão amostral dp(X):
Fórmula: dp(X)=√(∑(xi​−x)2² /n−1)

No caso desvio padrão amostral= 0.1315

Então applicar na fórmula do intervalo(2dp(X)/ √​n). O resultado é 0.0832

Resultado final:

A média foi 2.02

A margem de erro (com 95% de confiança) é ±0.0832

Então, o intervalo de confiança da média é: [2.02−0.0832, 2.02+0.0832]=[1.9368, 2.1032]

Com 95% de confiança, podemos dizer que o tempo médio real para a lâmpada acender está entre 1.94 e 2.10 segundos.

<h4>Exercicio 28 C</h4>
Como adicionar o valor em cima de cada barra e explicação do código:

'''
for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)
'''

1. for bar in ax.patches:
    ax é o gráfico (AxesSubplot) criado pelo sns.barplot(...).
    ax.patches contém todas as barras desenhadas no gráfico.
    Essa linha começa um laço que percorre cada barra (bar) para adicionar o valor da frequência em cima dela.

2. height = bar.get_height()
    bar.get_height() retorna a altura da barra, que no caso de um gráfico de barras verticais, representa a frequência.
    Aqui, estamos salvando esse valor para poder usá-lo na anotação.

3. ax.annotate(...)
 Essa função escreve texto dentro do gráfico.

Vamos quebrar os parâmetros:
🗨️ f'{int(height)}'
    Esse é o texto a ser exibido — ou seja, o número da frequência.
    A função int(height) converte para número inteiro (ex: 12.0 → 12).
    O f'{}' é uma f-string do Python para interpolar variáveis.

📍 xy=(bar.get_x() + bar.get_width() / 2, height)
    Define a posição do texto dentro do gráfico.
    bar.get_x() → posição horizontal onde a barra começa.
    bar.get_width()/2 → metade da largura da barra, para centralizar o texto no meio.
    height → altura da barra → onde o topo da barra está.
🔹 Resultado: o texto vai ser colocado centralizado acima da barra.

🧭 xytext=(0, 3)
    Isso desloca o texto um pouco acima da posição real (xy) — nesse caso, 3 pixels para cima.
    0 → sem deslocamento na horizontal.
    3 → deslocamento vertical positivo (mais alto que o topo da barra).

🗺️ textcoords="offset points"
    Diz ao matplotlib que o deslocamento xytext deve ser feito em pontos (pixels) a partir do ponto original (xy).

📐 ha='center'
    Horizontal alignment → centraliza o texto horizontalmente.

📏 va='bottom'
    Vertical alignment → alinha o texto pela base (embaixo), útil para que o texto cresça para cima.

🖋️ fontsize=10
    Define o tamanho da fonte do texto.



<h4>Exercicio 33</h4>
Ao fazer uma query para utilizar variáveis externas é necessário adicionar um @ a frente delas e é possível adicionar mais de uma condição a query.
