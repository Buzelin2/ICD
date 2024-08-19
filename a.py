import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

# Dados da primeira visualização
data_categoria = {
    "Categoria": ["Bate-papo", "Jogos", "Fã Clubes", "Anime", "Web Namoro", 
                  "Roleplay", "Educação", "Pornografia", "Negócios", "Esporte", "Política"],
    "Pré": [27, 42, 33, 11, 2, 4, 7, 0, 2, 0, 1],
    "Durante": [281, 278, 181, 96, 75, 68, 81, 39, 72, 8, 5],
    "Pós": [121, 69, 23, 55, 42, 31, 14, 54, 22, 5, 0]
}

# Convertendo para DataFrame
df_categoria = pd.DataFrame(data_categoria)

# Título da aplicação
st.title("Visualização Interativa de Categorias Pré, Durante e Pós Pandemia")

# Seção para seleção de categorias
st.header("Seleção de Categoria")
categoria_selecionada = st.selectbox("Selecione uma Categoria:", df_categoria["Categoria"])

# Filtrando dados para a categoria selecionada
df_filtrado = df_categoria[df_categoria["Categoria"] == categoria_selecionada]

# Transformando dados para formato longo (necessário para Seaborn)
df_long = pd.melt(df_filtrado, id_vars=["Categoria"], var_name="Período", value_name="Quantidade")

# Criando o gráfico de barras
plt.figure(figsize=(8, 6))
sns.barplot(data=df_long, x="Período", y="Quantidade", palette="viridis")
plt.title(f"Quantidade ao longo do tempo para {categoria_selecionada}")
plt.xlabel("Período")
plt.ylabel("Quantidade")
st.pyplot(plt)


st.title("Métricas BERT")
# Dados da segunda visualização
data_metrica = {
    "Categoria": ["Racismo", "Homofobia", "Sexismo", "Body-Shaming", "Ideologia"],
    "Acc": [0.989, 0.985, 0.987, 0.985, 0.993],
    "Prec": [0.889, 0.924, 0.940, 0.887, 0.948],
    "F1 Score": [0.933, 0.927, 0.913, 0.937, 0.953],
    "Rec": [0.981, 0.930, 0.886, 0.993, 0.958]
}

# Convertendo para DataFrame
df_metrica = pd.DataFrame(data_metrica)

# Lista de métricas disponíveis
metricas = ["Acc", "Prec", "F1 Score", "Rec"]

# Seleção de métricas
st.session_state.metric_index = st.session_state.get("metric_index", 0)

# Funções para navegação de métricas
def proxima_metrica():
    st.session_state.metric_index = (st.session_state.metric_index + 1) % len(metricas)

def metrica_anterior():
    st.session_state.metric_index = (st.session_state.metric_index - 1) % len(metricas)

# Layout dos botões e gráfico
col1, col2, col3 = st.columns([1, 5, 1])

# Botão "Anterior"
with col1:
    st.button("Anterior", on_click=metrica_anterior)

