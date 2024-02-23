Basically a fork of [raiyansayeed's repo](https://github.com/raiyansayeed/leetcode-download-questions) but is specilized for leetcode Chinese site.

Repo is updated to work with LeetCode's GraphQL API and only includes some questions. The code should theoretically work with any Leetcode question list though. 

Questions are currently only available in PDF format. 

Feel free to submit a PR to include other lists e.g topic specific lists.

### Usage

You can download '.pdf' file from this repo and view it however you want. 

### Building PDF 

This repo relies on WeasyPrint which itself has some annoying dependencies to install. Refer to their [documentation](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html) for platform specific installation steps. 

__NOTE__ For MacOS you may also need to install LibMagic with `brew install libmagic`

Run the following to install other dependencies 
```python
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In virtualenv, run `python3 export_all_questions.py` to generate PDF. 

### Updating questions

Add the new question link in the file `question_links.txt` and run `export_all_questions.py` python script. 

To get all questions in a LeetCode list, visit a LeetCode URL with problem links visible on the page e.g `https://leetcode.com/list/xi4ci4ig/`. Open up the dev console and run the following code. Make sure all problem links are visible e.g extend list view > 50 to show all problem links if needed. Then  replace all occurrences of `leetcode.com` with `leetcode.cn` in all links.

```
var links = document.getElementsByTagName('a');
var all_links = Array.prototype.slice.call(links);
var problems_str = "";
all_links.forEach(function(val) {
    if (val.href.includes('/problems/') && !val.href.includes('/solution')) {
        problems_str = problems_str.concat(`${val.href}\n`)
    }
});
console.log(problems_str)
```