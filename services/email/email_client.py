import imaplib
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header
from email.utils import make_msgid
from settings.configurations import DefaultConfig



class EmailClient:
    def __init__(self, config: DefaultConfig, mailbox = 'inbox') -> None:
        self.config = config
        self.mailbox = mailbox

        self.imap = imaplib.IMAP4_SSL(host=config.IMAP_SERVER)
        self.imap.login(user=config.FROM_EMAIL, password=config.FROM_PWD)

   
    def _create_message(self, to: str, message_id:str,  subject: str, message_text: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message['Message-ID'] = make_msgid()
        # message['In-Reply-To'] = message_id
        message['References'] = message_id
        message['From'] = self.config.FROM_EMAIL
        message['To'] = to
        message['Subject'] = subject

        # html_default_ans = Answer(message_text)
        # html = html_default_ans.botAnswer()
        # footer = html_default_ans.footer()
        # message.attach(MIMEText(html, 'html'))
        # message.attach(MIMEText(footer, 'html'))      
        
        message.attach(MIMEText(message_text, 'plain'))
        return message


    def reply(self, to: str, message_id: str, subject: str, message_text: str) -> None:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.config.FROM_EMAIL, self.config.FROM_PWD)
    
        message = self._create_message(
            to=to, 
            message_id=message_id, 
            subject=subject, 
            message_text=message_text
        ).as_string()

        server.sendmail(self.config.FROM_EMAIL, to, message)
        server.quit()

        print("\nEmail enviado!\n")


# conf = DefaultConfig()
# email = Email(config=conf)
# email.reply(
#     'gabriel.assunsas@gmail.com',
#     'Teste - Message Id',
#     'Teste - Subject',
#     'Conteúdo'
# )


'''
tela de resetar senha no app (dois botões):
    1. solicitar reset de senha
        a. será enviado um hash para o email cadastrado (tempo ativo: 10 min)
            {
                'request_reset_password': bool
                'hash_reset_password'   : str
                'time_request'          : datetime 
            }
    2. já possuo o codigo de renovação
        a. o usuario copia esse hash e cola na tela de resetar senha
        b. o hash será validado pela api
            caso success: mostar a tela de redefinição de senha
            caso fail: mostrar mensagem de erro
'''
