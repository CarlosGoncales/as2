#Imagem a se usar
FROM selenium/standalone-chrome

#Diretorio
WORKDIR /app

#Faz a copia
COPY . /app

#usuario
USER root

#instala dependencias
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install -r requirements.txt

#executta python
CMD python3 app.py
