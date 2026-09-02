def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    passo_x = 1 if dx > 0 else -1
    passo_y = 1 if dy > 0 else -1
    dx_abs = abs(dx)
    dy_abs = abs(dy)

    pixels = []
    x, y = x0, y0

    if dx_abs >= dy_abs:
        erro = 2 * dy_abs - dx_abs
        for _ in range(dx_abs + 1):
            pixels.append((x, y))
            if erro > 0:
                y += passo_y
                erro -= 2 * dx_abs
            erro += 2 * dy_abs
            x += passo_x
    else:
        erro = 2 * dx_abs - dy_abs
        for _ in range(dy_abs + 1):
            pixels.append((x, y))
            if erro > 0:
                x += passo_x
                erro -= 2 * dy_abs
            erro += 2 * dx_abs
            y += passo_y

    return pixels


def exibir_linha(pixels, titulo="", tamanho_minimo=6):
    if not pixels:
        print("Nenhum pixel.")
        return

    xs = [p[0] for p in pixels]
    ys = [p[1] for p in pixels]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    largura = max(max_x - min_x + 1, tamanho_minimo)
    altura = max(max_y - min_y + 1, tamanho_minimo)

    falta_x = largura - (max_x - min_x + 1)
    falta_y = altura - (max_y - min_y + 1)
    min_x -= falta_x // 2
    max_x += falta_x - falta_x // 2
    min_y -= falta_y // 2
    max_y += falta_y - falta_y // 2

    largura = max_x - min_x + 1
    altura = max_y - min_y + 1

    grid = [['.' for _ in range(largura)] for _ in range(altura)]
    for x, y in pixels:
        linha_grid = max_y - y
        coluna_grid = x - min_x
        if 0 <= linha_grid < altura and 0 <= coluna_grid < largura:
            grid[linha_grid][coluna_grid] = '#'

    if titulo:
        print(f"\n{titulo}")

    print("     " + " ".join(str(x) for x in range(min_x, max_x + 1)))
    for i, linha in enumerate(grid):
        y_valor = max_y - i
        print(f"{y_valor:>2}    " + " ".join(linha))
if __name__ == "__main__":
    print("=" * 50)
    print("ATIVIDADE - ALGORITMO DE BRESENHAM")
    print("=" * 50)

    pontos1 = bresenham(0, 0, 5, 2)
    exibir_linha(pontos1, titulo="1ª ESCADA: (0,0) → (5,2)  (horizontal)")

    pontos2 = bresenham(0, 0, 2, 5)
    exibir_linha(pontos2, titulo="2ª ESCADA: (0,0) → (2,5)  (vertical)")
