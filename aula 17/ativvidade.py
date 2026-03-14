conexao = sqlite3.connect("leads.db")
cursor = conexao.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXIST leads (
    nome TEXT,
    idade INTEGER,
    email TEXT,
    enderexo TEXT
    trabalho TEXT,
    graduacao TEXT
)
""")

def salvar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    endereco = entrada_endereco.get()
    trabalho = entrada_trabalho.get()
    graduacao = entrada_graduaco.get()

    cursor.execute("INSERT INTO leads VALEUS(?,?,?,?,?,?),(nome, idade, email, endereco, trabalho, graduacao))")

    conexao.commit()

janela = tk.Tk()
janela.title("Cadastro de Leads - Agência de Marketing")
janela.geometry("400x400")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Idade").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela, text="Endereço").pack()
entry_endereco = tk.Entry(janela)
entry_endereco.pack()

tk.Label(janela, text="Trabalho").pack()
entry_trabalho = tk.Entry(janela)
entry_trabalho.pack()

tk.Label(janela, text="Graduação").pack()
entry_graduacao = tk.Entry(janela)
entry_graduacao.pack()

botao = tk.Button(janela, text="Cadastrar Lead", command=cadastrar_lead)
botao.pack(pady=10)
