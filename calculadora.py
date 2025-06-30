import tkinter as tk
from tkinter import messagebox

# --- Funções da Calculadora ---

def ao_clicar_botao(char):
    """ Adiciona o caractere do botão à expressão no display. """
    global expressao
    # Limpa o display se o cálculo anterior deu erro ou se já mostrou um resultado
    if "Erro" in texto_display.get() or "maçãs" in texto_display.get():
        expressao = ""
        texto_display.set("")
    
    expressao += str(char)
    texto_display.set(expressao)

def calcular_resultado():
    """ Calcula a expressão, exibe o resultado com tema de maçãs e checa por surpresas. """
    global expressao
    if not expressao:
        return
        
    try:
        # Avalia a expressão matemática
        resultado_numerico = eval(expressao)

        # Formata para int se não houver parte decimal
        if resultado_numerico == int(resultado_numerico):
            resultado_numerico = int(resultado_numerico)

        # Atualiza o display com o tema
        texto_display.set(f"{resultado_numerico} maçãs")
        
        # Deixa o resultado numérico pronto para o próximo cálculo
        expressao = str(resultado_numerico)

        # --- VERIFICA AS SURPRESAS ESPECIAIS ---
        if resultado_numerico == 6:
            messagebox.showinfo("Jornada Completa!", 
                                "Resultado 6! Você relembrou as 6 etapas da jornada da maçã de Palmas!")
        elif resultado_numerico == 1:
            messagebox.showinfo("Número 1!", 
                                "Palmas, a Capital Nacional da Maçã, é a número 1!")
        elif resultado_numerico >= 1000:
            messagebox.showinfo("Grande Colheita!",
                                f"Uau! {resultado_numerico} maçãs! Isso encheria um caminhão inteiro saindo dos pomares de Palmas!")

    except (SyntaxError, ZeroDivisionError):
        texto_display.set("Erro")
        expressao = ""
    except Exception:
        texto_display.set("Erro")
        expressao = ""

def limpar_tudo():
    """ Limpa o display e a expressão. """
    global expressao
    expressao = ""
    texto_display.set("")

# --- Função para a História da Maçã ---

def abrir_janela_historia():
    """Cria e abre uma nova janela para contar a história da maçã."""
    
    # --- Conteúdo da História ---
    cenas = [
        {"titulo": "Bem-vindo a Palmas, PR!", "texto": "Esta é a jornada da maçã, a fruta que faz de Palmas a Capital Nacional da Maçã.", "cor_fundo": "#AED581", "texto_botao": "Começar"},
        {"titulo": "1. O Pomar", "texto": "Tudo começa aqui, nos vastos pomares da região. As maçãs crescem saudáveis sob o sol.", "cor_fundo": "#81C784", "texto_botao": "Próximo"},
        {"titulo": "2. A Colheita", "texto": "Com muito cuidado, agricultores colhem as maçãs na época certa, garantindo a melhor qualidade.", "cor_fundo": "#FFB74D", "texto_botao": "Próximo"},
        {"titulo": "3. O Transporte", "texto": "As maçãs são embaladas e carregadas em caminhões. A viagem para a cidade grande começa!", "cor_fundo": "#64B5F6", "texto_botao": "Próximo"},
        {"titulo": "4. O Mercado da Cidade", "texto": "Finalmente, as maçãs de Palmas chegam às prateleiras dos mercados, frescas e deliciosas.", "cor_fundo": "#FFF176", "texto_botao": "Próximo"},
        {"titulo": "Bom Apetite!", "texto": "Da próxima vez que comer uma maçã, lembre-se da jornada dela desde os campos de Palmas até você!", "cor_fundo": "#E57373", "texto_botao": "Reiniciar"}
    ]
    cena_atual = 0

    # --- Janela da História (Toplevel) ---
    janela_historia = tk.Toplevel(janela)
    janela_historia.title("A Jornada da Maçã de Palmas")
    janela_historia.geometry("500x300")
    janela_historia.resizable(False, False)
    
    # --- Widgets da História ---
    frame_historia = tk.Frame(janela_historia)
    frame_historia.pack(expand=True, fill="both")
    
    label_titulo = tk.Label(frame_historia, font=('Helvetica', 20, 'bold'), wraplength=450)
    label_titulo.pack(pady=(10, 20))

    label_texto = tk.Label(frame_historia, font=('Helvetica', 14), wraplength=450)
    label_texto.pack(pady=10)

    # --- Funções da História ---
    def proxima_cena():
        nonlocal cena_atual
        cena_atual = (cena_atual + 1) % len(cenas)
        atualizar_interface()

    def atualizar_interface():
        cena = cenas[cena_atual]
        janela_historia.config(bg=cena["cor_fundo"])
        frame_historia.config(bg=cena["cor_fundo"])
        label_titulo.config(text=cena["titulo"], bg=cena["cor_fundo"])
        label_texto.config(text=cena["texto"], bg=cena["cor_fundo"])
        botao_proximo.config(text=cena["texto_botao"])

    botao_proximo = tk.Button(frame_historia, font=('Helvetica', 12, 'bold'), command=proxima_cena)
    botao_proximo.pack(pady=20, ipadx=20, ipady=10)

    atualizar_interface()
    janela_historia.transient(janela) # Mantém a janela da história na frente da calculadora
    janela_historia.grab_set() # Foca na janela da história


# --- Configuração da Janela Principal da Calculadora ---
janela = tk.Tk()
janela.title("Calculadora de Palmas")
janela.geometry("300x450")
janela.resizable(False, False)
janela.configure(bg="#2E2E2E")

# Variável global para guardar a expressão matemática
expressao = ""

# --- Menu Superior ---
menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_arquivo)
menu_arquivo.add_command(label="História da Maçã", command=abrir_janela_historia)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

# --- Display da Calculadora ---
texto_display = tk.StringVar()
display = tk.Entry(janela, textvariable=texto_display, font=('arial', 24, 'bold'), bd=10, 
                   insertwidth=2, width=14, borderwidth=4, justify='right', bg="#C8C8C8")
display.pack(pady=20)

# --- Frame para os Botões ---
frame_botoes = tk.Frame(janela, bg="#2E2E2E")
frame_botoes.pack()

# --- Layout dos Botões (Grid) ---
# Lista de botões para criar o layout de forma mais fácil
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Cria e posiciona os botões em um grid 4x4
row = 0
col = 0
for texto_botao in botoes:
    # Define a função e a cor com base no tipo de botão
    if texto_botao == '=':
        acao = calcular_resultado
        cor_bg = '#4CAF50' # Verde
    elif texto_botao in ['/', '*', '-', '+']:
        acao = lambda x=texto_botao: ao_clicar_botao(x)
        cor_bg = '#FF9800' # Laranja
    else:
        acao = lambda x=texto_botao: ao_clicar_botao(x)
        cor_bg = '#E0E0E0' # Cinza claro

    # Cria o botão
    btn = tk.Button(frame_botoes, text=texto_botao, font=('arial', 14, 'bold'),
                    fg='black', bg=cor_bg,
                    height=2, width=5, command=acao)
    btn.grid(row=row, column=col, padx=5, pady=5)
    
    # Atualiza a posição no grid
    col += 1
    if col > 3:
        col = 0
        row += 1

# --- Botão de Limpar (C) ---
btn_limpar = tk.Button(frame_botoes, text='C', font=('arial', 14, 'bold'),
                       fg='white', bg='#f44336', # Vermelho
                       height=2, width=5, command=limpar_tudo)
btn_limpar.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='we')


# Inicia o loop da interface gráfica
janela.mainloop()