s="Hello"
news=""
def reverse_string(i,s,news):
    if(i==len(s)):
        return news
    news=reverse_string(i+1,s,news)
    return news+s[i]
news=reverse_string(0,s,news)
print(news)

