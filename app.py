import datetime
import streamlit as st

#modulos
import listas as lst
import extrair
import caminhos

hoje={}
hoje['datetime'] = datetime.datetime.now()
hoje['data'] = hoje['datetime'].date()
hoje['hora'] = hoje['datetime'].time()

with st.sidebar:
	cols = st.columns([1,1])
	cols[0].text(hoje['data'])
	cols[1].text(hoje['hora'])
	
	with st.expander('usuario',expanded=True):
		st.selectbox("usuarios",lst.usuarios,key='usuario')
		st.write(st.session_state['usuario'])

caminho =caminhos.tabelas['jcb_relatorio'] 
#st.write(caminho)

df = extrair.gsheet_to_df(
	id = caminho['id'],
	tabela=caminho['tabela'],
	testar=False)

st.write('transformação da tabela')
def df_bronze(coluna:str,df:pd.DataFrame)->pd.DataFrame:
	df[['dia', 'mes', 'ano', 'hora','minuto']] = df[coluna].str.split(' |/:', expand=True)

	# Convert columns to the desired data types
	df['dia'] = df['dia'].astype(int)
	df['mes'] = df['mes'].astype(int)
	df['ano'] = df['ano'].astype(int)
	df['hora'] = df['hora'].astype(int)
	df['minuto'] = df['minuto'].astype(int)

	return df



with st.expander('raw',expanded=True):
	st.dataframe(df)

with st.expander('bronze',expanded=False):
	df1 = df_bronze(coluna='Iniciar',df=df)
	st.dataframe(df1)

with st.expander('silver',expanded=False):
	st.dataframe(df)

with st.expander('gold',expanded=False):
	st.dataframe(df)