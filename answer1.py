class TokenAnalyzer:
    def __init__(self):
        self.tokens = []

    def ingest(self, string):
        self.tokens.append(string)

    def appearance(self, prefix):
        count = sum(token.startswith(prefix) for token in self.tokens)
        return count / len(self.tokens)

# Usage example
analyzer = TokenAnalyzer()
analyzer.ingest('oursky:uk:dev')
analyzer.ingest('oursky:hk:design')
analyzer.ingest('oursky:hk:pm')
analyzer.ingest('oursky:hk:dev')
analyzer.ingest('skymaker')

print(analyzer.appearance('oursky'))  # Output: 0.8
print(analyzer.appearance('oursky:hk'))  # Output: 0.6
print(analyzer.appearance('skymaker')) #output 0.2
print(analyzer.appearance('oursky:hk:dev')) #output 0.2

analyzer.ingest('skymaker:london:ealing:dev')
analyzer.ingest('skymaker:london:croydon')
analyzer.ingest('skymaker:london:design')
analyzer.ingest('skymaker:man:pm')
analyzer.ingest('skymaker:man:pm')

print(analyzer.appearance('skymaker:man'))  # Output: 0.2


#Space complexity: O(n)
#Time complexity: O(n) for the appearance function, O(1) for the ingest function.