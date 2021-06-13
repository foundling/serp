import sys

def main():

    files = sys.argv[1:] 

    for file in files:
        try:
            content = open(file).readlines()
        except FileNotFoundError as e:
            print("file {} was not found", file)
        except:
            print("something went wrong!")

        print(content)


main()
