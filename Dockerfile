FROM python:3.9

WORKDIR /opt/mockbot
ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]