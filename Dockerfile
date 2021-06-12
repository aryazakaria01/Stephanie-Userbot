# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Userbot
# Stephanie-UserBot
# Userbot
RUN git clone -b Geez-UserBot https://github.com/aryazakaria01/Stephanie-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/aryazakaria01/Stephanie-UserBot/Geez-UserBot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
