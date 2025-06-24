from .dynamic_array import DynamicArray

def decimal_a_base_b(decimal, b):
    if decimal <= 0:
        return DynamicArray(), "0", 1
    cociente = decimal
    b_string = ""
    digitos = DynamicArray()
    while cociente > 0:
        residuo = cociente % b
        digitos.push(residuo)
        b_string = str(residuo) + b_string
        cociente = cociente // b
    return digitos, b_string, len(digitos)

def base_b_a_decimal(digitos, b):
    decimal = 0
    for i in range(len(digitos)):
        decimal += digitos.get(i) * (b ** i)
    return decimal

def suma_digitos_base_b(u, v, b):
    u_digitos, u_string, n = decimal_a_base_b(u, b)
    v_digitos, v_string, m = decimal_a_base_b(v, b)

    # Pad with zeros
    if n < m:
        for _ in range(m - n):
            u_digitos.push(0)
    elif n > m:
        for _ in range(n - m):
            v_digitos.push(0)

    max_len = max(n, m)
    k = 0  # carry
    w = DynamicArray()
    steps = []

    for i in range(max_len):
        a = u_digitos.get(i)
        b_ = v_digitos.get(i)
        s = a + b_ + k
        digit = s % b
        carry_out = 1 if s >= b else 0

        w.push(digit)

        # Pad result with None to show progress
        result_partial = [w.get(j) for j in range(len(w))] + [None] * (max_len + 1 - len(w))

        steps.append({
            "index": i,
            "highlight": i,
            "carry_in": k,
            "carry_out": carry_out,
            "u_digit": a,
            "v_digit": b_,
            "sum": s,
            "digit_result": digit,
            "result": result_partial,
            "Resumen": f"{a} + {b_} + {k} = {s} → {digit} (Acarreo {carry_out})"
        })

        k = carry_out

    # Final carry
    w.push(k)
    result_final = [w.get(j) for j in range(len(w))]

    steps.append({
        "index": max_len,
        "highlight": max_len,
        "carry_in": k,
        "carry_out": 0,
        "u_digit": 0,
        "v_digit": 0,
        "sum": k,
        "digit_result": k,
        "result": result_final,
        "summary": f"Acarreo final: {k}"
    })

    # Build final string
    w_string = "".join(str(w.get(i)) for i in reversed(range(len(w))))
    w_base10 = base_b_a_decimal(w, b)

    return {
        "steps": steps,
        "u_string": u_string,
        "v_string": v_string,
        "result_digits": result_final,
        "result_string": w_string,
        "result_decimal": w_base10,
        "u_digits": [u_digitos.get(i) for i in range(len(u_digitos))],
        "v_digits": [v_digitos.get(i) for i in range(len(v_digitos))],
        "base": b
    }
