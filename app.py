import streamlit as st
import pandas as pd
from modelo import X, y, model_rf

st.set_page_config(
    page_title="Preditor de diabetes",
    page_icon = "favicon.ico"
)

st.title("Preditor de diabetes")

#sexo
sexo_options = ["", "Masculino", "Feminino"]
sexo_dict = {"Masculino": 0, "Feminino": 1}
sexo = st.selectbox("Selecione o sexo:", sexo_options)

# Idade
idade = st.slider("Idade do paciente", 1, 100, 25)

#IMC
altura = st.number_input("Digite a altura em metros", min_value=0.5, max_value=2.2, value=1.70)
peso = st.number_input("Digite o peso em kg", min_value=10.0, max_value=170.0, value=70.0, step=1.0)

#Diabetes na família
familia_diabetes_options = ["", "Não", "Sim"]
familia_diabetes_dict = {"Não": 0, "Sim": 1}
familia_diabetes = st.selectbox("Tem caso de diabetes na família?", familia_diabetes_options)

#Tabagismo
tabagismo_options = ["", "Não", "Sim"]
tabagismo_dict = {"Não": 0, "Sim": 1}
tabagismo = st.selectbox("É fumante?", tabagismo_options)

#Álcool
alcool_options = ["", "Não", "Sim"]
alcool_dict = {"Não": 0, "Sim": 1}
alcool = st.selectbox("Faz uso de bebida alcoólica?", alcool_options)

#sono
sono = st.number_input("Horas de sono por dia", min_value=4, max_value=11, value=7)

#sono profundo
sono_profundo = st.number_input("Horas de sono profundo por dia", min_value=0, max_value=sono, value=sono-2)

#uso de medicamentos regulares
medicamentos_options = ["", "Não", "Sim"]
medicamentos_dict = {"Não": 0, "Sim": 1}
medicamentos = st.selectbox("Faz uso de medicamentos regulares?", medicamentos_options)

# Gravidez
gravidez = st.number_input("Número de gestações que você teve?", min_value=0, value=0) if sexo == "Feminino" else 0

#Diabetes na Gravidez
diabetes_gravidez_options = ["", "Não", "Sim"]
diabetes_gravidez_dict = {"Não": 0, "Sim": 1}
diabetes_gravidez = st.selectbox("Teve diabetes na gravidez?", diabetes_gravidez_options) if sexo == "Feminino" and gravidez > 0 else 0

# Frequência de urina
urina_options = ["", "Não muito", "Muito"]
urina_dict = {"Não muito": 0, "Muito": 1}
urina = st.selectbox("Com que frequência você urina?", urina_options)

#atividade física
atividade_options = ["", "Uma hora ou mais", "Mais de meia hora", "Menos de meia hora", "Nenhuma"]
atividade = st.selectbox("Quantas horas por dia de atividade física?", atividade_options)

#fast food
fastfood_options = ["", "Nunca", "Às vezes", "Quase sempre", "Sempre"]
fastfood = st.selectbox("Com que frequência come fast food?", fastfood_options)

#estresse
estresse_options = ["", "Nunca", "Às vezes", "Quase sempre", "Sempre"]
estresse = st.selectbox("Selecione o nível de estresse:", estresse_options)

#pressão
pressao_options = ["", "Normal", "Alta", "Baixa"]
pressao = st.selectbox("Como é sua pressão arterial?", pressao_options)


# Inicializar um DataFrame vazio
dados_form = pd.DataFrame(columns=[
    "Sexo", "Família_Diabetes", "Pressão_Alta", "IMC", "Tabagismo", "Álcool",
    "Sono", "Sono_Profundo", "Medicamentos_Regulares", "Gravidez", "Diabetes_Gravidez",
    "Frequência_Urina", "Idade_40-49", "Idade_50-59", "Idade_60_ou_Mais", "Idade_Menos_de_40",
    "Atividade_Física_Menos_de_Meia_Hora", "Atividade_Física_Mais_de_Meia_Hora",
    "Atividade_Física_Nenhuma", "Atividade_Física_Uma_Hora_ou_Mais",
    "Fast_Food_Sempre", "Fast_Food_Nunca", "Fast_Food_Às_Vezes", "Fast_Food_Quase_Sempre",
    "Estresse_Sempre", "Estresse_Nunca", "Estresse_Às_Vezes", "Estresse_Quase_Sempre",
    "Pressão_Arterial_Alta", "Pressão_Arterial_Baixa", "Pressão_Arterial_Normal"
])

