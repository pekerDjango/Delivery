SIGeP
=====

Sistema Integrado de Gestión de Pedidos



Requerimientos

    Python 2.7 
    virtualenv (o similar, para linux, windows pip)

Setup del ambiente de desarrollo

    Clonar repo git clone https://github.com/pekerDjango/Delivery.git
    Activar virtualenv . virtualenv/bin/activate
    Instalar dependencias pip install -r requirements.txt
    Setup BD python manage.py syncdb
    Correr migraciones python manage.py migrate
    
Otras configuraciones:

    encoding de archivos: UTF-8
  




