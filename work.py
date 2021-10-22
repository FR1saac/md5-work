def main():
    string = list("aaaaaa")
    print("".join(string))
    while True:
        while string[5] != "z":
            string[5] = chr(ord(string[5]) + 1)
            print("".join(string))
        if all(letter == "z" for letter in string):
            break
        if string[5] == "z":
            string[5] = "a"
            string[4] = chr(ord(string[4]) + 1)
        for idx in range(3, -1, -1):
            if string[1 + idx] == chr(ord("z") + 1):
                string[1 + idx] = "a"
                string[idx] = chr(ord(string[idx]) + 1)
        print("".join(string))

        

        

                
        
if __name__ == "__main__":
    main()
