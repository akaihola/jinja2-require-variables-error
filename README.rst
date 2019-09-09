============================================================
 Error on Undefined Required Variables Extension for Jinja2
============================================================

A custom Jinja tag ``require``:
raise an error if any of the listed variables is undefined
in the template context.


How to install
==============

For Flask::

    app.jinja_env.add_extension('jinja2_ext_require_variables_error.RequireExtension')

For standalone Jinja2::

    jinja_env = Environment(extensions=['jinja2_ext_require_variables_error.RequireExtension'])

Background
==========

If an undefined variable is used e.g. in a function call,
the exception doesn't mention the name of the variable.
This is a problem when debugging complex templates::

    {{ my_function(my_variable) }}

This custom tag extension allows the template author
to specify which variables must not be undefined.
If such a case, a more descriptive exception is raised.

Example
=======

Single variable::

    {% require MY_VARIABLE %}

Multiple variables::

    {% require MY_VARIABLE MY_SECOND_VARIABLE %}
