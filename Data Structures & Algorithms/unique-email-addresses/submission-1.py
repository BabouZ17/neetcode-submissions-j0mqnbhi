class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            normalized_email, valid = self._normalize_email(email)
            if valid:
                unique_emails.add(normalized_email)
        return len(unique_emails)

    def _normalize_email(self, email: str) -> tuple[str, bool]:
        if len(email.split("@")) != 2:
            return "", False

        local_name, domain_name = email.split("@")
        local_name = local_name.replace(".", "").split("+")[0]


        return f"{local_name}@{domain_name}", True