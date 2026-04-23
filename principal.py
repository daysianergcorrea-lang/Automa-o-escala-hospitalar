import pandas as pd

arquivo = "escala_planejada.xlsx"

# leitura geral
df = pd.read_excel(arquivo, header=None)

print("\nSHAPE:", df.shape)

# identificar cabeçalho
df.columns = df.iloc[5]
df = df.iloc[6:].reset_index(drop=True)

df.columns = df.columns.str.strip()

print("\nApós definir cabeçalho:")
print(df.head(10))

# ajustar os dias
linha_dias = df.iloc[0]

novas_colunas = []
for i, col in enumerate(df.columns):
    valor_dia = linha_dias.iloc[i]

    if str(valor_dia).isdigit():
        novas_colunas.append(str(valor_dia))
    else:
        novas_colunas.append(col)

df.columns = novas_colunas
df = df.iloc[1:].reset_index(drop=True)

print("\nApós ajustar dias:")
print(df.head(10))

# padronizar colunas
df.rename(columns={
    "MASP/ MATRICULA": "id",
    "NOME": "nome"
}, inplace=True)

# identificar setor

def eh_texto_setor(texto):
    if pd.isna(texto):
        return False

    texto = str(texto).strip().upper()

# ignorar lixo
    lixo = [
        "LEGENDA", "MODELO", "ATUALIZADO", "DISPONIVEL",
        "SIGLA", "SMU", "PLANEJADA", "EXECUTADA",
        "NOVEMBRO", "DEZEMBRO", "VAGA",
        "ABONO", "FALTA", "COBERT", "JORNADA"
    ]

    if any(l in texto for l in lixo):
        return False

    # ignorar números
    if any(c.isdigit() for c in texto):
        return False

    # precisa ser texto relevante
    return len(texto) > 5


setor_atual = None
setores = []

for i, row in df.iterrows():

    id_val = row["id"]
    nome_val = row["nome"]

    possivel_setor = None

    if pd.isna(nome_val) and eh_texto_setor(id_val):  # setor pode estar vinculada a  coluna matricula
        possivel_setor = id_val

    elif pd.isna(id_val) and eh_texto_setor(nome_val):   # setor pode estar vinculada a  coluna nome
        possivel_setor = nome_val

    if possivel_setor:
        setor_atual = str(possivel_setor).strip().upper()

    setores.append(setor_atual)

df["setor"] = setores

print("\nSetores detectados:")
print(df[["id", "nome", "setor"]].head(20))

# filtrar funcionários
df_func = df[
    (pd.to_numeric(df["id"], errors="coerce").notna()) &
    (df["setor"].notna())
].copy()

print("\nApenas funcionários:")
print(df_func.head(10))

# colunas de dias
colunas_dias = [c for c in df_func.columns if str(c).isdigit()]

df_func.columns = df_func.columns.str.strip()

# melt
df_melt = df_func.melt(
    id_vars=[
        "id",
        "nome",
        "setor",
        "VINCULO",
        "HORÁRIO",
        "CHS",
        "CHM",
        "JCT"
    ],
    value_vars=colunas_dias,
    var_name="dia",
    value_name="status"
)

df_melt = df_melt[df_melt["status"].notna()]

print("\nBase final para BI:")
print(df_melt.head(20))

# padronização das colunas

df_melt.columns = df_melt.columns.str.lower()

df_melt["status"] = df_melt["status"].astype(str).str.upper().str.strip()
df_melt["vinculo"] = df_melt["vinculo"].astype(str).str.upper().str.strip()
df_melt["horário"] = df_melt["horário"].astype(str).str.upper().str.strip()

# exportar
df_melt.to_excel("escala_planejada_final.xlsx", index=False)

print("\n Arquivo final gerado com sucesso!")
