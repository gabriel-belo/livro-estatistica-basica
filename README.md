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











