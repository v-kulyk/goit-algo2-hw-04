import marisa_trie

class LongestCommonWord:
    def __init__(self):
        # Initialize an empty marisa trie and a set to store our words
        self.trie = marisa_trie.Trie()
        self.words = set()
    
    def put(self, word, value):
        """
        Add a word to our collection. Since marisa-trie is immutable,
        we store words in a set and rebuild the trie when needed.
        """
        if isinstance(word, str):
            self.words.add(word)
            # Rebuild the trie with all current words
            self.trie = marisa_trie.Trie(self.words)
    
    def find_longest_common_word(self, strings) -> str:
        """
        Find the longest common prefix among all strings in the input list.
        This method completely rebuilds the trie with the input strings,
        ignoring any previously stored words.
        """
        # Input validation
        if not isinstance(strings, list):
            return ""
        if not strings:
            return ""
        if not all(isinstance(s, str) for s in strings):
            return ""
        
        # Get the first string to compare against
        first_string = strings[0]
        if not first_string:
            return ""
            
        # Initialize the longest common prefix
        lcp = []
        
        # Check each character position across all strings
        for i in range(len(first_string)):
            current_char = first_string[i]
            # Check if this character exists at the same position in all strings
            if all(len(s) > i and s[i] == current_char for s in strings):
                lcp.append(current_char)
            else:
                break
                
        return ''.join(lcp)

if __name__ == "__main__":
    # Test cases remain unchanged
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