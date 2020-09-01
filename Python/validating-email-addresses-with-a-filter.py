from re import match


def fun(s):
    if not match(r'[^@]+@[^@]+\.[^@]+', s):
        return False
    if not match("^[A-Za-z0-9_-]*$", s.split('@')[0]):
        return False
    if not match("^[A-Za-z0-9]*$", s.split('@')[1].split('.')[0]):
        return False
    if not len(s.split('.')[1]) < 4:
        return False
    return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
