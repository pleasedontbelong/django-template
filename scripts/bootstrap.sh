#!/bin/sh

if [ "$1" = "--dev" ]; then
	export ENVIRONMENT=local
    pip install -r requirements/dev.txt
    if [ ! -f ./settings/local.default.py ]; then
        cp ./settings/local.default.py ./settings/local.py
    fi
    git init
    echo -n "Do you want to create a superuser now? (y/n)? "
	read answer
	if echo "$answer" | grep -iq "^y" ;then
	    echo Yes
	fi
elif [ "$1" = "--prod" ]; then
    pip install -r requirements/prod.txt
else
    echo "argument needed (--dev, --prod)"
fi
