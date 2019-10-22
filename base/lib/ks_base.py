"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""


def switch(key, scope, default="Default", prefix="case"):
    try:
        method = getattr(scope, str(prefix) + str(key))
    except Exception:
        try:
            method = getattr(scope, str(prefix) +  str(default))
        except Exception:
            pass
    if type(method).__name__ == 'method':
        return method()
