#Longest Common Prefix:

def longest_common_prefix(strs):
    if not strs:
        return ""
#Find shortest string:
    min_len = min(len(s) for s in strs)
# Iterate through each character index up to the length of the shortest string
    for i in range(min_len):
# Use zip to group characters from each string at the current index
        chars = [s[i] for s in strs]
# Check if all characters at the current index are the same
        if len(set(chars)) != 1:
            return strs[0][:i]
    return strs[0][:min_len]
#Exapmles:
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""
