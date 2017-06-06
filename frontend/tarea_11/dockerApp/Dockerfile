FROM frolvlad/alpine-python3
LABEL maintainer "manuelbr <manuelbr994@gmail.com>"

RUN apk update && apk upgrade \
    && apk add git supervisor gcc linux-headers python3-dev musl-dev freetype-dev libjpeg-turbo-dev lcms2-dev openjpeg-dev tiff-dev libwebp-dev libxml2-dev libxslt-dev zlib-dev \
    && pip install gunicorn  \
    && git clone https://github.com/manuelbr/web_restaurante_SSBW.git /home/web_restaurante_SSBW  \
    && cd /home/web_restaurante_SSBW/sitio_web && pip install -r requirements.txt  \
    && apk del git gcc linux-headers

EXPOSE 8000

CMD ["gunicorn sitio_web.wsgi", "-n"]
