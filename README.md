# Confounded Paper

I'm using the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin in VSCode with the `latex-workshop.docker.enabled` setting set to `true`.

With this, the PDF automatically builds anytime I save the `.tex` file.

I'm also using [Better BibTeX](https://retorque.re/zotero-better-bibtex/) in conjunction with [Zotero](https://www.zotero.org/) and the [Zotero Connector Chrome Plugin](https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc?hl=en) for managing citations.

## Conversion to Docx

Make sure the line `\usepackage[square,numbers]{natbib}` is commented out and replaced with `\usepackage{natbib}` in the main file.

You might have to remove all the junk with `rm thesis!(.tex)`.

```bash
latex2rtf thesis
```

Then open it up in Word & convert to Docx

## Running the code

This will run the entire analysis: downloading and tidying the data, batch adjusting the data, calculating metrics, and making charts and tables. It takes around 4 hours to run to completion.

After running, the output figures and tabless will be in `code/data/output/`.

Dependencies:

- R
- Python >=3.6
- Pandas
- Scikit-Learn
- Numpy
- wget

```bash
cd code/
bash run_all.sh
```
