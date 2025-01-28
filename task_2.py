import marisa_trie

class LongestCommonWord:
    def __init__(self):
        self.trie = marisa_trie.Trie()
        self.words = set()
    
    def put(self, word, value):
        if isinstance(word, str):
            self.words.add(word)
            self.trie = marisa_trie.Trie(self.words)
    
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list):
            return ""
        if not strings:
            return ""
        if not all(isinstance(s, str) for s in strings):
            return ""
        
        first_string = strings[0]
        if not first_string:
            return ""
            
        lcp = []
        
        for i in range(len(first_string)):
            current_char = first_string[i]
            if all(len(s) > i and s[i] == current_char for s in strings):
                lcp.append(current_char)
            else:
                break
                
        return ''.join(lcp)

if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    assert trie.find_longest_common_word([]) == ""

    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["apple", 123]) == ""

    print("All tests passed!")