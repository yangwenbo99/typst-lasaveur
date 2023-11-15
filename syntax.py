from bs4 import BeautifulSoup
from gen import *

SUBSCRIPT_LETTERS = '0123456789+-=()aeoxhklmnpst'
SUBSCRIPT_JOINEDS = '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜ'
SUPERSCRIPT_LETTERS = '0123456789+-=()ni'
SUPERSCRIPT_JOINEDS = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ'
# CAL_LETTERS = '𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵'
CAL_LETTERS = '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'
LETTERS     = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BB_LETTERS         = '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡'
LETTERS_AND_DIGITS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# also need fb and bold

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--function-prefix', dest='function_prefix', default="f")
    parser.add_argument('--font_function-prefix', dest='font_function_prefix', default="f")
    parser.add_argument('--arrow-prefix', dest='arrow_prefix', default="ar")
    parser.add_argument('--magic-character', dest='magic_character', default="g")
    parser.add_argument('--greek-prefix', dest='greek_prefix', default="k")
    return parser.parse_args()

def print_one_line(k: str, v: str):
    k = k.replace('*', '\\*')
    k = k.replace('\'', '\\\\\'')
    k = k.replace('~', '\\~')
    k = k.replace('[', '\\[')
    k = k.replace(']', '\\]')
    k = k.replace('.', '\\.')
    if "'" in v or "'" in k:
        print(f"    \\ [\"{k}\", \"{v}\"],")
    else:
        print(f"    \\ ['{k}', '{v}'],")

def main(args: argparse.Namespace):
    SHORT_SYMBOLS = {}
    for k, v in FUNCTIONS.items(): 
        SHORT_SYMBOLS[args.function_prefix + k] = v
    for k, v in FONT_FUNCTIONS.items(): 
        SHORT_SYMBOLS[args.font_function_prefix + k] = v
    for k, v in MAGICS.items(): 
        SHORT_SYMBOLS[args.magic_character + k] = v
    for k, v in GREEKS.items(): 
        SHORT_SYMBOLS[args.greek_prefix + k] = v
    for k, v in ARROWS.items(): 
        SHORT_SYMBOLS[args.arrow_prefix + k] = v
    for k, v in COMPATIBILITY.items(): 
        SHORT_SYMBOLS[k] = v

    # symbol/sym
    with open('symbols.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    buttons = soup.select('.symbol-grid > li > button')
    symbols = {}

    for button in buttons:
        key = button.find('code').text.strip()
        value = button.find('span').text.strip()
        symbols[key] = value

    print("let s:typstMathList=[")
    for k, v in symbols.items():
        if len(v) > 1: continue
        print_one_line(k, v)
    for k, kk in SHORT_SYMBOLS.items():
        if kk in symbols:
            v = symbols[kk]
            if len(v) > 1: continue
            print_one_line(k, v)
    print('\\ ]')
    print("""
    for typmath in s:typstMathList
        exe "syn match typstMathSymbol '\\\\a\\\\@<!".typmath[0]."\\\\a\\\\@!' contained conceal cchar=".typmath[1]
    endfor
          """)

    # symbol
    with open('symbols_0.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    symbol_grids = soup.select('.symbol-grid')
    buttons = symbol_grids[1].select('li > button')
    symbols = {}

    for button in buttons:
        key = button.find('code').text.strip()
        value = button.find('span').text.strip()
        symbols[key] = value

    print("let s:typstMathList2=[")
    for k, v in symbols.items():
        if len(v) > 1: continue
        print_one_line(k, v)
    print('\\ ]')
    print("""
    for typmath in s:typstMathList2
        exe "syn match typstMathSymbol '".typmath[0]."' contained conceal cchar=".typmath[1]
    endfor
          """)


    # Fonts
    print("let s:typstCalList=[")
    for k, v in zip(LETTERS, CAL_LETTERS):
        print_one_line(k, v)
    print('\\ ]')
    print("""
    for typmath in s:typstCalList
        exe "syn match typstMathSymbol '\\\\a\\\\@<!cal(".typmath[0].")' contained conceal cchar=".typmath[1]
        exe "syn match typstMathSymbol '\\\\a\\\\@<!fca(".typmath[0].")' contained conceal cchar=".typmath[1]
    endfor
          """)

    print("let s:typstBBList=[")
    for k, v in zip(LETTERS_AND_DIGITS, BB_LETTERS):
        print_one_line(k, v)
    print('\\ ]')
    print("""
    for typmath in s:typstBBList
        exe "syn match typstMathSymbol '\\\\a\\\\@<!bb(".typmath[0].")' contained conceal cchar=".typmath[1]
        exe "syn match typstMathSymbol '\\\\a\\\\@<!fbb(".typmath[0].")' contained conceal cchar=".typmath[1]
    endfor
          """)

    print("""
syntax region typstMathBold
    \ matchgroup=typstMathFunction start=/\<fb(/ end=/)/
    \ contains=@typstMath
    \ contained concealends

syntax region typstMathBold
    \ matchgroup=typstMathFunction start=/\<bold(/ end=/)/
    \ contains=@typstMath
    \ contained concealends
    
highlight default link typstMathBold         typstMarkupBold
    """)

    # Simple super/subscripts
    print("let s:typstSubList=[")
    for k, v in zip(SUBSCRIPT_LETTERS, SUBSCRIPT_JOINEDS):
        if k in '()':  # Temp workaround
            continue
        print_one_line(k, v)
    print('\\ ]')
    # print("""
    # for typmath in s:typstSubList
        # exe "syn match typstMathScripts '\\\\(\\\\w\\\\|)\\\\)\\\\@<=_".typmath[0]."\\\\>' contained conceal cchar=".typmath[1]
    # endfor
          # """)
    print("let s:typstSupList=[")
    for k, v in zip(SUPERSCRIPT_LETTERS, SUPERSCRIPT_JOINEDS):
        if k in '()':   # Temp workaround
            continue
        print_one_line(k, v)
    print('\\ ]')
    # print("""
    # for typmath in s:typstSupList
        # exe "syn match typstMathScripts '\\\\(\\\\w\\\\|)\\\\)\\\\@<=\\\\^".typmath[0]."\\\\>' contained conceal cchar=".typmath[1]
    # endfor
          # """)
    with open('syntax.vim', 'r') as f:
        print(f.read())



if __name__ == '__main__':
    args = parse_args()
    main(args)
