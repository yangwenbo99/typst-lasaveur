import argparse

FUNCTIONS = {
        'h': 'hat',
        't': 'tilde',
        '2': 'sqrt',
        }
FONT_FUNCTIONS = {
        'b': 'bold',
        'bb': 'bb',
        'ca': 'cal',
        }
MAGICS = {
        '6': 'diff',
        '8': 'infinity',
        '0': 'nothing', 
        'o': 'circle.stroked.tiny', 
        '_': 'without', 
        'd': 'dot.op', 
        't': 'times', 
        'U': 'union.big', 
        'I': 'sect.big', 
        'b': 'subset', 
        'beq': 'subset.eq', 
        'bne': 'subset.neq', 
        'bneq': 'subset.neq', 
        'p': 'supset', 
        'peq': 'supset.eq', 
        'pne': 'supset.neq', 
        'pneq': 'supset.neq', 
        'al': 'angle.l', 
        'ar': 'angle.r', 
        'V': 'nabla', 
        'd': 'dot',
        'dd': 'dot.double',
        'ddd': 'dot.triple',
        'dddd': 'dot.quad',
        '1': 'tilde.op',
        }
GREEKS = {
        'a': 'alpha',
        'b': 'beta',
        'c': 'chi',
        'd': 'delta',
        'e': 'epsilon.alt',
        'ee': 'epsilon',
        'f': 'phi.alt',
        'ff': 'phi',
        'g': 'gamma',
        'h': 'eta',
        'i': 'iota',
        'k': 'kappa',
        'l': 'lambda',
        'm': 'mu',
        'n': 'nu',
        'o': 'omicron',
        'p': 'pi',
        'q': 'theta',
        'r': 'rho',
        's': 'sigma',
        't': 'tau',
        'u': 'upsilon',
        'v': 'sigma.alt',
        'w': 'omega',
        'x': 'xi',
        'y': 'psi',
        'z': 'zeta',
        'D': 'Delta',
        'G': 'Gamma',
        'L': 'Lambda',
        'X': 'Xi',
        'S': 'Sigma',
        'U': 'Upsilon',
        'F': 'Phi',
        'y': 'psi',
        'W': 'Omega',
        }
COMPATIBILITY = {
        'partial': 'diff',
        'infty': 'infinity',
        'circ': 'circle.stroked.tiny',
        'setminus': 'without',
        'cdot': 'dot.op',
        'bigcup': 'union.big',
        'bigcap': 'sect.big',
        'prod': 'product',
        'to': 'arrow.r',
        'implies': 'arrow.r.double',
        'gets': 'arrow.l',
        'iff': 'arrow.l.r.double.long',
        'cdots': 'dots.h.c',
        'vdots': 'dots.v',
        'ddots': 'dots.down',
        'int': 'integral',
        'iint': 'integral.double',
        'iiint': 'integral.triple',
        'oint': 'integral.cont',
        'sim': 'tilde.op',
        'ne': 'eq.not',
        }
ARROWS = {
        'l': 'l',
        'r': 'r',
        't': 't',
        'b': 'b',
        'lr': 'l.r',
        'll': 'l.long',
        'lr': 'r.long',
        'llr': 'l.r.long',
        'dl': 'l.double',
        'dr': 'r.double',
        'dlr': 'l.r.double',
        'dt': 't.double',
        'db': 'b.double',
        'ldl': 'l.long.double',
        'ldr': 'r.long.double',
        'ldlr': 'l.r.long.double',
        }

# bf, rm, sf, tt, it, fr, ca, sc, bb
# greek

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--function-prefix', dest='function_prefix', default="f")
    parser.add_argument('--font_function-prefix', dest='font_function_prefix', default="f")
    parser.add_argument('--arrow-prefix', dest='arrow_prefix', default="ar")
    parser.add_argument('--magic-character', dest='magic_character', default="g")
    parser.add_argument('--greek-prefix', dest='greek_prefix', default="k")
    return parser.parse_args()

def main(args: argparse.Namespace):
    for k, v in FUNCTIONS.items(): 
        print_symbol_def(args.function_prefix + k + '(a)', v + '(#a)')
    for k, v in FONT_FUNCTIONS.items(): 
        print_symbol_def(args.font_function_prefix + k + '(a)', v + '(#a)')
    for k, v in MAGICS.items(): 
        print_symbol_def(args.magic_character + k, v)
    for k, v in GREEKS.items(): 
        print_symbol_def(args.greek_prefix + k, v)
    for k, v in COMPATIBILITY.items(): 
        print_symbol_def(k, v)
    translate_dict(ARROWS, args.arrow_prefix, 'arrow.')


def print_symbol_def(new: str, existing: str):
    print(f'#let {new} = ${existing}$')

def translate_dict(d: dict, dict_name: str, existing_prefix: str):
    print(f'#let {dict_name} = (')
    for k, v in d.items():
        print(f'\t{k}: ${existing_prefix}{v}$,')
    print(f')')

if __name__ == '__main__':
    args = parse_args()
    main(args)


