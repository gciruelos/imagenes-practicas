.PHONY = clean view-informe
IMGS_PDF = $(wildcard informe-imgs/*.pdf)

informe.pdf: informe.tex $(IMGS_PDF)
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make informe.tex
	ls -lha informe.pdf

informe-imgs/%.jpg: informe-imgs/%.pdf
	convert -density 150 $< -quality 80 $@

view-informe: informe.pdf
	zathura informe.pdf &

clean:
	latexmk -CA
	rm -rf informe-imgs/*.jpg
