" The following parts are hand-written
	" a_123, a_p
	syn match typstMathScripts /\(\w\|)\)\@<=_\([0-9]\+\|[+-=aeoxhklmnpst]\)\>/ contained
				\ contains=typstMathSimpleSubscripts
	syntax region typstMathSimpleSubscripts
		\ contained
		\ matchgroup=typstScriptSegs 
		\ start=/\(\w\|)\)\@<=_/ end=/\>/
		\ concealends contains=typstMathSubscript
    for typmath in s:typstSubList
        " exe "syn match typstMathSubscript '\\<".typmath[0]."\\>' contained conceal cchar=".typmath[1]
        exe "syn match typstMathSubscript '".typmath[0]."' contained conceal cchar=".typmath[1]
        " exe "syn match typstMathSymbol '\\a\\@<!bb(".typmath[0].")' contained conceal cchar=".typmath[1]
        " exe "syn match typstMathSubscript '\\a\\@!".typmath[0]."\\a\\@!' contained conceal cchar=".typmath[1]
    endfor

	" a_(123), a_(123 p)
	syn match typstMathScripts /\(\w\|)\)\@<=_(\<\([0-9]\+\>\|\<[+-=aeoxhklmnpst]\>\|\s\)\+)/ contained
				\ contains=typstMathCompoundSubscripts
        syntax region typstMathCompoundSubscripts
            \ contained
            \ matchgroup=typstScriptSegs 
            \ start=/\(\w\|)\)\@<=_(/ end=/)/
            \ concealends contains=typstMathCompoundSubscript
    for typmath in s:typstSubList
        " exe "syn match typstMathSubscript '\\<".typmath[0]."\\>' contained conceal cchar=".typmath[1]
        exe "syn match typstMathCompoundSubscript '".typmath[0]."' contained conceal cchar=".typmath[1]
        " exe "syn match typstMathSymbol '\\a\\@<!bb(".typmath[0].")' contained conceal cchar=".typmath[1]
        " exe "syn match typstMathSubscript '\\a\\@!".typmath[0]."\\a\\@!' contained conceal cchar=".typmath[1]
    endfor
          
	" a^123, a^n
	syn match typstMathScripts /\(\w\|)\)\@<=^\([0-9]\+\|[+-=ni]\)\>/ contained
				\ contains=typstMathSimpleSupscripts
	syntax region typstMathSimpleSupscripts
		\ contained
		\ matchgroup=typstScriptSegs 
		\ start=/\(\w\|)\)\@<=^/ end=/\>/
		\ concealends contains=typstMathSupscript
    for typmath in s:typstSupList
        exe "syn match typstMathSupscript '".typmath[0]."' contained conceal cchar=".typmath[1]
    endfor

	" a^(123), a^(123 n)
	syn match typstMathScripts /\(\w\|)\)\@<=^(\<\([0-9]\+\>\|\<[+-=ni]\>\|\s\)\+)/ contained
				\ contains=typstMathCompoundSupscripts
        syntax region typstMathCompoundSupscripts
            \ contained
            \ matchgroup=typstScriptSegs 
            \ start=/\(\w\|)\)\@<=^(/ end=/)/
            \ concealends contains=typstMathCompoundSupscript
    for typmath in s:typstSupList
        exe "syn match typstMathCompoundSupscript '".typmath[0]."' contained conceal cchar=".typmath[1]
    endfor
          
	highlight default typstScriptSegs                    ctermfg=Green guifg=Green
	highlight default link typstMathScriptNum              typstMathNumber
	highlight default link typstMathSubscript              typstMathScriptNum
	highlight default link typstMathCompoundSubscript              typstMathScriptNum

