import numpy as np

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

#Bibliotecas do proprio aplicativo
from psql import *
from authenticator import *

#Criptografia unidirecional
import hashlib

class consignado(Screen):
    pass
class menu(Screen):
    pass
class login(Screen):
    pass
class register(Screen):
    pass
class salario(Screen):
    pass
class configuracoes(Screen):
    pass
class configuracoes_alter(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        #Estilo
        Builder.load_file("main2.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
        #Telas
        self.sm = ScreenManager()
        
        self.menu = menu(name="menu")
        self.sm.add_widget(self.menu)
        
        self.login_screen = login(name="login")
        self.sm.add_widget(self.login_screen)
        
        self.register = register(name="register")
        self.sm.add_widget(self.register)
        
        self.consignado = consignado(name="consignado")
        self.sm.add_widget(self.consignado)
        
        self.salario = salario(name="salario")
        self.sm.add_widget(self.salario)
        
        self.configuracoes = configuracoes(name="configuracoes")
        self.sm.add_widget(self.configuracoes)
        
        self.configuracoes_alter = configuracoes_alter(name="configuracoes_alter")
        self.sm.add_widget(self.configuracoes_alter)
        
        #configurações do servidor SQL
        self.sql = psql("localhost","postgres","postgres","admin")
        self.sm.current = "login"
        return self.sm

    def login(self):
#         if self.login_screen.ids.user.text=='1' and self.login_screen.ids.password.text=='1':
#             return self.switch_screen("menu")
        query = self.sql.select_db("app","auth", {"usuario": self.login_screen.ids.user.text,
                                                "senha" : hashlib.sha256(self.login_screen.ids.password.text.encode()).hexdigest()})
        if query:
            self.user_cpf = query['cpf']
            return self.switch_screen("menu")
        else:
            return self.dialog_box("Falha", "Não foi encontrado uma conta com essas informações")
        
    def register_user(self):
        authenticator = validate_fields(self.register,
                                        (validate_cpf,validate_name, validate_cep, none, validate_email, none))
        if authenticator == True:
            password = hashlib.sha256(self.register.ids.reg_pass.text.encode()).hexdigest()
            query = self.sql.insert_db('app."auth"', '("cpf", "nome", "cep", "usuario", "email", "senha")',
                                 (self.register.ids.reg_cpf.text, self.register.ids.reg_name.text.upper(),
                                  f'{self.register.ids.reg_cep.text}', f'{self.register.ids.reg_user.text}',
                                  f'{self.register.ids.reg_mail.text}', f'{password}'))
            return self.dialog_box("Sucesso!","Conta registrada com êxito!")
        else:
            return self.dialog_box("Falha", "Registro com algum campo preenchido incorretamente")
    
    #Utilidades
    def switch_screen(self, screen, **kwargs):
        if kwargs:
            self.sm.transition = SlideTransition(direction = kwargs.get('transition'))
        else:
            self.sm.transition = SlideTransition(direction = 'left')
        self.sm.current = screen
        return
    
    def dialog_box(self, header, message):
        #Criando a caixa de diálogo
        self.dialog = MDDialog(
            title=header,
            text=f"{message}",
            buttons=[MDFlatButton(text="Ok", text_color=self.theme_cls.primary_color,
                                  on_release=self.close),],)
        return self.dialog.open() #Abrindo a caixa de diálogo

    def close(self, instance):
        self.dialog.dismiss()
        
    def change_label(self, screen_name:str, sql_dict: tuple):
        #Os valores são os ids dos labels em formato string
        #Retornando a tela
        screen = self.sm.get_screen(f'{screen_name}')
        label_ids = list(screen.ids.keys())
        #Fazendo um query na db
        query = self.sql.select_db("app","auth", {"cpf": self.user_cpf}) # -> Dicionário
        
        #Ajustando os dados e fazendo comparações entre dicionários/listas
        query_keys = list(query.keys())
        for i in range(len(query_keys)):
            if query_keys[i] not in label_ids:
                query.pop(query_keys[i])
    
        #Inserindo os dados na tela
        #Pode mudar
        for i in range(len(label_ids)):
            screen.ids[label_ids[i]].text = query[label_ids[i]]
        
        return
if __name__ == '__main__':
    MainApp().run()
