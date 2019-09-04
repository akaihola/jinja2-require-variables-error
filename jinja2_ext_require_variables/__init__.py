#!/usr/bin/python3

from jinja2 import nodes, contextfunction, UndefinedError
from jinja2.ext import Extension


class RequireExtension(Extension):
    """Jinja2 extension implementing the ``{% require <varname> ... %}`` tag

    Example::

        {% require MYVAR1 MYVAR2 %}

    If any of the listed variable names is not found in the template rendering
    context, an exception will be raised::

        jinja2.exceptions.UndefinedError: Required context variables are missing when rendering the template:
        - MYVAR1
        - MYVAR2

    """
    tags = {'require'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        variable_names = []
        while parser.stream.current.type != 'block_end':
            variable_names.append(next(parser.stream))

        node = nodes.CallBlock(
            self.call_method('_require',
                             [nodes.List([nodes.Const(token.value)
                                          for token in variable_names])]),
            [], [], []).set_lineno(lineno)
        return parser.parse_import_context(node, True)

    @contextfunction
    def _require(self, context, required_variables, caller):
        missing = [arg for arg in required_variables if arg not in context]
        if missing:
            missing_msg = '\n'.join('- {}'.format(arg) for arg in missing)
            raise UndefinedError('Required context variables are missing when '
                                 'rendering the template:\n'
                                 '{}'.format(missing_msg))
        return ''
