def best_fit(mem_avail, req_size, index):
    if not mem_avail:
        return None

    memoria_copia = mem_avail[:]
    BestPos = -1  
    minor = float('inf')
    totalB = len(memoria_copia)

    # 🔹 Cambio: Se usa `for` en lugar de `while`
    for contador in range(totalB):
        idx = (index + contador) % totalB
        dir_inicio, dir_fin = memoria_copia[idx]

        # 🔹 Cambio: Reorganización de la condición lógica
        if dir_fin < req_size:
            continue  

        if dir_fin < minor:
            BestPos = idx
            minor = dir_fin

    if BestPos == -1:
        return None

    dir_inicio, dir_fin = memoria_copia[BestPos]
    nueva_dir_inicio = dir_inicio
    nueva_dir_fin = dir_fin - req_size

    # 🔹 Cambio: Uso de `if memoria_copia:` en lugar de `if len(memoria_copia) > 0:`
    if nueva_dir_fin == 0:
        del memoria_copia[BestPos]

        BestPos = BestPos % len(memoria_copia) if memoria_copia else 0
    else:
        memoria_copia[BestPos] = (dir_inicio + req_size, nueva_dir_fin)

    return memoria_copia[:], nueva_dir_inicio, req_size, BestPos

