Source2 provides functions for describing a quadrilateral.

Determining Quadrilateral Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_quadrilateral_type` provides users with a way to provide a set of four sides
of a quadrilateral and returns the type of quadrilateral ("rectangle", "square" or "invalid")

Square
^^^^^^^

>>> from source.source2 import get_quadrilateral_type
>>> get_quadrilateral_type(1, 1, 1, 1)
'square'

Rectangle
^^^^^^^^^^

>>> from source.source2 import get_quadrilateral_type
>>> get_quadrilateral_type(2, 1, 2, 1)
'rectangle'

Invalid
^^^^^^^^

>>> from source.source2 import get_quadrilateral_type
>>> get_quadrilateral_type(1, 2, 1, 0)
'invalid'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: