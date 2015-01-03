# -*- coding: utf-8 -*-
"""
     pygments.styles.snemo
     ~~~~~~~~~~~~~~~~~~~~~~~

     A style for SuperNEMO software code
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
    Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class SNEMOStyle(Style):
    """
     A style for SuperNEMO software code

    """

    background_color = "#ffffff"
    highlight_color  = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                   "#252525"            , # class:  ''
        Whitespace:             ""                   , # class: 'w'
        Error:                  ""                   , # class: 'err'
        Other:                  ""                   , # class 'x'

        Comment:                "#888a85"            , # class: 'c'
        Comment.Multiline:      ""                   , # class: 'cm'
        Comment.Preproc:        "#C08040"            , # class: 'cp'
        Comment.Single:         ""                   , # class: 'c1'
        Comment.Special:        ""                   , # class: 'cs'

        Keyword:                "#003399"            , # class: 'k'
        Keyword.Constant:       ""                   , # class: 'kc'
        Keyword.Declaration:    ""                   , # class: 'kd'
        Keyword.Namespace:      "#f92672"            , # class: 'kn'
        Keyword.Pseudo:         ""                   , # class: 'kp'
        Keyword.Reserved:       ""                   , # class: 'kr'
        Keyword.Type:           ""                   , # class: 'kt'

        Operator:               "#252525"            , # class: 'o'
        Operator.Word:          ""                   , # class: 'ow' - like keywords

        Punctuation:            "#003399"            , # class: 'p'

        Name:                   "#252525"            , # class: 'n'
        Name.Attribute:         ""                   , # class: 'na' - to be revised
        Name.Builtin:           ""                   , # class: 'nb'
        Name.Builtin.Pseudo:    ""                   , # class: 'bp'
        Name.Class:             ""                   , # class: 'nc' - to be revised
        Name.Constant:          "#4066B3"            , # class: 'no' - to be revised
        Name.Decorator:         ""                   , # class: 'nd' - to be revised
        Name.Entity:            ""                   , # class: 'ni'
        Name.Exception:         ""                   , # class: 'ne'
        Name.Function:          "#4066B3"            , # class: 'nf'
        Name.Property:          ""                   , # class: 'py'
        Name.Label:             ""                   , # class: 'nl'
        Name.Namespace:         ""                   , # class: 'nn' - to be revised
        Name.Other:             ""                   , # class: 'nx'
        Name.Tag:               "#f92672"            , # class: 'nt' - like a keyword
        Name.Variable:          ""                   , # class: 'nv' - to be revised
        Name.Variable.Class:    ""                   , # class: 'vc' - to be revised
        Name.Variable.Global:   ""                   , # class: 'vg' - to be revised
        Name.Variable.Instance: ""                   , # class: 'vi' - to be revised

        Number:                 "#4066B3"            , # class: 'm'
        Number.Float:           ""                   , # class: 'mf'
        Number.Hex:             ""                   , # class: 'mh'
        Number.Integer:         ""                   , # class: 'mi'
        Number.Integer.Long:    ""                   , # class: 'il'
        Number.Oct:             ""                   , # class: 'mo'

        Literal:                "#252525"            , # class: 'l'
        Literal.Date:           "#e6db74"            , # class: 'ld'

        String:                 "#4066B3"            , # class: 's'
        String.Backtick:        ""                   , # class: 'sb'
        String.Char:            ""                   , # class: 'sc'
        String.Doc:             ""                   , # class: 'sd' - like a comment
        String.Double:          ""                   , # class: 's2'
        String.Escape:          "#252525"            , # class: 'se'
        String.Heredoc:         ""                   , # class: 'sh'
        String.Interpol:        ""                   , # class: 'si'
        String.Other:           ""                   , # class: 'sx'
        String.Regex:           ""                   , # class: 'sr'
        String.Single:          ""                   , # class: 's1'
        String.Symbol:          ""                   , # class: 'ss'

        Generic:                ""                   , # class: 'g'
        Generic.Deleted:        ""                   , # class: 'gd',
        Generic.Emph:           "italic"             , # class: 'ge'
        Generic.Error:          ""                   , # class: 'gr'
        Generic.Heading:        ""                   , # class: 'gh'
        Generic.Inserted:       ""                   , # class: 'gi'
        Generic.Output:         ""                   , # class: 'go'
        Generic.Prompt:         ""                   , # class: 'gp'
        Generic.Strong:         "bold"               , # class: 'gs'
        Generic.Subheading:     ""                   , # class: 'gu'
        Generic.Traceback:      ""                   , # class: 'gt'
    }
