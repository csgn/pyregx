
# ^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$

""" Anchors

NAME                    SYMBOL       VALUE                FUNCTION
----------------------  ------------ -------------------  --------------------
start of string         ^            START_OF_STRING      sof()
end of string           $            END_OF_STRING        eof()
a [non]word boundary    [\b, \B]     [NON_]WORD_BOUNDARY  bound(non=[0, 1])

"""


""" Meta Sequences
NAME                    SYMBOL       VALUE                FUNCTION
----------------------  ------------ -------------------  --------------------
any single character    .            ANY                  any()
alternate               |            OR                   or()
any [non]whitespace     [\s, \S]     [NON_]WS             space(non=[0, 1])           
any [non]digit          [\d, \D]     [NON_]DIGIT          digit(non=[0, 1])
any [non]word           [\w, \W]     [NON_]WORD           word(non=[0, 1])
backreference           \#           BACKREFERENCE        back_refer()
literal                 \            LITERAL              lit()
"""

""" Quantifiers
NAME                    SYMBOL       VALUE                FUNCTION
----------------------  ------------ -------------------  --------------------
zero or one of a        ?            ZERO_OR_ONE          zero_or_one()
zero or more of a       *            ZERO_OR_MORE         zero_or_more()
one or more of a        +            ONE_OR_MORE          one_or_more()
exactly x or a          {x}          EXACT                exact(x)
x or more of a          {x,}         EXACT_MORE           exact_more(x)
between x and y of a    {x,y}        EXACT_RANGE          exact_range(x, y)

"""

"""

START_OF_STRING
    ZERO_OR_ONE
    GROUP
        TEXT
            DIGIT
            EXACT_RANGE
        WS
    END
    ZERO_OR_ONE
        TEXT
            DIGIT
            EXACT_RANGE
    ZERO_OR_ONE
        TEXT
    CONTAIN_GROUP
        CONTAIN
            WS
            TEXT
            TEXT
    END
    DIGIT
        EXACT_RANGE
    CONTAIN_GROUP
        CONTAIN
            WS
            TEXT
            TEXT
    END
    DIGIT
        EXACT_RANGE
END_OF_STRING
"""

"""
(Pyregx()
    .sof()
    .zero_or_one.group()
        .text('+')
        .digit()
            .exact_range(1, 2)
        .space()
    .end()
    .zero_or_one.text('(')
        .digit()
        .exact(3)
    .zero_or_one.text(')')
    .contain_group()
        .contain.space()
        .contain.text('.')
        .contain.text('-')
    .end()
    .digit()
        .exact(3)
    .contain_group()
        .contain.space()
        .contain.text('.')
        .contain.text('-')
    .end()
    .digit()
        .exact_range(4)
    .eof()
)
"""


if __name__ == '__main__':
    pass
