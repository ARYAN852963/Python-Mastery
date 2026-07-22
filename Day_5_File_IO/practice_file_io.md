# Day 5 Practice: File I/O (The 1% Harder Protocol)

You called me out. You are 100% correct. The rule is 10 questions every day, getting progressively harder. No shortcuts.

**ENGINEERING RULE FOR ALL 10 QUESTIONS:** 
You MUST use the `with open(...) as f:` syntax. Do not use `f.close()`. Build these as reusable functions (`def`).

### Level 1: The Basics
**1. The Blank Canvas (Write)**
Write a function `create_file()` that opens a file named `day5.txt` in write mode (`"w"`) and writes the text `"Day 5: 1% Harder"` into it.

**2. The Appender (Append)**
Write a function `add_guest(name)` that opens `guest_list.txt` in append mode (`"a"`) and adds the `name` to the file. Call it 3 times with 3 different names to add them to the list. (Hint: don't forget the newline `\n`).

**3. The Simple Reader (Read)**
Write a function `read_guests()` that opens `guest_list.txt` in read mode (`"r"`), reads the entire file, and prints the text to the terminal.

### Level 2: Accumulators & Math
**4. The Line Counter**
Create a text file with 5 random lines of text. Write a function `count_lines(filename)` that opens the file, loops through it line by line using a `for` loop, and returns the total number of lines. (Use an accumulator variable `count = 0`).

**5. The Word Finder**
Write a function `contains_word(filename, word)`. It reads the file and returns `True` if the specific word is inside the text, and `False` if it isn't. 

**6. The Vowel Scrubber**
Write a function `scrub_vowels(filename)`. It reads a text file, loops through every character, and prints out the text with ALL vowels (`a, e, i, o, u`) completely removed.

### Level 3: Reading & Writing (Full Stack Logic)
**7. The Copycat**
Write a function `clone_file(original, clone)`. It opens the `original` file, reads its contents, and then opens the `clone` file and writes the exact same contents into it.

**8. The Number Filter (Type Conversion)**
Manually create a file called `numbers.txt` and write 5 numbers in it (each on a new line). 
Write a function `extract_evens()` that reads `numbers.txt`. It loops through the lines, checks if the number is EVEN (`% 2 == 0`), and if it is, writes that number into a new file called `evens.txt`. *(Hint: When you read from a file, it gives you a String. You must use `int()` to turn it into a number before doing math!)*

**9. The High Score (The King of the Hill returns)**
Create a file called `scores.txt` with these scores on separate lines: 45, 99, 12, 104, 33.
Write a function `get_highest_score(filename)` that loops through the file, finds the highest integer, and returns it. (You must combine File reading, integer conversion, and the King of the Hill accumulator logic from yesterday).

### Boss Level
**10. The Server Log Censor**
Create a file called `server_log.txt` with these 3 lines:
```text
System booted successfully.
WARNING: Memory usage high.
ERROR: Database connection failed.
```
Write a function `clean_logs()`. It reads `server_log.txt` line by line. 
- If a line contains `"ERROR"`, completely ignore it (do not save it).
- If a line contains `"WARNING"`, replace the word `"WARNING"` with `"RESOLVED"`.
- Write the final, cleaned lines into a new file called `clean_log.txt`. 

Prove to me you are the 1%. Let's go.
