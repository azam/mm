# lextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'DO': 1, 'REMAINDER_ASSIGN': 1, 'RSHIFT': 1, 'SYNCHRONIZED': 1, 'GTEQ': 1, 'MINUS_ASSIGN': 1, 'OR_ASSIGN': 1, 'VOID': 1, 'STRING_LITERAL': 1, 'ABSTRACT': 1, 'CHAR': 1, 'LSHIFT_ASSIGN': 1, 'WHILE': 1, 'SHORT': 1, 'STATIC': 1, 'PRIVATE': 1, 'LSHIFT': 1, 'CONTINUE': 1, 'THROWS': 1, 'NULL': 1, 'TRUE': 1, 'BYTE': 1, 'NEQ': 1, 'CASE': 1, 'TIMES_ASSIGN': 1, 'THROW': 1, 'NEW': 1, 'SWITCH': 1, 'LONG': 1, 'FINAL': 1, 'PROTECTED': 1, 'STRICTFP': 1, 'IF': 1, 'NUM': 1, 'CATCH': 1, 'ELLIPSIS': 1, 'NATIVE': 1, 'CLASS': 1, 'BLOCK_COMMENT': 1, 'IMPLEMENTS': 1, 'TRANSIENT': 1, 'LINE_COMMENT': 1, 'FOR': 1, 'PACKAGE': 1, 'PLUSPLUS': 1, 'AND_ASSIGN': 1, 'RRSHIFT_ASSIGN': 1, 'ENUM': 1, 'ELSE': 1, 'TRY': 1, 'FINALLY': 1, 'DIVIDE_ASSIGN': 1, 'PUBLIC': 1, 'MINUSMINUS': 1, 'EQ': 1, 'RRSHIFT': 1, 'AND': 1, 'ASSERT': 1, 'RETURN': 1, 'FALSE': 1, 'NAME': 1, 'XOR_ASSIGN': 1, 'THIS': 1, 'DOUBLE': 1, 'LTEQ': 1, 'RSHIFT_ASSIGN': 1, 'CHAR_LITERAL': 1, 'DEFAULT': 1, 'FLOAT': 1, 'BREAK': 1, 'INT': 1, 'BOOLEAN': 1, 'VOLATILE': 1, 'IMPORT': 1, 'PLUS_ASSIGN': 1, 'INTERFACE': 1, 'EXTENDS': 1, 'INSTANCEOF': 1, 'SUPER': 1, 'OR': 1}
_lexreflags   = 0
_lexliterals  = '()+-*/=?:,.^|&~!=[]{};<>@%'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_LINE_COMMENT>//.*?\\n)|(?P<t_BLOCK_COMMENT>/\\*(.|\\n)*?\\*/)|(?P<t_NAME>[A-Za-z_$][A-Za-z0-9_$]*)|(?P<t_newline>\\n+)|(?P<t_newline2>(\\r\\n)+)|(?P<t_NUM>\\.?[0-9][0-9eE_lLdDa-fA-F.xXpP]*)|(?P<t_STRING_LITERAL>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_CHAR_LITERAL>\\\'([^\\\\\\n]|(\\\\.))*?\\\')|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_MINUSMINUS>\\-\\-)|(?P<t_OR>\\|\\|)|(?P<t_RRSHIFT_ASSIGN>>>>=)|(?P<t_XOR_ASSIGN>\\^=)|(?P<t_RSHIFT_ASSIGN>>>=)|(?P<t_LSHIFT_ASSIGN><<=)|(?P<t_OR_ASSIGN>\\|=)|(?P<t_PLUS_ASSIGN>\\+=)|(?P<t_RRSHIFT>>>>)|(?P<t_TIMES_ASSIGN>\\*=)|(?P<t_LTEQ><=)|(?P<t_RSHIFT>>>)|(?P<t_AND_ASSIGN>&=)|(?P<t_DIVIDE_ASSIGN>/=)|(?P<t_GTEQ>>=)|(?P<t_MINUS_ASSIGN>-=)|(?P<t_EQ>==)|(?P<t_AND>&&)|(?P<t_REMAINDER_ASSIGN>%=)|(?P<t_NEQ>!=)|(?P<t_LSHIFT><<)', [None, ('t_LINE_COMMENT', 'LINE_COMMENT'), ('t_BLOCK_COMMENT', 'BLOCK_COMMENT'), None, ('t_NAME', 'NAME'), ('t_newline', 'newline'), ('t_newline2', 'newline2'), None, (None, 'NUM'), (None, 'STRING_LITERAL'), None, None, (None, 'CHAR_LITERAL'), None, None, (None, 'ELLIPSIS'), (None, 'PLUSPLUS'), (None, 'MINUSMINUS'), (None, 'OR'), (None, 'RRSHIFT_ASSIGN'), (None, 'XOR_ASSIGN'), (None, 'RSHIFT_ASSIGN'), (None, 'LSHIFT_ASSIGN'), (None, 'OR_ASSIGN'), (None, 'PLUS_ASSIGN'), (None, 'RRSHIFT'), (None, 'TIMES_ASSIGN'), (None, 'LTEQ'), (None, 'RSHIFT'), (None, 'AND_ASSIGN'), (None, 'DIVIDE_ASSIGN'), (None, 'GTEQ'), (None, 'MINUS_ASSIGN'), (None, 'EQ'), (None, 'AND'), (None, 'REMAINDER_ASSIGN'), (None, 'NEQ'), (None, 'LSHIFT')])]}
_lexstateignore = {'INITIAL': ' \t\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
