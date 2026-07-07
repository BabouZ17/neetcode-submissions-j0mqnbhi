class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            if self.isValidEmail(email):
                res.add(self.cleanEmail(email))
        print(res)
        return len(res)

    def isValidEmail(self, email: str) -> bool:
        return "@" in email

    def cleanEmail(self, email: str) -> str:
        local_name, domain_name = email.split("@")
        local_name = local_name.replace(".", "").split("+")[0]
        return f"{local_name}@{domain_name}"