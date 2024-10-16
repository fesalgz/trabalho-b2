# Trabalho para compor a B2
## Análise de Resultados:
### Responder às perguntas seguintes:
1) Como a imagem original mudou após a aplicação de cada filtro?

    R: Com a minha primeira imagem, onde vemos uma foto de cachorro com muitos ruídos, fiz a aplicação dos filtros de média, mediana e sobel. Com o filtro de Média 5x5, a imagem perdeu seus ruídos, mas suavizou muito, deixando a imagem com muito blur, tendo uma leve dificuldade de enxergar detalhes da imagem. Com o filtro de Mediana 5x5, a imagem perdeu seus ruídos, e suavizou num ponto bom, onde a gente consegue ver detalhes na imagem. Já com o filtro Sobel, temos o destaque das bordas, onde podemos observar os contornos do cachorro. <br><br> ![image](https://github.com/user-attachments/assets/4014bb66-fe1d-47d9-8686-e6dc72cb88c7) <br><br> Já com a segunda imagem, onde temos uma placa de carro desfocada, com a aplicação dos filtros de média e mediana, obtive uma imagem mais desfocada ainda, ficando cada vez mais dificil de ver, com a aplicação do filtro de Sobel, onde teve o destaque nas bordas, conseguimos entender melhor o que está escrito na placa. <br><br> ![image](https://github.com/user-attachments/assets/05014a74-5f60-490e-bf98-85ebe6619ca9)

3) Qual filtro foi mais eficaz para suavizar a imagem?

   R: Foi o filtro Gaussiano (Mediana) com um kernel de 5x5, pois ele tem uma suavização mais leve em comparação a Média, deixando mais visível os detalhes da imagem.
5) E qual foi o mais eficaz para destacar as bordas?

   R: Foi o Filtro de Sobel Combinado, onde ele destaca bem as bordas, deixando mais visível os detalhes na placa do carro, por exemplo.
6) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

   R: Para reduzir os ruídos de uma imagem e não perder muitos detalhes, o melhor filtro para uso é o Gaussiano (Mediana) com um kernel de 5x5. <br> Já para o destaque de bordas em imagens desfocadas, o melhor filtro para uso é o Sobel Combinado.

## Experimentar:
1) Experimente diferentes tipos de tamanhos de kernel nos filtros de média e mediana (por exemplo, [3,3], [5,5], etc.) e observar como isso afeta a suavização da imagem.
<br><br> R: Utilizando as mesmas imagens de exemplo, utilizando o Filtro de Média, e usando os kernels (3,3), (5,5), (10,10), conforme aumentando o kernel, mais suave a imagem fica, ficando quase impossibilitado de ver os detalhes. <br><br> ![image](https://github.com/user-attachments/assets/c28812b8-ccc8-4ae2-8499-654df70d49df)<br> ![image](https://github.com/user-attachments/assets/48cc0a07-1b70-46b7-91b3-0e8e90e55b44) <br><br> Já utilizando o Filtro Gaussiano (Mediana), utilizando os kernels (3,3), (5,5), (7,7), já temos uma suavização mais leve, mesmo com o kernel (7,7), conseguindo enxergar bem mais detalhes em comparação com o Filtro de Média. <br><br> ![image](https://github.com/user-attachments/assets/b90192ef-8f8c-4a55-be38-43e4484944a7) <br> ![image](https://github.com/user-attachments/assets/75d94eeb-3582-4d79-8ce1-a2289cde86f6)
