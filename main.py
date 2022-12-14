from matplotlib import pyplot as plt
import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

#Funcionalidades do kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.base import runTouchApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.filemanager import MDFileManager

#Bibliotecas do proprio aplicativo
from psql import *
from authenticator import *

#Criptografia unidirecional
import hashlib

class menu(Screen):
    pass
class login(Screen):
    pass
class register(Screen):
    pass
class configuracoes(Screen):
    pass
class configuracoes_alter(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        #Estilo
        Builder.load_file('main2.kv')
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Blue'
        
        #Telas
        self.sm = ScreenManager()
        
        self.menu = menu(name='menu')
        self.sm.add_widget(self.menu)
        
        self.login_screen = login(name='login')
        self.sm.add_widget(self.login_screen)
        
        self.register = register(name='register')
        self.sm.add_widget(self.register)
        
        self.configuracoes = configuracoes(name='configuracoes')
        self.sm.add_widget(self.configuracoes)
        
        self.configuracoes_alter = configuracoes_alter(name='configuracoes_alter')
        self.sm.add_widget(self.configuracoes_alter)
        
        self.sql = psql(host = '127.0.0.1', database = 'app', username = 'postgres', password = 'admin')
        self.sm.current = 'login'
        return self.sm

    def login(self):
        if self.login_screen.ids.user.text=='1' and self.login_screen.ids.password.text=='1':
            return self.switch_screen('menu')
#         query = self.sql.select_db('app','auth', {'usuario': self.login_screen.ids.user.text,
#                                                 'senha' : hashlib.sha256(self.login_screen.ids.password.text.encode()).hexdigest()})
#         if query:
#             self.user_cpf = query['cpf']
#             return self.switch_screen('menu')
#         else:
#             return self.dialog_box('Falha', 'N??o foi encontrado uma conta com essas informa????es')
        
    def register_user(self):
        functions = (validate_cpf,validate_name, validate_cep, none, validate_email, none)
        authenticator = validate_fields(self.register, functions)
        if authenticator == True:
            password = hashlib.sha256(self.register.ids.reg_pass.text.encode()).hexdigest()
            query = self.sql.insert_db('app','auth', "('cpf', 'nome', 'cep', 'usuario', 'email', 'senha')",
                                 (self.register.ids.reg_cpf.text, self.register.ids.reg_name.text.upper(),
                                  f'{self.register.ids.reg_cep.text}', f'{self.register.ids.reg_user.text}',
                                  f'{self.register.ids.reg_mail.text}', f'{password}'))
            return self.dialog_box('Sucesso!','Conta registrada com ??xito!')
        else:
            error = f'Registro com os seguintes campos preenchidos incorretamente:'
            for element in range(len(functions)):
                error = error + f'\n {element}'
            return self.dialog_box('Falha', error)
    
    #Utilidades
    def switch_screen(self, screen, **kwargs):
        if kwargs:
            self.sm.transition = SlideTransition(direction = kwargs.get('transition'))
        else:
            self.sm.transition = SlideTransition(direction = 'left')
        self.sm.current = screen
        return
    
    def dialog_box(self, header, message):
        #Criando a caixa de di??logo
        self.dialog = MDDialog(
            title=header,
            text=f'{message}',
            buttons=[MDFlatButton(text='Ok', text_color=self.theme_cls.primary_color,
                                  on_release=self.close),],)
        return self.dialog.open() #Abrindo a caixa de di??logo

    def close(self, instance):
        self.dialog.dismiss()
        
    def change_label(self, screen_name:str, sql_dict: tuple):
        #Os valores s??o os ids dos labels em formato string
        #Retornando a tela
        screen = self.sm.get_screen(f'{screen_name}')
        label_ids = list(screen.ids.keys())
        #Fazendo um query na db
        query = self.sql.select_db('app','auth', {'cpf': self.user_cpf}) # -> Dicion??rio
        
        #Ajustando os dados e fazendo compara????es entre dicion??rios/listas
        query_keys = list(query.keys())
        for i in range(len(query_keys)):
            if query_keys[i] not in label_ids:
                query.pop(query_keys[i])
    
        #Inserindo os dados na tela
        for i in range(len(label_ids)):
            screen.ids[label_ids[i]].text = query[label_ids[i]]
            
if __name__ == '__main__':
    MainApp().run()
