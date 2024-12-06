import copy
import matplotlib.pyplot as plt
import csv
import numpy as np
from regioes_rn import agreste, leste, oeste, central

ANOS = range(2007, 2025, 2)


def get_all_cidades():
    """
    Número de cidades constante cada ano
    """
    filename = "Ideb municipios RN - 2007.csv"
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        cidades = set([row["cidade"] for row in reader])
    return cidades


def get_pior_ano(ano):
    filename = f"Ideb municipios RN - {ano}.csv"
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        pior_nota = 10
        pior_cidades = []
        for row in reader:
            if "-" in row["ideb"]:
                continue
            nota = float(row["ideb"].replace(",", "."))
            if nota < pior_nota:
                pior_nota = nota
                pior_cidades = [row["cidade"]]
            elif nota == pior_nota:
                pior_cidades.append(row["cidade"])
    return pior_cidades, pior_nota


def get_melhor_ano(ano):
    filename = f"Ideb municipios RN - {ano}.csv"
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        melhor_nota = 0
        melhor_cidades = ""
        for row in reader:
            if "-" in row["ideb"]:
                continue
            nota = float(row["ideb"].replace(",", "."))
            if nota > melhor_nota:
                melhor_nota = nota
                melhor_cidades = [row["cidade"]]
                print("NOVA", melhor_nota)
            elif nota == melhor_nota:
                print("IGUAL", melhor_nota)
                melhor_cidades.append(row["cidade"])
    print("--")
    return melhor_cidades, melhor_nota


