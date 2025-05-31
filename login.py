usuarios = {}

# --- Boas-vindas --- #
def boas_vindas():
    print("==========================================")
    print("     BEM-VINDO(A) AO EXPLORAMUNDO VIAGENS ")
    print("==========================================")
    print("Descubra destinos incríveis e reserve suas aventuras aqui!\n")

# --- Funções auxiliares --- #
def limpar_numeros(texto):
    resultado = ""
    for caractere in texto:
        if caractere >= "0" and caractere <= "9":
            resultado += caractere
    return resultado

def validar_cpf(cpf):
    cpf_limpo = limpar_numeros(cpf)
    if len(cpf_limpo) != 11:
        return False
    for digito in cpf_limpo:
        if digito < "0" or digito > "9":
            return False
    return True

def formatar_cpf(cpf):
    cpf = limpar_numeros(cpf)
    return cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

def validar_email(email):
    if "@" in email and "." in email:
        return True
    return False

def validar_telefone(telefone):
    telefone = limpar_numeros(telefone)
    if len(telefone) >= 10 and len(telefone) <= 13:
        for c in telefone:
            if c < "0" or c > "9":
                return False
        return True
    return False

def formatar_telefone(telefone):
    t = limpar_numeros(telefone)
    if len(t) == 13:
        return "+" + t[:2] + " (" + t[2:4] + ") " + t[4:9] + "-" + t[9:]
    elif len(t) == 11:
        return "(" + t[:2] + ") " + t[2:7] + "-" + t[7:]
    else:
        return telefone

def entrada_valida(mensagem, funcao_validar, funcao_formatar=None):
    while True:
        valor = input(mensagem)
        if funcao_validar(valor):
            if funcao_formatar != None:
                return funcao_formatar(valor)
            else:
                return valor
        else:
            print("Entrada inválida. Tente novamente.")

def confirmar_dados():
    while True:
        resposta = input("Os dados estão corretos? (sim/não): ").lower()
        if resposta == "sim" or resposta == "s":
            return True
        elif resposta == "não" or resposta == "nao" or resposta == "n":
            return False
        else:
            print("Digite apenas 'sim' ou 'não'.")

# --- Cadastro --- #
def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    nome = input("Nome completo: ")
    cpf = entrada_valida("CPF (apenas números): ", validar_cpf, formatar_cpf)
    email = entrada_valida("E-mail: ", validar_email)
    telefone = entrada_valida("Telefone com DDD: ", validar_telefone, formatar_telefone)
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    print("\n=== CONFIRMAÇÃO ===")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("E-mail:", email)
    print("Telefone:", telefone)
    print("Usuário:", usuario)

    if confirmar_dados():
        usuarios[usuario] = senha
        print("\nCadastro concluído com sucesso!")
        tela_login()
    else:
        print("\nCadastro cancelado. Vamos tentar novamente.")
        cadastrar_usuario()

# --- Login --- #
def tela_login():
    print("\n=== LOGIN ===")
    nome = input("Usuário: ")
    senha = input("Senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        print("\nLogin realizado com sucesso!")
        menu_apos_login(nome)
    else:
        print("\nUsuário ou senha incorretos.")
        tentar_novamente()

def tentar_novamente():
    resposta = input("Deseja tentar novamente? (s/n): ").lower()
    if resposta == "s":
        tela_login()
    else:
        print("Encerrando o sistema.")

def menu_apos_login(usuario):
    print("\nBem-vindo(a),", usuario)

# --- Início do sistema --- #
if __name__ == "__main__":
    boas_vindas()
    cadastrar_usuario()