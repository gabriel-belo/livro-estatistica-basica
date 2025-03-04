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
      <li>Apsena com estes dois valores não temos ideia da simetria ou assimetria da distribuição dos dados.</li>
</ol>

Podemos definir uma medida , chamada quantil de ordem p ou p-quartil, indicada por q(p), em que p é uma proporção qualquer, 0 < p < 1.
q(0,25)= q1: 1º Quartil = 25 Percentil

q(0,5)= q2: Mediana= 2º Quartil= 50 Percentil

q(0,75)= q3: 3ºQuartil= 75 Percentil

q(0,4): 4º Decil

q(0,95): 95º Percentil

Dizemos que a mediana é resistente (ou robusta), no sentido que ela não é muito afetada pelo valor discrepante.

Se od dados estiverem agrupados em classes , podemos obter os quantis usando o histograma . Por exemplo, para obter a mediana, sabemos que ela deve corresponder ao valor da abscissa que divide a àrea do histograma em duas partes iguais(50% para cada lado).
Exemplo se pegarmos um histograma dividido em porcentagens e buscamos o ponto em que chegamos a metade dele, devemos analisar a somatória das classes, em um caso em que a soma das duas primeiras classes é igual a 61% sendo 28% da primeira barra e 33% da segunda, sabemos que a mediana esta na dentro da segunda barra. Então fazemos o cálculo:
12-8/ 33%= mediana- 8/ 22%

ou 

md-8= (22%/33%)x4

logo

md= 8+ 2.67= 10,67

O cálculo dos quantis pode ser feito de forma similar a este cálculo da mediana.
Exemplos
1.q(0,25) verificamos que 2(0,25) esta na primeira classe, pois a proporção no primeiro retângulo é 0,28.
q(0,25)- 4/ 25%= 8-4/28%

logo

q(0,25)= 4+ (25/28) x 4= 7,57

Uma medida de dispersão alternativa ao desvio padrão é a distância interquartil, definida como a diferença entre o terceiro e primeiro quartis, ou seja: dq=q3- q1.

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

Medir a dispersão central: Como o IQR exclui valores extremos, ele é mais robusto do que a amplitude total dos dados.

Exemplo de cálculo
Dado o conjunto ordenado de dados: [2,4,5,7,8,10,12,15,18,20]

Q1= 5.5 (média entre 5 e 7).
Q3= 14 (média entre 12 e 15).
IQR= 14- 5.5= 8.5
