
# # Reading a txt file using Python
# with open("/home/dinesh-p/Documents/C_git/ml_learning/data.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Read the txt file line by line
# with open("/home/dinesh-p/Documents/C_git/ml_learning/data.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# # Word Count in a txt file
# with open("/home/dinesh-p/Documents/C_git/ml_learning/data.txt", "r") as file:
#     content = file.read()
#     words = content.split()
#     word_count = len(words)
#     print(f"Total number of words: {word_count}")

# # Write to a txt file
# with open("/home/dinesh-p/Documents/C_git/ml_learning/output.txt", "w") as file:
#     file.write("This is an output file created using Python.\n")

# # Append to a txt file
# with open("/home/dinesh-p/Documents/C_git/ml_learning/output.txt", "a") as file:
#     file.write("Appending a new line to the output file.\n")

with open("/home/dinesh-p/Documents/C_git/ml_learning/data.txt", "a") as file:
    file.write("This line will be added at the end.\n")

with open("/home/dinesh-p/Documents/C_git/ml_learning/data.txt", "r") as file:
    content = file.read()
    print(content)