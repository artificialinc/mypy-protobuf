"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import testproto.test3_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Inner(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    A_FIELD_NUMBER: builtins.int
    a: testproto.test3_pb2.OuterEnum.ValueType
    def __init__(
        self,
        *,
        a: testproto.test3_pb2.OuterEnum.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["a", b"a"]) -> None: ...

Global___Inner: typing_extensions.TypeAlias = Inner
