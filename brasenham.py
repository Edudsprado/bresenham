def bresenham(x0, y0, x1, y1):
    """
    Algoritmo de Bresenham para desenhar uma linha entre dois pontos.
    Retorna uma lista de pixels (coordenadas) que formam a linha.
    """
    dx = x1 - x0
    dy = y1 - y0

    passo_x = 1 if dx > 0 else -1
    passo_y = 1 if dy > 0 else -1

    dx_abs = abs(dx)
    dy_abs = abs(dy)

    pixels = [(x0, y0)]
    x, y = x0, y0

    if dx_abs >= dy_abs:  # Linha mais horizontal
        erro = 2 * dy_abs - dx_abs
        for _ in range(dx_abs):
            x += passo_x
            erro += 2 * dy_abs
            if erro > 0:
                y += passo_y
                erro += 2 * (dy_abs - dx_abs)
            pixels.append((x, y))
    else:  # Linha mais vertical
        erro = 2 * dx_abs - dy_abs
        for _ in range(dy_abs):
            y += passo_y
            erro += 2 * dx_abs
            if erro > 0:
                x += passo_x
                erro += 2 * (dx_abs - dy_abs)
            pixels.append((x, y))

    return pixels


def exibir_linha(pixels, titulo="", tamanho_minimo=6):
    """
    Mostra a linha em uma grade com '.' para fundo e '#' para os pixels.
    A grade é dimensionada para caber todos os pixels, com tamanho mínimo.
    """
    if not pixels:
        print("Nenhum pixel.")
        return

    xs = [p[0] for p in pixels]
    ys = [p[1] for p in pixels]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Garantir tamanho mínimo da grade
    largura = max(max_x - min_x + 1, tamanho_minimo)
    altura = max(max_y - min_y + 1, tamanho_minimo)

    # Distribuir espaço extra igualmente nos dois lados
    falta_x = largura - (max_x - min_x + 1)
    falta_y = altura - (max_y - min_y + 1)
    min_x -= falta_x // 2
    max_x += falta_x - falta_x // 2
    min_y -= falta_y // 2
    max_y += falta_y - falta_y // 2

    largura = max_x - min_x + 1
    altura = max_y - min_y + 1

    # Criar grid com fundo '.'
    grid = [['.' for _ in range(largura)] for _ in range(altura)]

    # Preencher os pixels da linha
    for x, y in pixels:
        linha_grid = max_y - y  # inverter Y
        coluna_grid = x - min_x
        if 0 <= linha_grid < altura and 0 <= coluna_grid < largura:
            grid[linha_grid][coluna_grid] = '#'

    # Exibir título
    if titulo:
        print(f"\n{titulo}")

    # Exibir cabeçalho com valores de X
    print("   " + " ".join(f"{x:2}" for x in range(min_x, max_x + 1)))

    # Exibir linhas com valores de Y
    for i, linha in enumerate(grid):
        y_valor = max_y - i
        print(f"{y_valor:2} " + " ".join(f" {cell}" for cell in linha))

    print("Coordenadas da escadinha:", pixels)


# --- ATIVIDADE: OS DOIS PONTOS ---
if __name__ == "__main__":
    print("=" * 50)
    print("ATIVIDADE - ALGORITMO DE BRESENHAM")
    print("As duas escadinhas:")
    print("=" * 50)

    # Primeiro ponto: (0,0) a (5,2) -> escada mais deitada
    pontos1 = bresenham(0, 0, 5, 2)
    exibir_linha(pontos1, titulo="1ª ESCADA: (0,0) → (5,2)  (mais horizontal)")

    # Segundo ponto: (0,0) a (2,5) -> escada mais em pé
    pontos2 = bresenham(0, 0, 2, 5)
    exibir_linha(pontos2, titulo="2ª ESCADA: (0,0) → (2,5)  (mais vertical)")