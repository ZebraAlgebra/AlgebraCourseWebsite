# Glossary of Homeworks

## 📁 About the Homework Files

We will try to supply the relevant homework screenshots, `.tex`, `.pdf`, and links to webpages.
* The `.png` files are the most reliable source. They are combined raw homework screenshots taken from textbooks.
* The `.tex` files are generated for the convenience of those that wish to type down their own solutions. The dependencies are as follows:
    * The commutative diagrams requires `tikzcd`.
    * The embedded pictures requires `graphicx`.
    * The bare minimum is `amsmath`, `amssymb`.
* The `.pdf` files serve both as previews to the `.tex` files and printable documents.
* The webpages are for aesthetic purposes.

## 🌱 Useful Resources
* [q.uiver](https://q.uiver.app/) - GUI for drawing commutative diagrams that supports conversion to `tikzcd` diagrams.
* [mathpix](https://snip.mathpix.com/) - Website for converting math screenshots into LaTeX codes. Reliable and robust.


## 📚 Source of Homeworks

* Week 01: [AtM] 2.14-16. [^note]
* Week 02: [DF] 12.1's 2, 7, 11, 16 and 12.2's 14 (over \\(\mathbb{R}\\)).

[^note]: For confusion on the meaning of abbreviations of names appearing in this subsection, please take a look [here](../home.md#references).


## 📌 Combined files
To appear.


## 📜 Homework Policies

### How to Submit

You may submit via COOL's online submission system or hand it to TA in class.

For the online system, either scanned copies or clear photos of your attempts, or typed ones are all allowed.

### Grading

We will generally give raw letter grades. Submissions without major mistakes and frequent minor mistakes will basically be given the raw letter grade A+ - after conversion, this roughly corresponds to a score of 93 on a scale of 0 to 100.

For the ones that are exceptionally good, few additional points will be added (within the range of the raw letter grade given), where "goodness" is roughly characterized as "those that stands out from the rest of the submissions"; this often means meeting a few of the following criteria:
* those with good presentation, such as:
    * well-structured arguments
    * well-organized ideas
    * good usage of notations and formalisms
    * an emphasis on clearly presenting the core ideas
    * a sense of authenticity
    * few occurences of apparent grammatical errors and typos
* those that attempted harder questions when it is not required by the description of the assignment
* those that demonstrated creative ideas and deep insights towards a problem
* those that verified the non-trivial details that others might have missed

### Policy on Late Submissions

Suppose a submission is late in \\(x\\) days. The grade of that submission will be penalized according to the following rules:

* For \\(0\leq x\leq 3\\), the letter grade will be adjusted downwards \\(\lceil x \rceil\\) units of plus/minus grades.
* For \\(x > 3\\), the formula will be \\(3 + \lfloor(x - 3) / 5\rfloor\\).

The decision boundary is a soft one; that is, when a submission is near a decision boundary, we will calculate towards the one that results in less penalty.

### Formula for Final Grades on Homeworks
Suppose the grades (converted to a scale of 0 to 100) of an individual student are - in ascending order - given by

\\[a\_0,a\_1,\dotsc,a\_{n-1}\\]

then the total grade is calculated as a weighted average, given by

\\[\frac{\left(\sum\_{i=0}\^{n-1}a\_i\right)-0.50a\_0-0.35a\_1-0.20a\_2}{n-(0.50+0.35+0.20)}.\\]