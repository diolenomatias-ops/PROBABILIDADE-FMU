"""Configuração: os problemas de negócio, suas features e seus limites."""
from pathlib import Path

PASTA = Path(__file__).resolve().parent
DADOS = PASTA / "data"
MODELOS = PASTA / "models"
SEMENTE = 42  # fixa a aleatoriedade: todos obtêm os mesmos resultados


def num(padrao, minimo, maximo):
    return {"tipo": "numero", "padrao": padrao, "min": minimo, "max": maximo}


def cat(*opcoes):
    return {"tipo": "categoria", "padrao": opcoes[0], "opcoes": list(opcoes)}


PROBLEMAS = {
    "churn": {
        "titulo": "Churn de clientes",
        "tipo": "classificacao",
        "arquivo": "churn.csv",
        "alvo": "cancelou",
        "resultado": "Probabilidade de cancelamento",
        "features": {
            "idade": num(35, 18, 90),
            "meses_contrato": num(6, 0, 72),
            "tipo_contrato": cat("mensal", "anual", "bianual"),
            "pagamento": cat("boleto", "cartao", "debito_automatico", "pix"),
            "internet": cat("fibra", "dsl", "sem_internet"),
            "streaming": cat("nao", "sim"),
            "mensalidade": num(150, 10, 400),
            "chamados_suporte": num(3, 0, 30),
            "atrasos_pagamento": num(1, 0, 12),
        },
    },
    "imoveis": {
        "titulo": "Preço de imóveis",
        "tipo": "regressao",
        "arquivo": "imoveis.csv",
        "alvo": "preco",
        "resultado": "Preço estimado (R$)",
        "features": {
            "tipo": cat("apartamento", "casa"),
            "bairro": cat("Centro", "Jardins", "Vila Nova", "Beira-Mar", "Industrial"),
            "area_m2": num(80, 20, 800),
            "quartos": num(2, 1, 8),
            "banheiros": num(2, 1, 6),
            "vagas": num(1, 0, 6),
            "idade_imovel": num(10, 0, 100),
            "distancia_metro_km": num(1.5, 0, 30),
            "piscina": cat("nao", "sim"),
        },
    },
    # ---------------- NOVO: Parte 5 do exercício ----------------
    "credito": {
        "titulo": "Risco de crédito",
        "tipo": "classificacao",
        "arquivo": "credito.csv",
        "alvo": "inadimplente",
        "resultado": "Probabilidade de inadimplência",
        "limiar": 0.19,  # escolhido na Parte 4 (menor custo na validação cruzada)
        "features": {
            "idade": num(40, 18, 90),
            "renda_mensal": num(4500, 500, 100000),
            "tempo_emprego_anos": num(3, 0, 50),
            "score_credito": num(640, 300, 1000),
            "dividas_ativas": num(1, 0, 20),
            "possui_imovel": cat("nao", "sim"),
            "finalidade": cat("pessoal", "veiculo", "reforma", "educacao", "negocio"),
            "prazo_meses": num(24, 12, 60),
            "valor_emprestimo": num(15000, 500, 300000),
        },
    },
}
