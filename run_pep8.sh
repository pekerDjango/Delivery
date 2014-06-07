#!/bin/bash

IGNORE=E128

if [ "$VIRTUAL_ENV" = "" ] ; then
	echo "ERROR: virtualenv (o alguno de la flia.) no encontrado"
	exit 1
fi

cd $(dirname $0)

pep8 --ignore=$IGNORE SiGeP/*.py
pep8 --ignore=$IGNORE ComponentesDePedido/*.py
pep8 --ignore=$IGNORE PedidoRegistrado/*.py
pep8 --ignore=$IGNORE RecursosDeEmpresa/*.py
pep8 --ignore=$IGNORE ConfiguracionDeComponentes/*.py

exit $?
