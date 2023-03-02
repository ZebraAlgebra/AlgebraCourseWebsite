# AlgebraCourseWebsite

## Info
This website is used to host contents for the [course Algebera II](https://cool.ntu.edu.tw/courses/25046) at NTU in 2023. Basic functionalities of this webside includes hosting the `pdf, tex, png` files of homeworks, and serve as a webview for the contents.

## File Generation Workflow
I plan to use Python as the primary tool for content generation. This includes:
1. Automate the process of generating course notifications.
2. Converting `.md` files to `.tex` and `.pdf` files where the students can use it to write their homeworks in LaTeX.
3. Automate the process of combining and annotate homework screenshots using `Pillow`.
4. Using OCR tools in Python to convert images to texts and LaTeX formulae using `pic2tex` and `pytesseract`.
5. Automate the process of updating all the pages of the site.

The overall expected workflow would be as follows:
1. Get the info of homework.
2. Generate notification, and paste it to NTUCOOL.
3. Get screenshots.
4. Paste and annotate as one big `.png`.
5. Convert `.png` to text file.
6. Double check and manually turn it into a `.md`.
7. Convert `.md` to `.tex` and `.pdf`.
8. Once the `.png`, `.md`, `.tex`, `.pdf` are ready, update webpages.

## Functionalities of the site
These will be added along the way. As for now, we will only use basic JavaScript to update links and not add other functionalities.


