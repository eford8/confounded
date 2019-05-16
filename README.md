# My Master's Thesis

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

## Prepping for Thesis Submission

[This page](https://gradstudies.byu.edu/file/adv-form-11) has a checklist for university requirements.

[This one](http://biology.byu.edu/Portals/10/docs/gradForms/ETD%20College%20of%20Life%20Sciences%20Requirements.pdf) has the college requirements.

[This one](https://gradstudies.byu.edu/page/etd-instruction-packet-0) has links to all the info you need to graduate.
