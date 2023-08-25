from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        while len(version.split('.')) != 3:
            version += '.0'
        self.version = version

    def __str__(self):
        return self.version

    def __repr__(self):
        return f"Version('{self.version}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            v1, v2, v3 = map(int, self.version.split('.'))
            vv1, vv2, vv3 = map(int, other.version.split('.'))
            return (v1, v2, v3) > (vv1, vv2, vv3)
        return NotImplemented


version = Version('12')
not_supported = ['12.0.0', 12.0, (12, 0), {12: 0}, True, False]

for obj in not_supported:
    print(obj == version)
