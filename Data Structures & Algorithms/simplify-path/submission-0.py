class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for directory in path:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory and directory != ".":
                stack.append(directory)
        return "/" + "/".join(stack)