# Botão para exibir resultados
if st.button("Analisar"):
    # Verificar se todos os campos foram preenchidos
    if sexo and idade and altura and peso and familia_diabetes and tabagismo and alcool and sono and sono_profundo and medicamentos and urina and atividade and fastfood and estresse and pressao:
        # Adicionar a linha ao DataFrame
        dados_form = dados_form.append({
            "Sexo": 1 if sexo == "Mulher" else 0,
            "Família_Diabetes": 1 if familia_diabetes == "Sim" else 0,
            "IMC": peso / (altura ** 2),
            "Tabagismo": 1 if tabagismo == "Sim" else 0,
            "Álcool": 1 if alcool == "Sim" else 0,
            "Sono": sono,
            "Sono_Profundo": sono_profundo,
            "Gravidez": gravidez,
            "Diabetes_Gravidez": 1 if diabetes_gravidez == "Sim" else 0,
            "Frequência_Urina": 1 if urina == "Muito" else 0,
            "Medicamentos_Regulares": 1 if medicamentos == "Sim" else 0,
            "Idade_40-49": 1 if 40 <= idade < 50 else 0,
            "Idade_50-59": 1 if 50 <= idade < 60 else 0,
            "Idade_60_ou_Mais": 1 if idade >= 60 else 0,
            "Idade_Menos_de_40": 1 if idade < 40 else 0,
            "Atividade_Física_Menos_de_Meia_Hora": 1 if atividade == "Menos de meia hora" else 0,
            "Atividade_Física_Mais_de_Meia_Hora": 1 if atividade == "Mais de meia hora" else 0,
            "Atividade_Física_Nenhuma": 1 if atividade == "Nenhuma" else 0,
            "Atividade_Física_Uma_Hora_ou_Mais": 1 if atividade == "Uma hora ou mais" else 0,
            "Fast_Food_Sempre": 1 if fastfood == "Sempre" else 0,
            "Fast_Food_Nunca": 1 if fastfood == "Nunca" else 0,
            "Fast_Food_Às_Vezes": 1 if fastfood == "Às vezes" else 0,
            "Fast_Food_Quase_Sempre": 1 if fastfood == "Quase sempre" else 0,  
            "Estresse_Sempre": 1 if estresse == "Sempre" else 0,
            "Estresse_Nunca": 1 if estresse == "Nunca" else 0,
            "Estresse_Às_Vezes": 1 if estresse == "Às vezes" else 0,
            "Estresse_Quase_Sempre": 1 if estresse == "Quase sempre" else 0,            
            "Pressão_Arterial_Alta": 1 if pressao == "Alta" else 0,
            "Pressão_Arterial_Baixa": 1 if pressao == "Baixa" else 0,
            "Pressão_Arterial_Normal": 1 if pressao == "Normal" else 0,
            "Pressão_Alta": 1 if pressao == "Alta" else 0
        }, ignore_index=True)
        
        
        
        # Exibir o DataFrame
        st.write("Resultados:")
        #df_form = pd.DataFrame(dados_form)
        #st.table(df_form)
        resultado = model_rf.predict(dados_form)
        if resultado == 1:
            st.error('❌' + ' É provável que o paciente TENHA diabetes')
        else:
            st.info('✅' + ' É provável que o paciente NÃO TENHA diabetes')

    else:
        st.warning("Por favor, preencha todos os campos antes de analisar.")

## Rodapé
st.text("")
st.text("")

url_logo = 'https://www.cafecomdados.com/diabetes/logo.png'
url_link = 'http://www.cafecomdados.com/'
st.markdown(f'<a href="{url_link}" target="_blank"><img src="{url_logo}" alt="Café com Dados" style="height:50px;"></a>', unsafe_allow_html=True)

email = "rodrigo@cafecomdados.com"
nome = "Rodrigo Gois"
rodape = f"Desenvolvido por <a href='mailto:{email}' title='Enviar e-mail para {nome}' alt='{nome}'>{nome}</a>, utilizando algoritmos avançados de inteligência artificial para proporcionar uma análise inteligente e personalizada. <br><br><small style='font-size: 90%'>Conjunto de dados:<br><small style='font-size: 90%'>Tigga, N. P., & Garg, S. (2020). Prediction of Type 2 Diabetes using Machine Learning Classification Methods. Procedia Computer Science, 167, 706-716. DOI: <a href='https://doi.org/10.1016/j.procs.2020.03.336' target='_blank'>https://doi.org/10.1016/j.procs.2020.03.336</a></small>."

st.markdown(rodape, unsafe_allow_html=True)


