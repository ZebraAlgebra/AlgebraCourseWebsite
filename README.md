# AlgebraCourseWebsite

## Info
This website is used to host contents for the [course Algebera II](https://cool.ntu.edu.tw/courses/25046) at NTU in 2023. Basic functionalities of this webside includes hosting the `pdf, tex, png` files of homeworks, and serve as a webview for the contents. This website is built using `mdbook`, a very friendly command line tool for generating webpages from `md` files.

## File Generation Workflow
1. Automate the process of generating course notifications.
2. Converting `.md` files to `.tex` and `.pdf` files where the students can use it to write their homeworks in LaTeX.
3. Automate the process of combining and annotate homework screenshots using `Pillow`.
4. Using OCR tools in Python to convert images to texts and LaTeX formulae using `pic2tex` and `pytesseract`. Perhaps design a GUI utilizing both.
5. Automate the process of updating `.md` files of the site.

The overall expected workflow would be as follows:
1. Get the info of homework.
2. Generate notification, and paste it to NTUCOOL.
3. Get screenshots.
4. Paste and annotate as one big `.png`.
5. Convert `.png` to text file and convert it as incomplete `.tex`.
7. Autocomplete `.tex` and convert to `.md`, `.tex` and `.pdf`.
8. Once the `.png`, `.md`, `.tex`, `.pdf` are ready, update webpages.
