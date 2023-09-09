def fun(s):
    try:
        a = s.index('@')
        b = s.index('.')
    except:
        return False
    else:
        if a > b:
            return False
        else:
            name = s[:a]
            site = s[a+1:b]
            ext = s[b+1:]
            
            if not name or not site or not ext:
                return False
            
            if len(ext) >3 or len(ext) < 1:
                return False
            
            for symbol in name:
                if symbol.isalnum() or symbol in ['-', '_']:
                    continue
                else:
                    return False
            for symbol in site:
                if not symbol.isalnum():
                    return False
            for symbol in ext:
                if not symbol.isalpha():
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