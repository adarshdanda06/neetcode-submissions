class Solution:
    def simplifyPath(self, path: str) -> str:
        pathSplit = path.split('/')
        finPath = []
        for item in pathSplit:
            if item == "." or item == "":
                continue
            
            elif item == "..":
                if finPath:
                    finPath.pop()

            else:
                finPath.append(item)

        return '/' + '/'.join(finPath)