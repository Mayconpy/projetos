import os
import random
import string
import sys
import time
from hashlib import sha256
import cryptography
import requests
from winotify import Notification,audio
from colorama import Fore, Back, Style 
from cryptography.fernet import Fernet
def criar_conta():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX)
    pessoa_ja_tem_email_no_gloogle = input('voce tem alguma email? [S]im [N]ao: ').lower()
    if pessoa_ja_tem_email_no_gloogle == 's':
        print('continue')
        time.sleep(0.7)
        os.system('cls')
    if pessoa_ja_tem_email_no_gloogle == 'n':
        toast = Notification(app_id="GLOOGLE",
                     title="CRIAR CONTA GLOOGLE",
                     msg="ENTRANDO..",
                     icon=r"C:\Users\Maycon\Downloads")
        toast.add_actions(label="GMAIL", 
                  launch="https://www.google.com/intl/pt-BR/gmail/about/")
        toast.set_audio(audio.Mail,loop=False)
        toast.show()
        print('volte quando criar')
        time.sleep(3)
        criar_conta()
    
    Email = input('Coloque seu Emaill: ').capitalize()
    armazenar_email = sha256(Email.encode()).hexdigest()
    if 'gmail.com'  in Email:
        retorna = 'correto ✔\nEmail salvo ✔'
        print(retorna)
        time.sleep(0.8)
        os.system('cls')
    else: 
        print('Incorreto falta (gmail.com)')
        criar_conta()
    Senha = input('Crie uma senha\nminimo 8 caracteres maximo 9: ')
    armazenar_Senha = sha256(Senha.encode()).hexdigest()
    if len(Senha) < 8:
        print('Senha muito pequena❌')
        time.sleep(1)
        os.system('cls')
        criar_conta()
        if len(Senha) > 9:
            print('Senha muito grande❌')
            time.sleep(1)
            os.system('cls')
            criar_conta()
    ramdomizar_senha = input('deseja ramdomizar sua senha [S]im [N]ao: ').lower()
    armazenar_random_senha = sha256(ramdomizar_senha.encode()).hexdigest(),
    if ramdomizar_senha == 's':
        tamanho = 8 
        strings = string.ascii_lowercase
        for i in range(tamanho):
            ramdomizar_senha += random.choice(strings)
            senha = ramdomizar_senha
            print(f'senha:{senha}')

    if ramdomizar_senha != 's':
            senha = armazenar_Senha
    def Login():
        login_Email = input('Endereço de Email: ')
        armazena_login = sha256(login_Email.encode()).hexdigest
        if login_Email == Email:
                print('✔')
        else:
             print('Nao Encontramos nenhum EMAIL Crie um Agora')
             criar_conta()
        senha_login = input('Digite sua senha: ')
        armazenar_senha_login = sha256(senha_login.encode()).hexdigest()
        if senha_login == Senha:
             print('✔')
        else:
             print('Email ou senha incorretos tente novamente')
             Login()
        if senha_login == ramdomizar_senha:
             print('✔')
        time.sleep(1)
        Logar = 'LOGAR'
        FIM = ('chegamos ao fim do codigo que quase bati a cabeça no teclado👍\naqui estao os dados criptografado em B(bytes):')
        print (f'{Logar}\n{FIM}\nEMAIL:{armazenar_email}\nSENHA:{armazenar_Senha}\nRANDOM_SENHA:{armazenar_random_senha}')
        
        

    Login()
    
    
puxar = criar_conta()
print(puxar)