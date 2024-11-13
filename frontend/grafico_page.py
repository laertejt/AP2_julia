#Frontend da aba GRÁFICOS: 

#Importação das bibliotecas:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
#Importação das funções encontradas nos outros arquivos
from backend.views import pegar_df_preco_corrigido, carteira, pegar_df_preco_diversos, validar_data
from backend.routes import menu_estrategia, menu_graficos, grafico_ibov, comp


#Exibição 
def render_grafico():
    st.header("ANÁLISE DE GRÁFICOS")
    st.write("Aqui você pode visualizar o gráfico correspondente a variação dos valores de fechamento das ações da carteira gerada na aba estratégia em relação ao decorrer do tempo.")

    #verificar se a lista das ações da carteira foi gerada e está no cache: 
    if 'acoes_carteira' not in st.session_state:
        st.warning("Nenhuma carteira de ações foi gerada. Gere a carteira na página de Estratégia.")
        return

    acoes_carteira = st.session_state.acoes_carteira  # Pega a carteira de ações
    
    #Inputs das datas 
    data_ini = st.date_input("Selecione uma data de início", value=pd.to_datetime('today'),key="data_inicio") #today como valor padrão
       
    data_fim = st.date_input("Selecione uma data de fim", value=pd.to_datetime('today'), key="data_fim") #today como valor padrão
    
    validar_data(data_ini)
    validar_data(data_fim)

    st.write(f"Variação do valor do fechamento da carteira formada pelas ações: {acoes_carteira}")
    st.write("Antes de clicar em Gerar Gráficos garanta que você selecionou a opção de visuzalização.")

   
#FILTROS INTERATIVOS PARA A VISUALIZAÇÃO DOS GRÁFICOS: 
    st.sidebar.header("Opções de Visualização")
    graficos_opcoes = st.sidebar.multiselect(
        "Escolha os gráficos:",
        ["Carteira de Ações", "IBOV", "Comparativo Carteira x IBOV"]
    )

    #Execução da busca: 
    if st.button("Gerar Gráficos"):
        if "Carteira de Ações" in graficos_opcoes:
            st.subheader("Carteira de Ações")
            df = menu_graficos(data_ini, data_fim, acoes_carteira)
       
        if "IBOV" in graficos_opcoes:
            st.subheader("IBOV")
            ibov = grafico_ibov(data_ini, data_fim)


        if "Comparativo Carteira x IBOV" in graficos_opcoes:
            df_carteira = pegar_df_preco_corrigido(data_ini, data_fim, acoes_carteira)
            df_ibov = pegar_df_preco_diversos(data_ini, data_fim)
            st.subheader("Comparativo: Carteira x IBOV")
            comparativo = comp(data_ini, data_fim, df_carteira, df_ibov)

    else:
        st.error("Não foi possível obter os dados. Verifique as datas ou ações selecionadas.")



    
   
    






    








 
#Exibição Ibovespa:       



