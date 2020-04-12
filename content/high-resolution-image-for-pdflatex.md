---
Status: published
Title: High Resolution Image for Pdflatex
Date: 2012-08-09 20:31
Author: Yunyao
Category: notebook
Tags: LaTeX
Slug: high-resolution-image-for-pdflatex
Alias: /blog/2012/08/high-resolution-image-pdflatex
Lang: en
---

While preparing the camera-ready version for our CIKM demo, my colleagues and I found that the screenshot included in our paper appeared to be fairly blurry in the pdf version, even though the original .jpg file looks fine.

I searched online to try to find the solutions. After a few trials and errors, adding the following two lines into the beginning of the latex files (before <span style="font-family: courier new,courier;">\\begin{document}</span>) did the trick.

<span style="font-family: courier new,courier;">\\pdfpxdimen=1in</span>

<span style="font-family: courier new,courier;">\\divide\\pdfpxdimen by 300</span>

The above solution basically forces the pdf file generated at a higher resolution (in this case, 300 dpi) so that everything, including the images, looks better.

The original solution comes from [here](https://stackoverflow.com/questions/5041492/latex-how-to-set-the-pdf-dpi-when-using-images).
