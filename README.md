# Processamento-de-Imagens

Repositório para projetos de Processamento de Imagens Digitais

<details><summary>Projeto 1: Inversão de Pixels</summary>

- O código do projeto 1 realiza a inversão dos pixels de uma imagem.
- Exemplos de valores de pixels:

   0 => 255

   255 >= 0

   10 => 245

   245 => 10

   *Não se esqueçam que os valores de tons de cinza não podem ser negativos.*


</details>

<details><summary>Projeto 2: Relacionamento entre Pixels - Operações espaciais por vizinhança</summary>

   Foi aplicado um filtro de média com o objetivo de borrar a imagem.


</details>

<details><summary>Projeto 3: Relacionamento entre Pixels - Transformações geométricas </summary>

   Através das transformações geométricas: foi rotacionado a imagem em 45°, foi dado um zoom na imagem e também foi possível cortar a imagem.


</details>


<details><summary>Projeto 4: Equalização Histograma + Filtro mediana
 </summary>

   Primeiramente foi calculado o histograma normalizado da imagem. A normalização é realizada dividindo a frequência de cada compartimento pelo número total de pixels na imagem.
   A seguir foi derivado uma tabela de pesquisa que mapeia as intensidades de pixel para obter características de histograma equalizadas. 
   Depois que a tabela de pesquisa é derivada, a intensidade de todos os pixels na imagem é mapeada para os novos valores. O resultado é uma imagem equalizada.
   A saída da equalização do histograma para as duas imagens estão salvas na pasta Images, tal como a imagem original.
   Para cada resultado, as duas imagens superiores mostram as imagens originais e equalizadas. A melhora no contraste é claramente observada. 
   As duas imagens inferiores mostram o histograma e o histograma cumulativo, comparando as imagens originais e equalizadas. 
   Após a equalização do histograma, as intensidades dos pixels são distribuídas por toda a faixa de intensidade. 
   Os histogramas cumulativos estão aumentando linearmente conforme o esperado, enquanto exibem um padrão de escada. 
   Isso é esperado, pois as intensidades de pixel da imagem original foram ampliadas para uma faixa mais ampla. 
   Isso cria lacunas de categorias com frequência zero entre categorias adjacentes diferentes de zero, aparecendo como uma linha plana no histograma cumulativo.


</details>

