import math
from flask import render_template, request


def calcular():
    try:
        num1_valor = request.form.get("num1", "").strip()
        if not num1_valor:
            return render_template(
                "index.html",
                etapas="Informe o primeiro número.",
                resultados="",
            )

        num1 = float(num1_valor)
        operacao = request.form.get("operacao", "+")

        if operacao == "sqrt":
            if num1 < 0:
                return render_template(
                    "index.html",
                    etapas=f"Não existe raiz real de {num1}.",
                    resultados="Erro: número negativo",
                )
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado:.6g}"
            return render_template("index.html", etapas=etapas, resultados=f"{resultado:.6g}")

        if operacao == "log":
            if num1 <= 0:
                return render_template(
                    "index.html",
                    etapas=f"Logaritmo indefinido para {num1} ≤ 0.",
                    resultados="Erro: número inválido para logaritmo",
                )
            resultado = math.log10(num1)
            etapas = f"log₁₀({num1}) = {resultado:.6g}"
            return render_template("index.html", etapas=etapas, resultados=f"{resultado:.6g}")

        if operacao == "bhaskara":
            a_val = request.form.get("num1", "").strip()
            b_val = request.form.get("num2", "").strip()
            c_val = request.form.get("num3", "").strip()

            if not b_val or not c_val:
                return render_template(
                    "index.html",
                    etapas="Para Bhaskara informe a, b e c.",
                    resultados="",
                )

            a = float(a_val)
            b = float(b_val)
            c = float(c_val)

            if a == 0:
                return render_template(
                    "index.html",
                    etapas="Coeficiente 'a' não pode ser zero (não seria equação do 2º grau).",
                    resultados="Erro",
                )

            delta = b ** 2 - 4 * a * c
            etapas_linhas = [
                f"Equação: {a}x² + {b}x + {c} = 0",
                f"Δ = b² − 4ac = {b}² − 4×{a}×{c} = {delta}",
            ]

            if delta < 0:
                etapas = " | ".join(etapas_linhas) + " | Δ < 0 → sem raízes reais."
                return render_template("index.html", etapas=etapas, resultados="Sem raízes reais")

            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            if delta == 0:
                etapas_linhas.append(f"Δ = 0 → x = {x1:.6g}")
                resultado_str = f"x = {x1:.6g}"
            else:
                etapas_linhas.append(f"x₁ = (−{b} + √{delta}) / (2×{a}) = {x1:.6g}")
                etapas_linhas.append(f"x₂ = (−{b} − √{delta}) / (2×{a}) = {x2:.6g}")
                resultado_str = f"x₁ = {x1:.6g}  |  x₂ = {x2:.6g}"

            etapas = " | ".join(etapas_linhas)
            return render_template("index.html", etapas=etapas, resultados=resultado_str)

        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "index.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )

        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado:.6g}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} − {num2} = {resultado:.6g}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado:.6g}"

        elif operacao == "/":
            if num2 == 0:
                return render_template(
                    "index.html",
                    etapas="Divisão por zero é indefinida.",
                    resultados="Erro: divisão por zero",
                )
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado:.6g}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado:.6g}"

        else:
            return render_template(
                "index.html",
                etapas="Operação inválida.",
                resultados="",
            )

        return render_template("index.html", etapas=etapas, resultados=f"{resultado:.6g}")

    except ValueError:
        return render_template(
            "index.html",
            etapas="Erro: valores inválidos. Use apenas números.",
            resultados="",
        )