FROM fedora:latest

RUN dnf update -y && \ 
    dnf install -y python3 python3-pip && \ 
    dnf clean all

WORKDIR /usr/src/app

COPY requisitos.txt requisitos.txt
RUN pip install --no-cache-dir -r requisitos.txt
COPY app.py .


EXPOSE 5000

CMD ["python3",  "app.py"]



