import smtplib #-----> smtp serverına bağlanmak için bu modülü dahil ettik
from email.mime.multipart import MIMEMultipart #-----> mailimizin yapısını oluşturacak
from email.mime.text import MIMEText #-----> mailimize ne yazacağımızı bu sınıftan oluşturacağız
import sys

mesaj = MIMEMultipart()                        # Mail yapımızı oluşturuyoruz.

mesaj["From"] = " "         # Maili göndereceğimiz adresimiz (kendi mail adresimiz) (Bu şablonda yalnızca gmail olmalı)
mesaj["To"] = " "     # Mailin iletileceği mail adresi
mesaj["Subject"] = " "        # Mailimizin Konusu

# Mailimizin İçeriği
yazi = """

"""

mesaj_govdesi = MIMEText(yazi,"plain")       # Mailimizin gövdesini bu sınıftan oluşturuyoruz."plain" normal bir yazı için.

mesaj.attach(mesaj_govdesi)                  # Mailimizin gövdesini mail yapımıza ekliyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)      # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.

    mail.ehlo()                # SMTP serverına kendimizi tanıtıyoruz.

    mail.starttls()            # Adresimizin ve Parolamızın şifrelenmesi için gerekli

    mail.login(" "," ")  # SMTP server'ına giriş yapıyoruz. Tırnakların içine kendi mail adresimizi ve parolamızı yazıyoruz.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # Mailimizi gönderiyoruz.Mesaj multipart bir yapıda oldugundan
    #mesaj.as_string() ile mesajı stringe çeviriyoruz.
    print("Mail Başarıyla Gönderildi.!.")

    mail.close()   # Smtp serverımızın bağlantısını koparıyoz.

except:
    sys.stderr.write("Bir sorun oluştu !")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()