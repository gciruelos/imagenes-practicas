.PHONY = clean


practica1-063_14.zip:
	make -C practica1 informe.pdf
	mv practica1/informe.pdf informe.pdf
	make -C practica1 clean
	zip -r -9 practica1-063_14.zip informe.pdf requirements.txt practica1/*.py
	rm -f informe.pdf

practica2-063_14.zip:
	make -C practica2 informe.pdf
	mv practica2/informe.pdf informe.pdf
	make -C practica2 clean
	zip -9 -r practica2-063_14.zip informe.pdf requirements.txt practica2/*.py
	rm -f informe.pdf

clean:
	rm -f practica*.zip
