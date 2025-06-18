import streamlit as st
from datetime import date

#st.set_page_config(page_title="Formulário de Habilitação e Avaliação de Fornecedores")
st.title("📋 Formulário de Habilitação e Avaliação de Fornecedores - J. Simões")

st.subheader("📌 Tipo de Fornecedor")
col1, col2, col3, col4, col5 = st.columns(5)
tipo_material = col1.checkbox("Material")
tipo_servico = col2.checkbox("Serviço")
tipo_projeto = col3.checkbox("Projeto")
tipo_corretor = col4.checkbox("Corretor/Imobiliária")
tipo_outros = col5.checkbox("Outros")
outro_texto = ""
if tipo_outros:
    outro_texto = st.text_input("Por favor, especifique o tipo 'Outros':", key="outro_tipo")

tipo = []
if tipo_material: tipo.append("Material")
if tipo_servico: tipo.append("Serviço")
if tipo_projeto: tipo.append("Projeto")
if tipo_corretor: tipo.append("Corretor/Imobiliária")
if tipo_outros: tipo.append(f"Outros - {outro_texto}")

with st.form("formulario"):
    st.subheader("🏢 Dados Comerciais")

    razao_social = st.text_input("Razão Social*", key="razao_social")
    nome_fantasia = st.text_input("Nome Fantasia", key="nome_fantasia")
    col1, col2 = st.columns(2)
    with col1:
        cnpj = st.text_input("CNPJ/CPF*", key="cnpj")
    with col2:
        insc_municipal = st.text_input("Inscrição Municipal", key="insc_municipal")
    col1, col2 = st.columns(2)
    with col1:
        insc_estadual = st.text_input("Inscrição Estadual", key="insc_estadual")
    with col2:
        insc_profissional = st.text_input("Inscrição Profissional (OAB, CRC, CRECI, CREA...)", key="insc_profissional")
    col1, col2 = st.columns(2)
    with col1:
        insc_inss = st.text_input("Inscrição INSS", key="insc_inss")
    with col2:
        insc_iss = st.text_input("Inscrição ISS", key="insc_iss")
    col1, col2 = st.columns([2, 1])
    with col1:
        endereco = st.text_input("Endereço*", key="endereco")
    with col2:
        numero = st.text_input("Nº*", key="numero")
    col1, col2 = st.columns(2)
    with col1:
        complemento = st.text_input("Complemento", key="complemento")
    with col2:
        cep = st.text_input("CEP*", key="cep")
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col1:
        bairro = st.text_input("Bairro*", key="bairro")
    with col2:
        cidade = st.text_input("Cidade", key="cidade")
    with col3:
        estado = st.text_input("País/UF*", key="estado")
    col1, col2, col3 = st.columns(3)
    with col1:
        telefone = st.text_input("Telefone", key="telefone")
    with col2:
        celular = st.text_input("Celular", key="celular")
    with col3:
        email = st.text_input("E-mail", key="email")

    st.subheader("👤 Dados do Representante Legal")

    representante = st.text_input("Representante Legal*", key="representante")
    col1, col2 = st.columns(2)
    with col1:
        rg = st.text_input("RG (representante legal)", key="rg")
    with col2:
        cpf_representante = st.text_input("CNPJ/CPF (representante legal)", key="cpf_representante")
    col1, col2 = st.columns(2)
    with col1:
        tipo_doc = st.text_input("Tipo de documento", key="tipo_doc")
    with col2:
        orgao_expedidor = st.text_input("Órgão Expedidor", key="orgao_expedidor")
    col1, col2 = st.columns(2)
    with col1:
        data_expedicao = st.date_input("Data de expedição", format="DD/MM/YYYY", key="data_expedicao")
    with col2:
        estado_rep = st.text_input("País/UF", key="estado_rep")
    col1, col2 = st.columns(2)
    with col1:
        estado_civil = st.text_input("Estado civil", key="estado_civil")
    with col2:
        profissao = st.text_input("Profissão", value="Administrador", key="profissao")
    col1, col2 = st.columns([2, 1])
    with col1:
        endereco_rep = st.text_input("Endereço", key="endereco_rep")
    with col2:
        numero_rep = st.text_input("Nº", key="numero_rep")
    col1, col2 = st.columns(2)
    with col1:
        complemento_rep = st.text_input("Complemento", key="complemento_rep")
    with col2:
        cep_rep = st.text_input("CEP", key="cep_rep")
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col1:
        bairro_rep = st.text_input("Bairro*", key="bairro_rep")
    with col2:
        cidade_rep = st.text_input("Cidade*", key="cidade_rep")
    with col3:
        estado_rep2 = st.text_input("País/UF", key="estado_rep2")
    col1, col2, col3 = st.columns(3)
    with col1:
        telefone_rep = st.text_input("Telefone", key="telefone_rep")
    with col2:
        celular_rep = st.text_input("Celular", key="celular_rep")
    with col3:
        email_rep = st.text_input("E-mail", key="email_rep")

    st.subheader("📄 Certificações")
    psq_sbac = st.radio("Empresa qualificada pelo PSQ ou SBAC?", ["Sim", "Não"], key="psq_sbac")

    st.subheader("📎 Documentos")
    arquivo = st.file_uploader("Anexe a ficha cadastral ou documentação complementar (PDF)", type=["pdf"], key="arquivo")

    st.subheader("📆 Finalização")
    data = st.date_input("Data de preenchimento", value=date.today(), key="data")
    responsavel = st.text_input("Responsável pelo preenchimento", key="responsavel")

    st.markdown("---")
    st.subheader("📌 Observações e Questionário Específico")

    st.markdown("""
    **OBSERVAÇÕES:**  
    Caso sua empresa seja qualificada pelo Programa Setorial da Qualidade (PSQ) ou tenha certificação no âmbito do Sistema Brasileiro de Avaliação de Conformidade (SBAC), não necessita preencher o questionário abaixo, bastando enviar a ficha cadastral.

    *Preenchimento obrigatório para emissão de contrato.*  
    **O questionário abaixo está classificado de acordo com cada fornecedor.**
    """)

    auditoria = st.radio("Fornecedor necessita ser auditado pela J. SIMÕES?", ["SIM", "NÃO"], key="auditoria_check")
    col1, col2 = st.columns(2)
    with col1:
        data_obs = st.date_input("Data", key="data_obs_check")
    with col2:
        responsavel_obs = st.text_input("Responsável pelo preenchimento", key="resp_obs_check")

    def render_radio_pergunta(label, key):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{label}**")
        with col2:
            st.radio("", ["SIM", "NÃO", "NA"], key=key, horizontal=True)

    st.markdown("### MATERIAL")
    render_radio_pergunta("1 – Sistema de Gestão da Qualidade: A empresa se compromete e assume todas as responsabilidades de fornecer o produto conforme estabelecido na ordem de compra?", "mat_check1")
    render_radio_pergunta("2 – Preservação do Produto: Existem métodos definidos de manuseio, preservação e entrega do material a fim de prevenir danos e estragos?", "mat_check2")
    render_radio_pergunta("3 – Estoque: A empresa possui estoque para atender a solicitação do pedido no máximo em 48 horas?", "mat_check3")
    render_radio_pergunta("4 – Atendimento pós-venda: O material fornecido nos dará garantia de qualidade até sua utilização (para nos resguardar de possíveis trocas)?", "mat_check4")

    st.markdown("### SERVIÇO")
    render_radio_pergunta("1 – Qualificação de fornecedores: Existem procedimentos para qualificação de seus fornecedores (fornecedores de matéria-prima)?", "serv_check1")
    render_radio_pergunta("2 – Monitoramento do processo: Após a execução do serviço, havendo alguma não conformidade, o mesmo será refeito?", "serv_check2")
    render_radio_pergunta("3 – Atendimento pós-venda: Existe alguma sistemática de atendimento ao cliente, pós-venda?", "serv_check3")
    render_radio_pergunta("4 – Treinamento: Existe uma programação de treinamento das pessoas envolvidas no desenvolvimento dos serviços?", "serv_check4")

    st.markdown("### PROJETO")
    render_radio_pergunta("1 – Qualificação de fornecedores: Sua empresa tem responsabilidade perante ao CREA pelo projeto, com habilitação a que se destina o mesmo?", "proj_check1")
    render_radio_pergunta("2 – Monitoramento do processo: Sua empresa oferece assistência técnica dos projetos a serem elaborados?", "proj_check2")
    render_radio_pergunta("3 – Atendimento pós-venda: Sua empresa assume todas as responsabilidades estabelecidas por lei inerentes ao projeto a ser elaborado?", "proj_check3")
    render_radio_pergunta("4 – Treinamento: Sua empresa compromete-se a efetuar alterações, tantas quanto forem necessárias à aprovação e execução do projeto?", "proj_check4")

    st.markdown("### CORRETORES/IMOBILIÁRIAS")
    st.text_input("1 – Principal público que atende:", key="imob_check1")
    render_radio_pergunta("2 – Infraestrutura: Sua empresa possui site próprio?", "imob_check2")
    render_radio_pergunta("3 – Possui escritório próprio para atendimento ao cliente?", "imob_check3")
    render_radio_pergunta("4 – Possui parceria com instituição bancária?", "imob_check4")
    render_radio_pergunta("5 – Comunicação: Sua empresa mantém um relacionamento contínuo com a construtora?", "imob_check5")

    enviar = st.form_submit_button("Enviar")
    if enviar:
        st.success("✅ Formulário enviado com sucesso! Os dados foram registrados.")
