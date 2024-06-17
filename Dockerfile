FROM ubuntu:latest
RUN apt-get -y update && apt-get install -y fortunes
RUN mkdir -p wisecow
WORKDIR /wisecow
ADD ./wisecow.sh .
RUN chmod +x wisecow.sh
EXPOSE 4499
CMD ["sh", "wisecow"]