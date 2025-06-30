import tkinter as tk

# --- Conteúdo da História ---
# Cada item da lista é uma "cena" da nossa história.
cenas = [
    {
        "titulo": "Bem-vindo a Palmas, PR!",
        "texto": "Esta é a jornada da maçã, a fruta que faz de Palmas a Capital Nacional da Maçã.",
        "cor_fundo": "#AED581", # Verde claro (campo)
        "texto_botao": "Começar"
    },
    {
        "titulo": "1. O Pomar",
        "texto": "Tudo começa aqui, nos vastos pomares da região. As maçãs crescem saudáveis sob o sol.",
        "cor_fundo": "#81C784", # Verde
        "texto_botao": "Próximo"
    },
    {
        "titulo": "2. A Colheita",
        "texto": "Com muito cuidado, agricultores colhem as maçãs na época certa, garantindo a melhor qualidade.",
        "cor_fundo": "#FFB74D", # Laranja claro (colheita)
        "texto_botao": "Próximo"
    },
    {
        "titulo": "3. O Transporte",
        "texto": "As maçãs são embaladas e carregadas em caminhões. A viagem para a cidade grande começa!",
        "cor_fundo": "#64B5F6", # Azul claro (estrada)
        "texto_botao": "Próximo"
    },
    {
        "titulo": "4. O Mercado da Cidade",
        "texto": "Finalmente, as maçãs de Palmas chegam às prateleiras dos mercados, frescas e deliciosas.",
        "cor_fundo": "#FFF176", # Amarelo (mercado)
        "texto_botao": "Próximo"
    },
    {
        "titulo": "Bom Apetite!",
        "texto": "Da próxima vez que comer uma maçã, lembre-se da jornada dela desde os campos de Palmas até você!",
        "cor_fundo": "#E57373", # Vermelho (maçã)
        "texto_botao": "Reiniciar"
    }
]

cena_atual = 0

# --- Funções ---
def proxima_cena():
    """ Avança para a próxima cena da história. """
    global cena_atual
    cena_atual += 1
    # Se for a última cena, volta para o início
    if cena_atual >= len(cenas):
        cena_atual = 0
    
    atualizar_interface()

def atualizar_interface():
    """ Atualiza os textos e cores da janela com base na cena atual. """
    cena = cenas[cena_atual]
    
    janela.config(bg=cena["cor_fundo"])
    frame_principal.config(bg=cena["cor_fundo"])
    
    label_titulo.config(text=cena["titulo"], bg=cena["cor_fundo"])
    label_texto.config(text=cena["texto"], bg=cena["cor_fundo"])
    botao_proximo.config(text=cena["texto_botao"])


# --- Configuração da Janela Principal ---
janela = tk.Tk()
janela.title("A Jornada da Maçã de Palmas")
janela.geometry("500x300")
janela.resizable(False, False)

# --- Widgets ---
# Usamos um frame para centralizar o conteúdo
frame_principal = tk.Frame(janela)
frame_principal.pack(expand=True)

label_titulo = tk.Label(frame_principal, font=('Helvetica', 20, 'bold'), wraplength=450)
label_titulo.pack(pady=(10, 20))

label_texto = tk.Label(frame_principal, font=('Helvetica', 14), wraplength=450)
label_texto.pack(pady=10)

botao_proximo = tk.Button(frame_principal, font=('Helvetica', 12, 'bold'), command=proxima_cena)
botao_proximo.pack(pady=20, ipadx=20, ipady=10)


# --- Iniciar a Aplicação ---
atualizar_interface() # Carrega a primeira cena
janela.mainloop() 