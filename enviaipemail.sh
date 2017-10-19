#! /bin/bash

# Este script envia e-mails quando detectado conectividade de rede na interface eth0.

#parametros
RPINAME="$(cat /etc/hostname | sed 's/^[\t]*//;s/[ \t]*$//')"
MAILTO="erivandoramos@bol.com.br"

# obtem interface
if [ $# -eq 0 ]
then
        IFC="eth0"
else
        IFC="$1"
fi

ifconfig $IFC &> /dev/null
if [ $? -ne 0 ]
then
        exit 1
fi

# obtem o ip da interface
PRIVATE=$(ifconfig $IFC | grep "inet addr:" | awk '{ print $2 }')
IPV6=$(ifconfig $IFC | grep "Scope:Global" | awk '{ print $3 }')
PRIVATE=${PRIVATE:5}

# sai se o ip fpr vazio
if [ -z $PRIVATE ]
then
    exit 0
fi

# aguarda 2 minutos aguardando o RTC durante boot de 10 em 10 segundos
for I in {1..12}
do
    sleep 10
    if [ $(date +%Y) != "1970" ]
    then
        # confirma o relogio e obtem o ip publico
                PUBLIC=$(curl -s checkip.dyndns.org|sed -e 's/.*Current IP Address: //' -e 's/<.*$//')
        MSG="Dispositivo: $RPINAME\nInterface de rede: $IFC\nIP local: $PRIVATE\nIP publico: $PUBLIC $IPV6\nData/hora: $(date +%F\ %T)"
        echo -e $MSG | mail -s "[IP]$RPINAME" "$MAILTO"
        exit 0
    fi
done

