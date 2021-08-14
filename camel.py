"""Kebab case is a typographical convention that combines words by replacing each space with a dash (-), as follows:

Raw: magnificent flying penguins
Kebab case: magnificent-flying-penguins
This style is often used in URLs, for example, "www.foo.com/user-login-count".

Camel case combines words by replacing the first character with the upper case character, as follows:

Raw: magnificent flying penguins
Camel case: MagnificentFlyingPenguins
Camel Kebab case is a specialized convention that combines kebab and camel, as follows:

Raw: magnificent flying penguins
Camel Kebab case: magnificent-Flying-Penguins"""

a = "abc de$fg hij"

print(a.split())

def capitalize(a):
    ls = []
    for word in a.split()[1:len(a.split())]:
        ls.append(word.capitalize())
    return(a.split()[0] + "-" + "-".join(ls))



print(capitalize(a))
