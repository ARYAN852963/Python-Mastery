# def create_file():
#     with open("day5.txt", "w") as f:
#        a = f.write("Day 5: 1% Harder")
# create_file()

# 2.
# def add_guest(name):
#    with open("guest_list.txt", "a") as f:
#       f.write(f"{name}\n")
# add_guest("Superman")
# add_guest("Hanuman")
# add_guest("Flash")

# 3.
# with open("guest_list.txt", "r") as f:
#       data = f.read()
#       print(data)

# 4.
# def count_lines(filename):
#    count = 0
#    with open("guest_list.txt") as f: 
#       for line in f: 
#        count = count + 1
#        print(count)
# count_lines("guest_list.txt")

# 5.
# def contains_word(filename, word):
#    with open("guest_list.txt", "r")as f :
#       text = f.read()
#       if word in text:
#             return True
#       else:
#          return False
# a = contains_word("guest_list.txt", "Blue")
# print(a)

# 6.
# def scrub_vowels(filename):
#    clean_text = ""
#    with open("guest_list.txt", "r") as f:
#        letter = f.read()
#        for i in letter:
#         if i.lower() not in "aeiou":
#          clean_text = clean_text + i
#        return clean_text
# a  = scrub_vowels("guest_list.txt")
# print(a)

# 7.
# def clone_file(original, clone):
#    with open(original, "r") as f:
#       text = f.read()
#    with open(clone, "w") as f:
#       f.write(text)
#    print(text)

# clone_file("guest_list.txt", "guest_list_clone.txt")

# 8.
# def extract_evens(filename):
#    # Open the file (using the filename variable!)
#    with open(filename, "r") as f:
      
#       # Loop through ONE FULL LINE at a time (e.g. "10\n")
#       for line in f:
         
#          # Turn the full line into an integer (e.g. 10)
#          num = int(line)
         
#          # Check if it is even
#          if num % 2 == 0:
            
#             # If it is even, open the NEW file and append the number to it
#             with open("even_numbers.txt", "a") as new_file:
#                new_file.write(f"{num}\n")
# extract_evens("numbers.txt")

# 9.
# def get_highest_score(filename):
#    a = 0
#    with open(filename, "r") as f:
#       for i in f:
#          num = int(i)
#          if num > a:
#             a = num
#    print(a)
            

# get_highest_score("scores.txt")

# 10.
def clean_logs(filename):
    clean_data = "" # Your string accumulator
    
    # 1. Open the file and loop line-by-line
    with open(filename, "r") as f:
        for line in f:
            
            # 2. Check for ERROR
            if "ERROR" in line:
                pass # Do absolutely nothing
                
            # 3. Check for WARNING
            elif "WARNING" in line:
                # Use replace to create a fixed line, then add it to your accumulator
                fixed_line = line.replace("WARNING", "RESOLVED")
                clean_data = clean_data + fixed_line
                
            # 4. If it's a normal line (System booted successfully)
            else:
                # Add the normal line to your accumulator
                clean_data = clean_data + line
                
    # 5. OUTSIDE the loop and OUTSIDE the first 'with', open the NEW file in Write mode ("w")
    # and write your entire clean_data string into it!
    with open(filename, "w") as f:
      f.write(clean_data)
clean_logs("server_log.txt")


