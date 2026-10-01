class Solution:
    def numDecodings(self, s: str) -> int:
        valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                '21', '22', '23', '24', '25', '26']
        memory = {}
        def recurse(newstr):
            if newstr in memory:
                return memory[newstr]
            if newstr[0] == '0':
                return 0
            if len(newstr) == 1:
                return 1
            if len(newstr) == 2 and newstr in valid and newstr[1] != '0':
                return 2
            elif len(newstr) == 2 and newstr in valid:
                return 1
            if newstr[:2] in valid:
                memory[newstr] = recurse(newstr[1:]) + recurse(newstr[2:])
            else:
                memory[newstr] = recurse(newstr[1:])
            return memory[newstr]

        return recurse(s)
