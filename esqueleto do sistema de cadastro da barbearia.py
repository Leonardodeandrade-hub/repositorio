import tkinter as tk
from tkinter import ttk

# Função para criar a tela de Login
def create_login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Sistema de Cadastro da Barbearia", font=("Helvetica", 16)).pack(pady=10)
    
    tk.Label(frame, text="Nome de Usuário").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Senha").pack(pady=5)
    tk.Entry(frame, show="*").pack(pady=5)
    
    tk.Button(frame, text="Login", command=lambda: create_main_screen(root)).pack(pady=20)
    tk.Button(frame, text="Cadastrar", command=lambda: create_client_registration_screen(root)).pack(pady=20)

# Função para criar a tela de Cadastro de Cliente
def create_client_registration_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Cadastro de Cliente", font=("Helvetica", 16)).pack(pady=10)
    
    tk.Label(frame, text="CPF").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Nome").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="E-mail").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Telefone").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Data de Nascimento").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Button(frame, text="Salvar").pack(pady=20)
    tk.Button(frame, text="Voltar", command=lambda: create_main_screen(root)).pack(pady=5)
    
#função para criar tela lista de clientes
def create_client_list_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Clientes Cadastrados", font=("Helvetica", 16)).pack(pady=10)
    
    columns = ("CPF", "Nome", "E-mail", "Telefone")
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.pack(pady=10, fill=tk.BOTH, expand=True)
    
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=5)
    
    tk.Button(button_frame, text="Adicionar Novo Cliente", command=lambda: create_client_registration_screen(root)).pack(side=tk.TOP, pady=5)
    edit_delete_frame = tk.Frame(button_frame)
    edit_delete_frame.pack(pady=5)
    
    tk.Button(edit_delete_frame, text="Editar").pack(side=tk.LEFT, padx=5)
    tk.Button(edit_delete_frame, text="Excluir").pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Voltar", command=lambda: create_main_screen(root)).pack(pady=5)


# Função para criar a tela de Cadastro de Pagamento
def create_payment_registration_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Cadastro de Pagamento", font=("Helvetica", 16)).pack(pady=10)
    
    tk.Label(frame, text="Data de Pagamento").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Valor").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Label(frame, text="Método de Pagamento").pack(pady=5)
    tk.Entry(frame).pack(pady=5)
    
    tk.Button(frame, text="Salvar").pack(pady=20)
    tk.Button(frame, text="Voltar", command=lambda: create_main_screen(root)).pack(pady=5)

# Função para criar a tela de Histórico de Serviços
def create_service_history_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Histórico de Serviços", font=("Helvetica", 16)).pack(pady=10)
    
    columns = ("Data", "Nome do Serviço", "Observações")
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.pack(pady=10, fill=tk.BOTH, expand=True)
    
    tk.Button(frame, text="Adicionar Novo Serviço").pack(pady=5)
    tk.Button(frame, text="Visualizar Detalhes").pack(pady=5)
    tk.Button(frame, text="Voltar", command=lambda: create_main_screen(root)).pack(pady=5)

# Função para criar a tela principal (Home)
def create_main_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(frame, text="Bem-vindo ao Sistema de Cadastro da Barbearia", font=("Helvetica", 16)).pack(pady=20)
    
    tk.Button(frame, text="Cadastro de Cliente", command=lambda: create_client_registration_screen(root)).pack(pady=5)
    tk.Button(frame, text="Listagem de Clientes", command=lambda: create_client_list_screen(root)).pack(pady=5)
    tk.Button(frame, text="Cadastro de Pagamento", command=lambda: create_payment_registration_screen(root)).pack(pady=5)
    tk.Button(frame, text="Histórico de Serviços", command=lambda: create_service_history_screen(root)).pack(pady=5)

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro da Barbearia")
root.geometry("600x400")

# Inicializa com a tela de Login
create_login_screen(root)

# Inicia o loop principal
root.mainloop()
