from pymonad.tools import curry

# from pymonad import Compose
from pymonad.reader import Compose


# 3.1
@curry(2)
def tag(tag_symbol, string):
    return f"<{tag_symbol}>{string}</{tag_symbol}>"


assert tag("b", "string") == "<b>string</b>"

bold = tag("b")
assert bold("string") == "<b>string</b>"

italic = tag("i")
assert italic("string") == "<i>string</i>"


# 3.2
@curry(2)
def add_atr(atr, string_with_tag):
    i = string_with_tag.find(">")
    atributes = " " + " ".join(f'{k}="{v}"' for k, v in atr.items())
    return string_with_tag[:i] + atributes + string_with_tag[i:]


tag_with_atr = Compose(tag("li")).then(add_atr({"class": "list-group"}))
assert tag_with_atr("item 23") == '<li class="list-group">item 23</li>'
