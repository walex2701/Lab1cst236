
Source2 provides functions for describing a quadrilateral.

Determining Quadrilateral Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_quadrilateral_type` provides users with a way to provide a set of four sides
of a quadrilateral and returns the type of quadrilateral ("rectangle", "square" or "invalid")

>>> from source.source2 import get_quadrilateral_type

Square
^^^^^^^

>>> test_get_quadrilateral_type(length, length, length, length)
'square'

Rectangle
^^^^^^^^^^

>>> test_get_quadrilateral_type(length, width, length, width)
'rectangle'

>>> test_get_quadrilateral_type(length,length, length, width)
'invalid'


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: