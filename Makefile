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

practica4-063_14.zip:
	make -C practica4 informe.pdf
	mv practica4/informe.pdf informe.pdf
	make -C practica4 clean
	zip -9 -r practica4-063_14.zip informe.pdf requirements.txt practica4/*.py practica4/imgs-ej3/*.png
	rm -f informe.pdf

practica5-063_14.zip:
	make -C practica5 informe.pdf
	mv practica5/informe.pdf informe.pdf
	make -C practica5 clean
	zip -9 -r practica5-063_14.zip informe.pdf requirements.txt practica5/*.py
	rm -f informe.pdf

practica6-063_14.zip:
	make -C practica6 informe.pdf
	mv practica6/informe.pdf informe.pdf
	make -C practica6 clean
	zip -9 -r practica6-063_14.zip informe.pdf requirements.txt practica6/*.py
	rm -f informe.pdf

clean:
	rm -f practica*.zip
