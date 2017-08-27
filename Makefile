.PHONY = clean

practica1-063_14.zip:
	make -C practica1 informe.pdf
	mv practica1/informe.pdf informe.pdf
	make -C practica1 clean
	zip -r practica1-063_14.zip informe.pdf requirements.txt practica1/*.py
	rm -f informe.pdf

clean:
	rm -f practica*.zip