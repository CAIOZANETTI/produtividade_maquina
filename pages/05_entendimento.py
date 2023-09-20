import streamlit as st
import pandas as pd

st.subheader("Entendimento")

st.write(
'A compreender as informações dos dados\
identificar quais informações são relevantes,\
como elas estão distribuídas, qual a relação\
entre demais variáveis como o tempo (hora, dia, mês)\
ou coordenadas lat+lon.')

# atividades....
#tab1,tab2,tab3,tab4 = st.tabs(['atividade_unicas','dias'])

if 'df1' not in st.session_state:
	df1 = pd.DataFrame()
	st.write('df1 esta vazio!!! voltar e transformar')

df1 = st.session_state['df1']

data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
)



df2 = df1['atividade'].count()

st.dataframe(df2)