def get_maior_crescimento_periodo():
    primeiro = 2007
    ultimo = 2023
    notas_iniciais = {}
    notas_finais = {}
    with open(f"Ideb municipios RN - {primeiro}.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "-" in row["ideb"]:
                continue
            notas_iniciais[row["cidade"]] = float(row["ideb"].replace(",", "."))
    with open(f"Ideb municipios RN - {ultimo}.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "-" in row["ideb"]:
                continue
            notas_finais[row["cidade"]] = float(row["ideb"].replace(",", "."))
    maior_crescimento = 0
    cidade_maior_crescimento = ""
    menor_crescimento = 10
    cidade_menor_crescimento = ""
    for cidade in notas_iniciais:
        if cidade not in notas_finais:
            continue
        crescimento = notas_finais[cidade] - notas_iniciais[cidade]
        if crescimento > maior_crescimento:
            maior_crescimento = crescimento
            cidade_maior_crescimento = cidade

        if crescimento < menor_crescimento:
            menor_crescimento = crescimento
            cidade_menor_crescimento = cidade
    return (
        cidade_maior_crescimento,
        maior_crescimento,
        cidade_menor_crescimento,
        menor_crescimento,
    )


def get_cidades_cairam_pandemia():
    ano_inicial = 2019
    ano_final = 2021
    notas_iniciais = {}
    notas_finais = {}
    nao_aplicaram = []
    with open(f"Ideb municipios RN - {ano_inicial}.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "-" in row["ideb"]:
                continue
            notas_iniciais[row["cidade"]] = float(row["ideb"].replace(",", "."))
    with open(f"Ideb municipios RN - {ano_final}.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "-" in row["ideb"]:
                continue
            notas_finais[row["cidade"]] = float(row["ideb"].replace(",", "."))
    cidades_cairam = []
    for cidade in notas_iniciais:
        if cidade not in notas_finais:
            nao_aplicaram.append(cidade)
            continue
        if notas_finais[cidade] < notas_iniciais[cidade]:
            cidades_cairam.append(cidade)
    return cidades_cairam, nao_aplicaram


def get_media_simples_ano(ano, cidades=[]):
    filename = f"Ideb municipios RN - {ano}.csv"
    notas = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if cidades and row["cidade"] not in cidades:
                continue
            if "-" in row["ideb"]:
                continue
            notas.append(float(row["ideb"].replace(",", ".")))
    return round(float(np.mean(notas)),1)


def get_desvio_padrao_ano(ano):
    filename = f"Ideb municipios RN - {ano}.csv"
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        notas = []
        for row in reader:
            if "-" in row["ideb"]:
                continue
            notas.append(float(row["ideb"].replace(",", ".")))
    return float(np.std(notas))


def get_data_ano(ano):
    filename = f"Ideb municipios RN - {ano}.csv"
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def progresso_ideb_cidade(cidade):
    anos = range(2007, 2025, 2)
    dados_ano = [get_data_ano(ano) for ano in anos]
    notas_cidade = []
    for ano in dados_ano:
        for linha in ano:
            if linha["cidade"] == cidade:
                if "-" in linha["ideb"]:
                    notas_cidade.append(np.nan)
                else:
                    notas_cidade.append(float(linha["ideb"].replace(",", ".")))
                break
    return notas_cidade


def plot_progresso_cidades(notas_cidades, com_desvio=False):
    anos = ANOS
    for cidade, notas_cidade in notas_cidades.items():
        ultima_nota = notas_cidade[-1]
        primeira_nota = notas_cidade[0]
        crescimento_percentual = ((ultima_nota - primeira_nota) / primeira_nota) * 100
        crescimento_percentual = round(crescimento_percentual, 2)
        plt.plot(
            anos,
            notas_cidade,
            marker="o",
            label=f"{cidade} +{crescimento_percentual}%",
            alpha=0.7,
        )
        for i, nota in enumerate(notas_cidade):
            plt.text(anos[i], nota, f"{nota}", fontsize=9, ha="right", color="black")
    media_anos = [get_media_simples_ano(ano) for ano in anos]
    primeira_nota = media_anos[0]
    ultima_nota = media_anos[-1]
    crescimento_percentual = ((ultima_nota - primeira_nota) / primeira_nota) * 100
    crescimento_percentual = round(crescimento_percentual, 2)
    plt.plot(
        anos,
        media_anos,
        marker="o",
        label=f"Média RN +{crescimento_percentual}%",
        color="black",
        linestyle="--",
        alpha=0.7,
    )
    for i, media in enumerate(media_anos):
        plt.text(
            anos[i], media, f"{round(media,1)}", fontsize=9, ha="right", color="black"
        )
    if com_desvio:
        desvio_padrao = [get_desvio_padrao_ano(ano) for ano in ANOS]
        plt.fill_between(
            anos,
            np.array(media_anos) - np.array(desvio_padrao),
            np.array(media_anos) + np.array(desvio_padrao),
            color="gray",
            alpha=0.1,
            label="Área do Desvio Padrão",
        )
    plt.title("Progresso do IDEB em cidades do RN")
    plt.xlabel("Ano")
    plt.ylabel("Nota IDEB")
    plt.xticks(anos)
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()


def plot_pior_melhor_por_ano():
    anos = ANOS
    piores = []
    melhores = []
    for ano in anos:
        pior_cidade, pior_nota = get_pior_ano(ano)
        melhor_cidade, melhor_nota = get_melhor_ano(ano)
        piores.append(pior_nota)
        melhores.append(melhor_nota)
    plt.plot(anos, piores, marker="o", label="Pior nota")
    plt.plot(anos, melhores, marker="o", label="Melhor nota")
    plt.title("Pior e melhor nota do IDEB no RN")
    plt.xlabel("Ano")
    plt.ylabel("Nota IDEB")
    plt.xticks(anos)
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()


def plot_casos_borda():
    piores_por_ano = [get_pior_ano(ano) for ano in range(2007, 2025, 2)]
    print(piores_por_ano)
    melhores_por_ano = [get_melhor_ano(ano) for ano in range(2007, 2025, 2)]
    piores_cidades = [cidade for cidade, nota in piores_por_ano]
    piores_valores = [nota for cidade, nota in piores_por_ano]
    melhores_cidades = [cidade for cidade, nota in melhores_por_ano]
    melhores_valores = [nota for cidade, nota in melhores_por_ano]
    plt.plot(
        ANOS, piores_valores, label="Pior do Ano", marker="o", color="red", alpha=0.5
    )
    for i, cidade in enumerate(piores_cidades):
        plt.text(
            ANOS[i],
            piores_valores[i],
            f"{','.join(cidade)} ({piores_valores[i]})",
            fontsize=9,
            ha="right",
            color="black",
        )

    # Linha para os melhores casos
    plt.plot(
        ANOS,
        melhores_valores,
        label="Melhor do Ano",
        marker="o",
        color="green",
        alpha=0.5,
    )
    for i, cidade in enumerate(melhores_cidades):
        plt.text(
            ANOS[i],
            melhores_valores[i],
            f"{','.join(cidade)} ({melhores_valores[i]})",
            fontsize=9,
            ha="left",
            color="black",
        )
    media_anos = [get_media_simples_ano(ano) for ano in ANOS]
    for i, media in enumerate(media_anos):
        plt.text(
            ANOS[i] + 0.2,
            media - 0.2,
            f"Média ({round(media,1)})",
            fontsize=9,
            ha="left",
            color="black",
        )
    plt.plot(
        ANOS,
        media_anos,
        marker="o",
        label="Média RN",
        color="black",
        linestyle="--",
        alpha=0.6,
    )
    plt.title("Piores e Melhores Casos por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Nota IDEB")
    plt.legend()
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.xticks(ANOS)
    plt.show()

def quantas_cidades_melhoraram():
    notas_iniciais = {}
    notas_finais = {}
    for ano in range(2007, 2025, 2):
        filename = f"Ideb municipios RN - {ano}.csv"
        melhores = 0
        notas_iniciais = copy.deepcopy(notas_finais)
        notas_finais = {}
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "-" in row["ideb"]:
                    continue
                notas_finais[row["cidade"]] = float(row["ideb"].replace(",", "."))
                if row["cidade"] in notas_iniciais:
                    if notas_finais[row["cidade"]] > notas_iniciais[row["cidade"]]:
                        melhores += 1
            print(f"{ano}: {melhores}")

# # Cidades importantes
# cidades_importantes = ["Natal", "Mossoró", "Parnamirim", "São Gonçalo do Amarante", "Macaíba", "Ceará-Mirim", "Extremoz", "Caicó", "Açu"]
# plot_progresso_cidades(
#     {cidade: progresso_ideb_cidade(cidade) for cidade in cidades_importantes}
# )

# # Cidades importantes com desvio
# cidades_importantes = [
#     "Natal",
#     "Mossoró",
#     "Parnamirim",
#     "São Gonçalo do Amarante",
#     "Macaíba",
#     "Ceará-Mirim",
#     "Extremoz",
#     "Caicó",
#     "Açu",
# ]
# plot_progresso_cidades(
#     {cidade: progresso_ideb_cidade(cidade) for cidade in cidades_importantes},
#     com_desvio=True,
# )

# Pior e melhor
# plot_casos_borda()

# # Maior e menor crescimento
# data = get_maior_crescimento_periodo()
# plot_progresso_cidades(
#     {data[0]: progresso_ideb_cidade(data[0]), data[2]: progresso_ideb_cidade(data[2])}
# )

# # Cidades que caíram na pandemia
# cidades, nao_aplicaram = get_cidades_cairam_pandemia()
# print(len(cidades), len(nao_aplicaram))

# media_anos = [get_media_simples_ano(ano) for ano in ANOS]
# for i, media in enumerate(media_anos):
#     if i == 0:
#         continue
#     crescimento = ((media - media_anos[i-1]) / media_anos[i-1]) * 100
#     print(f"{ANOS[i]}: {media} {crescimento:.2f}%")

# desvios = [round(get_desvio_padrao_ano(ano), 2) for ano in ANOS]
# print(desvios)

# # Cidades importantes
# cidades_importantes = [
#     "Natal",
#     "Mossoró",
#     "Parnamirim",
#     "São Gonçalo do Amarante",
#     "Macaíba",
#     "Ceará-Mirim",
#     "Extremoz",
#     "Caicó",
#     "Açu",
# ]
# plot_progresso_cidades(
#     {
#         "Agreste": [get_media_simples_ano(ano, cidades=agreste) for ano in ANOS],
#         "Leste": [get_media_simples_ano(ano, cidades=leste) for ano in ANOS],
#         "Oeste": [get_media_simples_ano(ano, cidades=oeste) for ano in ANOS],
#         "Central": [get_media_simples_ano(ano, cidades=central) for ano in ANOS],
#     },
# )


#quantas_cidades_melhoraram()