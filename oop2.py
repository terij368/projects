"""
Self-closing cookie jar


When you were little, your mother used to make the most delicious cookies, which you could not resist. So, every now and then, when your mother didn't see you, you sneaked into the kitchen, climbed onto a stool to reach the cookie jar, and stole a cookie or two. However, sometimes while doing this, you would hear foot steps approaching, so you quickly jumped down from the stool and, when your mother entered the kitchen, you pretended as if nothing had happened (whistle, whistle innocently). However, your mother knew. How did she know? You forgot to put the lid back on the cookie jar! Oh, no!

Growing older (and still not able to resist cookies), you devised a contraption that would automatically put the lid back on the cookie jar, no matter what would happen.

The class CookieJar is provided:

class CookieJar(object):

    def __init__(self):
        self._is_open = False

    def take(self):
        if not self._is_open:
            raise ValueError("Cookie jar is closed")
        return "Cookie"

    def open_jar(self):
        self._is_open = True

    def close_jar(self):
        self._is_open = False

    def is_open(self):
        return self._is_open

Your task is to implement the 'contraption' SelfClosing (class, method, whatever; it's your choice) such that, given an instancecookie_jar of CookieJar, you may call:


with SelfClosing(cookie_jar) as jar:
    cookie = jar.take()

after which, cookie_jar.is_open() == False, no matter what.


Do not alter the provided code.

Bon appétit!

"""

class CookieJar(object):

    def __init__(self):
        self._is_open = False

    def take(self):
        if not self._is_open:
            raise ValueError("Cookie jar is closed")
        return "Cookie"

    def open_jar(self):
        self._is_open = True

    def close_jar(self):
        self._is_open = False

    def is_open(self):
        return self._is_open
    
class SelfClosing:
    def __init__(self, cookie_jar):
        self.cookie_jar = cookie_jar

    def __enter__(self):
        self.cookie_jar.open_jar()
        return self.cookie_jar

    def __exit__(self, type, value, traceback):
        self.cookie_jar.close_jar()


cookie_jar = CookieJar()
print(cookie_jar.is_open()) # Should print: False
with SelfClosing(cookie_jar) as jar:
    cookie = jar.take()
    print(jar.is_open()) # Should print: False
print(cookie_jar.is_open()) # Should print: False
print(cookie) # Should print: Cookie



