class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def modify_email(email: str) -> str:
            modified_email = ''
            state = 'local'
            for cha in email:
                if state == 'local':
                    if cha == '.':
                        continue
                    elif cha == '@':
                        state = 'domain'
                        modified_email += cha
                    elif cha == '+':
                        state = 'after_plus'
                    else:
                        modified_email += cha
                elif state == 'after_plus':
                    if cha == '@':
                        state = 'domain'
                        modified_email += cha
                else:
                    modified_email += cha
            return modified_email

        modify_emails_set = set()
        for email in emails:
            modify_emails_set.add(modify_email(email))
        return len(modify_emails_set)
    

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        modifeid_emails = set()
        for email in emails:
            local, domain = email.split('@')
            modified_local = local.replace('.', '').split('+')[0]
            modifeid_emails.add(modified_local + '@' + domain)
        return len(modifeid_emails)
