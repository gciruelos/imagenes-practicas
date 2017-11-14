.PHONY = clean view-informe
IMGS_PDF = $(wildcard informe-imgs/*.pdf)
IMGS_JPG = $(IMGS_PDF:.pdf=.jpg)

informe.pdf: informe.tex $(IMGS_JPG) $(wildcard ej1-imgs/*.png)
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make informe.tex
	ls -lha informe.pdf

informe-imgs/%.jpg: informe-imgs/%.pdf
	convert -density 100 $< -quality 80 $@

view-informe: informe.pdf
	zathura informe.pdf &

clean:
	latexmk -CA
	rm -rf informe-imgs/*.jpg