# Gráfico interativo no centro
with col2:
    metrica_atual = metricas[st.session_state.metric_index]
    st.header(f"Gráfico Interativo para {metrica_atual}")
    chart = alt.Chart(df_metrica).mark_bar().encode(
        x=alt.X('Categoria:N', title='Categoria'),
        y=alt.Y(f'{metrica_atual}:Q', title=metrica_atual),
        color=alt.Color('Categoria:N', legend=None)
    ).properties(
        width=800,
        height=400
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

# Botão "Próxima"
with col3:
    st.button("Próxima", on_click=proxima_metrica)


st.title("Intensidade dos comportamento nas categorias de servidores")
# Dados da terceira visualização
data_heatmap = {
    "Categoria": ["suicídio", "depressão", "ansiedade", "psicose", "transtornos", "questões gerais"],
    "Anime": [0.025, 0.2, 0.0031, 0.0027, 0.00026, 0.014],
    "Conversa": [0.027, 0.19, 0.006, 0.0025, 0.00092, 0.018],
    "Educação": [0.0094, 0.14, 0.0055, 0.0031, 0.00035, 0.018],
    "Esporte": [0.024, 0.097, 0.0014, 0.00069, 0.00005, 0.0067],
    "Fãs/Serviços": [0.011, 0.14, 0.0032, 0.0028, 0.00021, 0.0093],
    "Jogos": [0.021, 0.17, 0.0029, 0.0016, 0.00015, 0.012],
    "Negócios": [0.014, 0.27, 0.0024, 0.0011, 0.00012, 0.038],
    "Política": [0.028, 0.25, 0.012, 0.0037, 0.0023, 0.016],
    "Pornografia": [0.031, 0.12, 0.0026, 0.0024, 0.0003, 0.016],
    "RolePlay": [0.0064, 0.15, 0.0063, 0.0013, 0.00032, 0.0063],
    "Webnamoro": [0.036, 0.15, 0.0053, 0.0032, 0.00033, 0.018]
}

# Convertendo para DataFrame
df_heatmap = pd.DataFrame(data_heatmap)

# Lista de categorias
categorias_heatmap = df_heatmap["Categoria"].tolist()

# Estado inicial para categoria selecionada
st.session_state.categoria_index = st.session_state.get("categoria_index", 0)

# Funções para navegação de categorias
def proxima_categoria():
    st.session_state.categoria_index = (st.session_state.categoria_index + 1) % len(categorias_heatmap)

def categoria_anterior():
    st.session_state.categoria_index = (st.session_state.categoria_index - 1) % len(categorias_heatmap)

# Layout dos botões e gráfico
col1, col2, col3 = st.columns([1, 5, 1])

# Botão "Anterior"
with col1:
    st.button("Anterior", on_click=categoria_anterior, key="anterior_button")

# Gráfico de heatmap no centro
with col2:
    categoria_atual = categorias_heatmap[st.session_state.categoria_index]
    st.header(f"Heatmap para a Categoria: {categoria_atual}")
    df_filtrado = df_heatmap[df_heatmap["Categoria"] == categoria_atual].drop(columns=["Categoria"])
    fig = px.imshow(df_filtrado,
                    labels=dict(x="Atividade", y="Categoria", color="Intensidade"),
                    x=df_filtrado.columns,
                    y=[categoria_atual],
                    aspect="auto",
                    color_continuous_scale='RdBu_r')
    fig.update_layout(
        title=f"Heatmap Interativo para {categoria_atual}",
        xaxis_nticks=len(df_filtrado.columns),
        yaxis_nticks=1,
        width=800,
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)

# Botão "Próxima"
with col3:
    st.button("Próxima", on_click=proxima_categoria, key="proxima_button")

st.title("Box Plot para as métricas de BERT")

# Dados da quarta visualização
data_boxplot = {
    "Category": ["Racismo", "Homofobia", "Sexismo", "Body-Shaming", "Ideologia"],
    "Acc": [0.989, 0.985, 0.987, 0.985, 0.993],
    "Acc_IC_Lower": [0.967, 0.964, 0.971, 0.962, 0.972],
    "Acc_IC_Upper": [0.994, 0.991, 0.992, 0.989, 0.997],
    "Prec": [0.889, 0.924, 0.940, 0.887, 0.948],
    "Prec_IC_Lower": [0.862, 0.906, 0.923, 0.853, 0.935],
    "Prec_IC_Upper": [0.911, 0.939, 0.957, 0.914, 0.961],
    "Rec": [0.981, 0.930, 0.886, 0.993, 0.958],
    "Rec_IC_Lower": [0.962, 0.909, 0.861, 0.976, 0.939],
    "Rec_IC_Upper": [0.992, 0.949, 0.911, 0.996, 0.977],
    "F1": [0.933, 0.927, 0.913, 0.937, 0.953],
    "F1_IC_Lower": [0.908, 0.905, 0.889, 0.910, 0.932],
    "F1_IC_Upper": [0.958, 0.949, 0.937, 0.964, 0.974]
}

# Convertendo para DataFrame
df_boxplot = pd.DataFrame(data_boxplot)

# Seleção de métricas
metricas_boxplot = {
    "Acurácia": "Acc",
    "Precisão": "Prec",
    "Recall": "Rec",
    "F1 Score": "F1"
}
metrica_selecionada = st.selectbox("Selecione a Métrica", list(metricas_boxplot.keys()))

# Filtrando dados para a métrica selecionada
metrica = metricas_boxplot[metrica_selecionada]
df_long_boxplot = pd.melt(df_boxplot, id_vars=["Category"], 
                          value_vars=[metrica, f"{metrica}_IC_Lower", f"{metrica}_IC_Upper"],
                          var_name="Tipo", value_name="Valor")

# Criando box plot
fig_boxplot = px.box(df_long_boxplot, x="Category", y="Valor", 
                     title=f"Distribuição de {metrica_selecionada} por Categoria",
                     labels={"Valor": metrica_selecionada, "Category": "Categoria"},
                     width=800, height=500)

# Melhorando layout
fig_boxplot.update_layout(
    yaxis_title=metrica_selecionada,
    xaxis_title="Categoria",
    boxmode='group',
    showlegend=False
)

# Exibindo gráfico
st.plotly_chart(fig_boxplot, use_container_width=True)
