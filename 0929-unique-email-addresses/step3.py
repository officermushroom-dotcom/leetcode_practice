class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        canonicalized_emails = set()
        for email in emails:
            local, domain = email.split('@')
            canonicalized_local = local.split('+')[0].replace('.', '')
            canonicalized_emails.add(canonicalized_local + '@' + domain)
        return len(canonicalized_emails)
