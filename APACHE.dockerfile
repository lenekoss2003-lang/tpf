FROM fedora:42

RUN dnf install -y httpd sudo && \
    dnf clean all

COPY ./html/ /var/www/html/

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]