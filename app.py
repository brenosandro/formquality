import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="Portal de Formulários - J. Simões", layout="wide")
st.title("🗂️ Portal de Formulários - J. Simões")

# Dicionário de nomes personalizados para os formulários
nomes_personalizados = {
    "RJS8_01.py": "📄 RJS8_01 - Habilitação e Avaliação de Fornecedores",
    # Adicione mais aqui se precisar:
    # "RJS8_02.py": "📄 RJS8_02 - Ficha de Recebimento de Materiais",
}

# Sidebar: seleção de área
menu = st.sidebar.selectbox("📁 Área:", ["Qualidade", "Suprimentos"])

# Se Suprimentos for escolhido, exibe o segundo selectbox
formulario_escolhido = None

if menu == "Suprimentos":
    pasta = "Suprimentos"
    arquivos = [
        f for f in os.listdir(pasta)
        if f.endswith(".py") and not f.startswith("__")
    ]

    # Lista com nomes formatados
    nomes_exibicao = [nomes_personalizados.get(f, f"📄 {f[:-3]}") for f in arquivos]

    if nomes_exibicao:
        escolha = st.sidebar.selectbox("📄 Formulário:", nomes_exibicao)
        nome_arquivo = arquivos[nomes_exibicao.index(escolha)]
        caminho = os.path.join(pasta, nome_arquivo)
        formulario_escolhido = caminho
    else:
        st.sidebar.warning("Nenhum formulário encontrado na pasta Suprimentos.")

# Conteúdo principal da página
if menu == "Qualidade":
    st.subheader("📁 Qualidade")
    st.info("Ainda não há formulários disponíveis nesta área.")

elif menu == "Suprimentos":
    if formulario_escolhido:
        st.subheader(f"📄 Formulário Selecionado: {escolha}")
        if os.path.exists(formulario_escolhido):
            spec = importlib.util.spec_from_file_location("formulario", formulario_escolhido)
            formulario = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(formulario)
        else:
            st.error(f"❌ Arquivo não encontrado: {formulario_escolhido}")
