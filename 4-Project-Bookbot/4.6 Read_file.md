![alt text](img/image-3.png)

### Work done by <span style="color:#ECAD35">Sara Eilenstine</span>, course and media are through <a href="https://www.boot.dev/">Boot.dev</a>!

<br>

# ADD BOOKS

1. Make a new directory called `books`

```bash
mkdir books
cd books/
```

2. Add `frakenstein.txt` book to this directory and paste the book text from provided link.

```bash
nano frakenstein.txt
```

3. Use a `.gitignore` file
   We don't want to save the entire book in our Git repository. Generally speaking, Git is for code, not for data.

```bash
# Go to home dir
cd ..
nano .gitignore
# books/
```

4. Verify you setup correctly
   If you see the `.gitignore` file then you most likely missed the `.` at the beginning

```bash
ls
# README.md  books  main.py
```

# READ THE BOOK

Change `main.py` so that instead of printing "hello world", it reads the contents of the "frankenstein.txt" and prints it _**all**_ to the console. Call `main()` to run program.

```python
def main():
    with open("books/frakenstein.txt") as book:
        file_contents = book.read()
    return file_contents

print(main())

# ALTERNATIVE
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()
```

### HINT

// _Keep in mind that `path_to_file` needs to be relative to wherever you're running the program from. If you're running the program from the root of your project, you would use `books/frankenstein.txt`. The path to the file is a string so it needs to be in quotes!_

# COUNT WORDS

Add a new function to your script that takes the text from the book as a string, and returns the number of words in the string. Add a `print()` statement, then run your code to make sure it's doing what you expect. The Frankenstein book should contain `77986` words!

```python
def main():
        with open("books/frankenstein.txt") as book:
                file_contents = book.read()
        return file_contents

def count(book_file):
        count = 0
        lines = book_file.split()
        #print(lines)
        for i in lines:
                count += 1
        return count

print(count(main()))

# ALTERNATIVE
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
```

# COUNT CHARACTERS

Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any character to lowercase, we don't want duplicates.

```python
def main():
        with open("books/frankenstein.txt") as book:
                file_contents = book.read()
        return file_contents

def count_words(book_file):
        count = 0
        lines = book_file.split()
        for i in lines:
                count += 1
        print(f"There are {count} many words.")
        return count

def get_chars(book_file):
        char_dict = {}
        lines = book_file.lower().split() # Make words lower case
        for i in lines: # Get the word
                for j in i: # Get just the characters
                        if j in char_dict:
                                char_dict[j] += 1
                        else:
                                char_dict[j] = 1
        print(char_dict)

text = main()

# ALTERNATIVE
# Notice how the main() is getting all of the functions. This is "cleaner" and I should keep this in mind moving forward.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
```

### NOTE

// _I'd recommend using a dictionary of `String` -> `Integer`. When you print out the dictionary it should look something like this:_

```python
{'p': 6121, 'r': 20818, 'o': 25225, ...
```

// _To convert a string to lowercase use the .lower() method:_

```python
my_string = "FOR FRODO"
lowered_string = my_string.lower()
print(lowered_string)
# for frodo
```

# PRINT A REPORT

Let's aggregate all the word and character data into a nice report that we can print to console.

An idea of what it should look like:

```bash
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
.
.
.
--- End report ---
```

1. Inside of the `main` function, print the first line using `f-string` where we already assigned the `book_path` variable.

```python
book_path = "books/frankenstein.txt"
print(f"--- Begin report of {book_path} ---")
```

2. Using `num_words` function, print the next line using `f-string`

```python
print(f"{num_words} words found in the documents \n")
```

3. Get the report of the _alpha only_ characters in this book.

- First, figure out how to split the dictionary into a list of dictionaries.
- After mulling over the internet, think to yourself, why can't I just sort the dictionary values by the times they show up and do that in place?
  **BIG** thanks to this Stack Overflow post:

## Reddit User: wjandrea and use of Lambda for in-place dictionary sorting.

https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

Python 3.7+ or CPython 3.6
Dicts preserve insertion order in Python 3.7+. Same in CPython 3.6, but it's an implementation detail.

```python
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```

or

```python
>>> dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```

Older Python
It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted. Dictionaries are inherently orderless, but other types, such as lists and tuples, are not. So you need an ordered data type to represent sorted values, which will be a list—probably a list of tuples.

For instance,

```python
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
```

`sorted_x` will be a list of tuples sorted by the second element in each tuple. `dict(sorted_x) == x`.

And for those wishing to sort on keys instead of values:

```python
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
```

In Python3 since <a href="https://stackoverflow.com/a/15712231/4293057">unpacking is not allowed</a> we can use

```python
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
```

If you want the output as a dict, you can use `collections.OrderedDict`:

```python
import collections

sorted_dict = collections.OrderedDict(sorted_x)
```

---

## Now, taking what we learned above and implementing it.

I ended up using `lambda` for my reporting function.

```python
def get_report(chars_dict):
    # Dict.sorted() method (iterable, key=?, reverse=True/False)
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Check to make sure the key is an alpha character
    for i in sorted_dict:
        # If it is: print it on the report
        if i.isalpha():
            print(f"The '{i}' character was found {sorted_dict[i]} times")
```

# SOLUTION

```python
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the documents \n")
    get_report(chars_dict)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_report(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Got help here: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    for i in sorted_dict:
        if i.isalpha():
            print(f"The '{i}' character was found {sorted_dict[i]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

# ALTERNATIVE
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
```

# COMMIT TO GIT

```bash
cattelia@Amaterasu:~/Github/bookbot$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        .main.py.swp
        main.py
        test.py

nothing added to commit but untracked files present (use "git add" to track)
# Stage changes for committing
cattelia@Amaterasu:~/Github/bookbot$ git add .

# Confirm their addition
cattelia@Amaterasu:~/Github/bookbot$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   .main.py.swp
        new file:   main.py
        new file:   test.py

# Commit changes
cattelia@Amaterasu:~/Github/bookbot$ git commit -m "Completed Bookbot Reader"
[main 8585129] Completed Bookbot Reader
 4 files changed, 83 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 .main.py.swp
 create mode 100644 main.py
 create mode 100644 test.py

 # Push to Github
 cattelia@Amaterasu:~/Github/bookbot$ git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.21 KiB | 411.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/cattelia/bookbot
   4d6657d..8585129  main -> main
```

---

### Work done by <span style="color:#ECAD35">Sara Eilenstine</span>, course and media are through <a href="https://www.boot.dev/">Boot.dev</a>!

<br>

![alt text](img/image-4.png)
