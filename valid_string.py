character = 26


def valid_string(string_input):
    freq = [0] * character

    #variable freq[] for storing of each character of string
    for i in range(len(string_input)):
        freq[ord(string_input[i]) - ord('a')] += 1

    # finding first charachter with non-zero frequency
    freq_str = 0
    count_freq_str = 0
    for i in range(character):

        if (freq[i] != 0):

            freq_str = freq[i]
            count_freq_str = 1
            break

    #finding a character with freq different from freq_str
    freq_str2 = 0
    count_freq_str2 = 0
    for j in range(i+1, character):

        if (freq[j] != 0):

            if (freq[j] == freq_str):
                count_freq_str += 1
            else:
                count_freq_str2 = 1
                freq_str2 = freq[j]
                break

    for k in range(j + 1, character):
        
        if (freq[k] != 0):
            if (freq[k] == freq_str):
                count_freq_str += 1
            if (freq[k] == freq_str2):
                count_freq_str2 += 1

            else:
                return False
        if (count_freq_str > 1 and count_freq_str2 > 1):
            return False

    return True


if __name__ == "__main__":
    string_input = "bcbca"

    if (valid_string(string_input)):
        print("True")
    else:
        print("False")
