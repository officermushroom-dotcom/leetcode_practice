import string


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        result = set()
        for email in emails:
            modified_email= ""
            for cha in email:
                if cha in string.ascii_lowercase:
                    modified_email += cha
                elif cha == '.':
                    continue
                else:
                    break
            for i, cha in enumerate(email):
                if cha == '@':
                    at_index = i
            modified_email += '@'
            modified_email += email[at_index + 1:]
            result.add(modified_email)
        return len(result)
    