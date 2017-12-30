"""

Este código é parte integrante do livro Dados FC: A Gestão da Informação aplicada ao Futebol
do autor Vitor Principe e publicado pela Editora Primeiro Lugar.

"""
#Bibliotecas usadas
from matplotlib.patches import Arc
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pandas as pd
import seaborn as sns

#Acesso a base de dados em arquivo excel
dataset = pd.read_excel('Messi_1Tempo.xlsx')
dados = dataset.iloc[:,1:]
X = dados.iloc[:, 0:1].values
y = dados.iloc[:, 1:2].values

#Função para desenhar o campo
def desenho_campo(ax=None, color='black', lw=1, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    #Campo central
    campo = plt.Rectangle((0, 0), 105, 68, edgecolor=color, linewidth=lw, fill=False)
    meio = lines.Line2D([52.5, 52.5], [0, 68], linewidth=1, color=color, alpha=1)
    circulo_central = plt.Circle((52.5, 34), radius=9.15, linewidth=lw, color=color, fill=False)
    marca_central = plt.Circle((52.5, 34), radius=0.2, linewidth=lw, color=color)
    #Contrução do lado direito do campo
    penalty = plt.Circle((94, 34), radius=0.2, linewidth=lw, color=color)
    grande_area = lines.Line2D([88.5,88.5], [13.85,54.15], linewidth=lw, color=color)
    grande_area2 = lines.Line2D([88.5,105], [13.85,13.85], linewidth=lw, color=color)
    grande_area3 = lines.Line2D([88.5,105], [54.15,54.15], linewidth=lw, color=color)
    grande_area4 = Arc((88.5,34), 13.5, 7, angle=270, theta1=180, theta2=0, linewidth=lw, color=color)
    pequena_area = lines.Line2D([99.5,99.5], [24.85,43.15], linewidth=lw, color=color)
    pequena_area2 = lines.Line2D([99.5,105], [24.85,24.85], linewidth=lw, color=color)
    pequena_area3 = lines.Line2D([99.5,105], [43.15,43.15], linewidth=lw, color=color)
    baliza = lines.Line2D([107.4,107.4], [30.35,37.65], linewidth=lw, color=color)
    baliza2 = lines.Line2D([105,107.4], [37.65, 37.65], linewidth=lw, color=color)
    baliza3 = lines.Line2D([105,107.4], [30.35, 30.35], linewidth=lw, color=color)
    linha_fundo = Arc((105,68), 5, 5, angle=270, theta1=270, theta2=0, linewidth=lw, color=color)
    linha_fundo2 = Arc((105,0), 5, 5, angle=-180, theta1=270, theta2=0, linewidth=lw, color=color)
    #Contrução do lado esquerdo do campo
    penalty_E  = plt.Circle((11, 34), radius=0.2, linewidth=1, color=color)
    grande_area_E  = lines.Line2D([16.5,16.5], [13.85,54.15], linewidth=lw, color=color)
    grande_area2_E  = lines.Line2D([16.5,0], [13.85,13.85], linewidth=lw, color=color)
    grande_area3_E  = lines.Line2D([16.5,0], [54.15,54.15], linewidth=lw, color=color)
    grande_area4_E  = Arc((16.5,34), 13.5, 7, angle=270, theta1=0, theta2=180, linewidth=lw, color=color)
    pequena_area_E  = lines.Line2D([5.5,5.5], [24.85,43.15], linewidth=lw, color=color)
    pequena_area2_E  = lines.Line2D([0,5.5], [24.85,24.85], linewidth=lw, color=color)
    pequena_area3_E  = lines.Line2D([0,5.5], [43.15,43.15], linewidth=lw, color=color)
    baliza_E  = lines.Line2D([-2.4,-2.4], [30.35,37.65], linewidth=lw, color=color)
    baliza2_E  = lines.Line2D([0,-2.4], [37.65, 37.65], linewidth=lw, color=color)
    baliza3_E  = lines.Line2D([0,-2.4], [30.35, 30.35], linewidth=lw, color=color)
    linha_fundo_E  = Arc((0,68), 5, 5, angle=360, theta1=270, theta2=0, linewidth=lw, color=color)
    linha_fundo2_E  = Arc((0,0), 5, 5, angle=-270, theta1=270, theta2=0, linewidth=lw, color=color)

    #Aplicação dos elementos para conrtução do campo
    elementos_linha = [meio, grande_area, grande_area2, grande_area3, pequena_area, 
                        grande_area_E , grande_area2_E , grande_area3_E , pequena_area_E,
                        pequena_area2, pequena_area3, baliza, baliza2, baliza3, pequena_area2_E,
                        pequena_area3_E , baliza_E , baliza2_E , baliza3_E]

    elementos_patch = [penalty_E , grande_area4_E , linha_fundo_E , linha_fundo2_E, campo,
                        circulo_central, marca_central, penalty, grande_area4, linha_fundo, linha_fundo2]

    for elemento in elementos_linha:
        ax.add_line(elemento)

    for elementos in elementos_patch:
        ax.add_patch(elementos)

    return ax

#Contrução do gráfico
grafico = sns.jointplot(X, y, stat_func=None, kind='scatter', space=0, alpha=0.5)
grafico.fig.set_size_inches(6,5)
ax = grafico.ax_joint
desenho_campo(ax)
ax.set_xlim(0,105)
ax.set_ylim(0,68)
ax.set_xlabel('coordenada x [m]')
ax.set_ylabel('coordenada y [m]')
ax.tick_params(labelbottom='off', labelleft='off')
ax.set_title('Ações de Messi no 1 tempo - Real Madrid 0 x 3 Barcelona', y=1.2, fontsize=14)

#Salvar no computador
plt.savefig('Messi_1Tempo.png', bbox_inches='tight', format='png', dpi=300)

#Mostrar na tela de programação o gráfico
plt.show()
















