# Atividade: Algoritmo de Bresenham

**Disciplina:** Computação Gráfica e geoprocessamento de imagens 
**Tema:** Algoritmo de Bresenham para rasterização de linhas  
**Autor:** Eduardo dos santos prado

---

## 📌 Objetivo

Implementar o algoritmo de Bresenham para desenhar uma linha em um grid de pixels, utilizando apenas operações inteiras (soma e subtração), e visualizar a **"escadinha"** formada pelos pixels escolhidos.

---

## 🧠 O que é o algoritmo de Bresenham?

O algoritmo de Bresenham é um método eficiente para determinar quais pixels devem ser preenchidos para representar um segmento de reta em um display raster (matriz de pixels). Ele evita operações de ponto flutuante e divisões, usando apenas números inteiros, o que o torna muito rápido.

### Como funciona?

1. Calcula as diferenças `dx` e `dy` entre os dois pontos.
2. Define a direção do passo em X e Y (direita/esquerda, cima/baixo).
3. Identifica se a linha é mais horizontal ou mais vertical.
4. Usa uma **variável de erro** para decidir quando dar um passo na direção secundária, formando a "escada".

A variável de erro acumula o desvio da linha em relação à grade e, quando ultrapassa um limite, o algoritmo corrige a trajetória.

---

## 🎯 Entrada e Saída

- **Entrada:** Dois pontos `(x0, y0)` e `(x1, y1)`.
- **Saída:** Lista de pixels (coordenadas) que compõem a linha, e uma grade visual com `#` para os pixels escolhidos e `.` para o fundo.

---

## 📐 Exemplos da Atividade

A atividade pede para testar o algoritmo com dois pares de pontos:

### 1. Linha de `(0, 0)` a `(5, 2)` → **Escada mais horizontal**

```python
bresenham(0, 0, 5, 2)
