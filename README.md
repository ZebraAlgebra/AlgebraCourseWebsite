# AlgebraCourseWebsite

## Info
This website is used to host contents for the course [Algebera II 2023 (Honor's Program)](https://cool.ntu.edu.tw/courses/25046) at NTU. Basic functionalities of this webside includes hosting the `pdf, tex, png` files of homeworks, and serve as a webview for the contents. This website is built using [`mdbook`](https://rust-lang.github.io/mdBook/), a very friendly command line tool for generating webpages from `md` files.

## File Generation Workflow
1. Automate the process of generating course notifications.
1. Automate the process of combining and annotating homework screenshots using [`Pillow`](https://pillow.readthedocs.io/en/stable/).
1. Manually convert to `.tex` using [mathpix](https://mathpix.com/image-to-latex).
1. Converting `.md` and `.pdf` files where the students can use it to write their homeworks in LaTeX.
1. Build the site using mdbook.

## Branches
1. `workspace` is used for writing scripts for tools assisting file generation.
1. `website` is used for updating webpage contents.
1. `main` is used for combining the two branches.
