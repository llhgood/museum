FROM python:3.7
ENV PYRHONUNBUFFERED 1
RUN mkdir -p /var/www/html/mysite
WORKDIR /var/www/html/mysite
ADD . /var/www/html/mysite
RUN sed -i 's/\r//' /var/www/html/mysite/start.sh
RUN chmod +x /var/www/html/mysite/start.sh
RUN pip install -r requirements.txt
EXPOSE 8088:8089
ENTRYPOINT python manage.py runserver 0.0.0.0:8089


