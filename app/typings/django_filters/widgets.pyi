"""
This type stub file was generated by pyright.
"""

from django import forms

class LinkWidget(forms.Widget):
    def __init__(self, attrs=..., choices=...) -> None: ...
    def value_from_datadict(self, data, files, name): ...
    def render(self, name, value, attrs=..., choices=..., renderer=...): ...
    def render_options(self, choices, selected_choices, name): ...
    def render_option(self, name, selected_choices, option_value, option_label): ...
    def option_string(self): ...

class SuffixedMultiWidget(forms.MultiWidget):
    """
    A MultiWidget that allows users to provide custom suffixes instead of indexes.

    - Suffixes must be unique.
    - There must be the same number of suffixes as fields.
    """

    suffixes = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def suffixed(self, name, suffix): ...
    def get_context(self, name, value, attrs): ...
    def value_from_datadict(self, data, files, name): ...
    def value_omitted_from_data(self, data, files, name): ...
    def replace_name(self, output, index): ...
    def decompress(self, value): ...

class RangeWidget(SuffixedMultiWidget):
    template_name = ...
    suffixes = ...
    def __init__(self, attrs=...) -> None: ...
    def decompress(self, value): ...

class DateRangeWidget(RangeWidget):
    suffixes = ...

class LookupChoiceWidget(SuffixedMultiWidget):
    suffixes = ...
    def decompress(self, value): ...

class BooleanWidget(forms.Select):
    """Convert true/false values into the internal Python True/False.
    This can be used for AJAX queries that pass true/false from JavaScript's
    internal types through.
    """

    def __init__(self, attrs=...) -> None: ...
    def render(self, name, value, attrs=..., renderer=...): ...
    def value_from_datadict(self, data, files, name): ...

class BaseCSVWidget(forms.Widget):
    surrogate = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def value_from_datadict(self, data, files, name): ...
    def render(self, name, value, attrs=..., renderer=...): ...

class CSVWidget(BaseCSVWidget, forms.TextInput):
    def __init__(self, *args, attrs=..., **kwargs) -> None: ...

class QueryArrayWidget(BaseCSVWidget, forms.TextInput):
    """
    Enables request query array notation that might be consumed by MultipleChoiceFilter

    1. Values can be provided as csv string:  ?foo=bar,baz
    2. Values can be provided as query array: ?foo[]=bar&foo[]=baz
    3. Values can be provided as query array: ?foo=bar&foo=baz

    Note: Duplicate and empty values are skipped from results
    """

    def value_from_datadict(self, data, files, name): ...