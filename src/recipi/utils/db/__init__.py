# -*- coding: utf-8 -*-


def sane_repr(*attrs):
    if 'id' not in attrs and 'pk' not in attrs:
        attrs = ('id',) + attrs

    def _repr(self):
        cls = type(self).__name__

        pairs = (
            '%s=%s' % (a, repr(getattr(self, a, None)))
            for a in attrs)

        return '<%s at 0x%x: %s>' % (cls, id(self), ', '.join(pairs))

    return _repr


def sane_str(*attrs):
    def _str(self):
        return '; '.join(str(getattr(self, attr, '-')) for attr in attrs)
    return _str
