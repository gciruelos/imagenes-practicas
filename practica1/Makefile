
informe.pdf: informe.tex informe-imgs/*
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make informe.tex

view-informe: informe.pdf
	zathura informe.pdf

clean:
	latexmk -CA
