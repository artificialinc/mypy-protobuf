"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import builtins
import concurrent.futures
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import google.protobuf.service
import test.test_generated_mypy
import testproto.inner.inner_pb2
import testproto.nested.nested_pb2
import testproto.nopackage_pb2
import testproto.test3_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OuterEnum(_OuterEnum, metaclass=_OuterEnumEnumTypeWrapper):
    r"""Outer Enum"""
    pass
class _OuterEnum:
    V = typing.NewType('V', builtins.int)
class _OuterEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OuterEnum.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    FOO = OuterEnum.V(1)
    r"""FOO"""

    BAR = OuterEnum.V(2)
    r"""BAR"""


FOO = OuterEnum.V(1)
r"""FOO"""

BAR = OuterEnum.V(2)
r"""BAR"""

global___OuterEnum = OuterEnum


class NamingConflicts(_NamingConflicts, metaclass=_NamingConflictsEnumTypeWrapper):
    r"""Naming conflicts!"""
    pass
class _NamingConflicts:
    V = typing.NewType('V', builtins.int)
class _NamingConflictsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NamingConflicts.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...

Name = NamingConflicts.V(1)
Value = NamingConflicts.V(2)
keys = NamingConflicts.V(3)
values = NamingConflicts.V(4)
items = NamingConflicts.V(5)
r"""See https://github.com/protocolbuffers/protobuf/issues/8803
proto itself generates broken code when DESCRIPTOR is there
DESCRIPTOR = 8;
"""

global___NamingConflicts = NamingConflicts


class Simple1(google.protobuf.message.Message):
    r"""Message with one of everything"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class InnerEnum(_InnerEnum, metaclass=_InnerEnumEnumTypeWrapper):
        r"""Inner Enum"""
        pass
    class _InnerEnum:
        V = typing.NewType('V', builtins.int)
    class _InnerEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_InnerEnum.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INNER1 = Simple1.InnerEnum.V(1)
        r"""INNER1"""

        INNER2 = Simple1.InnerEnum.V(2)
        r"""INNER2"""


    INNER1 = Simple1.InnerEnum.V(1)
    r"""INNER1"""

    INNER2 = Simple1.InnerEnum.V(2)
    r"""INNER2"""


    class InnerMessage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    class EmailByUidEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Optional[builtins.int] = ...,
            value : typing.Optional[typing.Text] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    A_STRING_FIELD_NUMBER: builtins.int
    A_REPEATED_STRING_FIELD_NUMBER: builtins.int
    A_BOOLEAN_FIELD_NUMBER: builtins.int
    A_UINT32_FIELD_NUMBER: builtins.int
    A_ENUM_FIELD_NUMBER: builtins.int
    A_EXTERNAL_ENUM_FIELD_NUMBER: builtins.int
    A_INNER_FIELD_NUMBER: builtins.int
    A_NESTED_FIELD_NUMBER: builtins.int
    INNER_ENUM_FIELD_NUMBER: builtins.int
    REP_INNER_ENUM_FIELD_NUMBER: builtins.int
    INNER_MESSAGE_FIELD_NUMBER: builtins.int
    REP_INNER_MESSAGE_FIELD_NUMBER: builtins.int
    NO_PACKAGE_FIELD_NUMBER: builtins.int
    NESTED_ENUM_FIELD_NUMBER: builtins.int
    NESTED_MESSAGE_FIELD_NUMBER: builtins.int
    A_ONEOF_1_FIELD_NUMBER: builtins.int
    A_ONEOF_2_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_IN_ONEOF_FIELD_NUMBER: builtins.int
    OUTER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    INNER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    EMAIL_BY_UID_FIELD_NUMBER: builtins.int
    a_string: typing.Text = ...
    @property
    def a_repeated_string(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    a_boolean: builtins.bool = ...
    a_uint32: builtins.int = ...
    a_enum: global___OuterEnum.V = ...
    a_external_enum: testproto.test3_pb2.OuterEnum.V = ...
    @property
    def a_inner(self) -> testproto.inner.inner_pb2.Inner: ...
    @property
    def a_nested(self) -> testproto.nested.nested_pb2.Nested: ...
    inner_enum: global___Simple1.InnerEnum.V = ...
    @property
    def rep_inner_enum(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Simple1.InnerEnum.V]: ...
    @property
    def inner_message(self) -> global___Simple1.InnerMessage: ...
    @property
    def rep_inner_message(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Simple1.InnerMessage]: ...
    @property
    def no_package(self) -> testproto.nopackage_pb2.NoPackage: ...
    nested_enum: testproto.nested.nested_pb2.AnotherNested.NestedEnum.V = ...
    @property
    def nested_message(self) -> testproto.nested.nested_pb2.AnotherNested.NestedMessage: ...
    a_oneof_1: typing.Text = ...
    a_oneof_2: typing.Text = ...
    @property
    def outer_message_in_oneof(self) -> global___Simple2: ...
    outer_enum_in_oneof: global___OuterEnum.V = ...
    inner_enum_in_oneof: global___Simple1.InnerEnum.V = ...
    user_id: test.test_generated_mypy.UserId = ...
    email: test.test_generated_mypy.Email = ...
    @property
    def email_by_uid(self) -> google.protobuf.internal.containers.ScalarMap[test.test_generated_mypy.UserId, test.test_generated_mypy.Email]: ...
    def __init__(self,
        *,
        a_string : typing.Optional[typing.Text] = ...,
        a_repeated_string : typing.Optional[typing.Iterable[typing.Text]] = ...,
        a_boolean : typing.Optional[builtins.bool] = ...,
        a_uint32 : typing.Optional[builtins.int] = ...,
        a_enum : typing.Optional[global___OuterEnum.V] = ...,
        a_external_enum : typing.Optional[testproto.test3_pb2.OuterEnum.V] = ...,
        a_inner : typing.Optional[testproto.inner.inner_pb2.Inner] = ...,
        a_nested : typing.Optional[testproto.nested.nested_pb2.Nested] = ...,
        inner_enum : typing.Optional[global___Simple1.InnerEnum.V] = ...,
        rep_inner_enum : typing.Optional[typing.Iterable[global___Simple1.InnerEnum.V]] = ...,
        inner_message : typing.Optional[global___Simple1.InnerMessage] = ...,
        rep_inner_message : typing.Optional[typing.Iterable[global___Simple1.InnerMessage]] = ...,
        no_package : typing.Optional[testproto.nopackage_pb2.NoPackage] = ...,
        nested_enum : typing.Optional[testproto.nested.nested_pb2.AnotherNested.NestedEnum.V] = ...,
        nested_message : typing.Optional[testproto.nested.nested_pb2.AnotherNested.NestedMessage] = ...,
        a_oneof_1 : typing.Optional[typing.Text] = ...,
        a_oneof_2 : typing.Optional[typing.Text] = ...,
        outer_message_in_oneof : typing.Optional[global___Simple2] = ...,
        outer_enum_in_oneof : typing.Optional[global___OuterEnum.V] = ...,
        inner_enum_in_oneof : typing.Optional[global___Simple1.InnerEnum.V] = ...,
        user_id : typing.Optional[test.test_generated_mypy.UserId] = ...,
        email : typing.Optional[test.test_generated_mypy.Email] = ...,
        email_by_uid : typing.Optional[typing.Mapping[test.test_generated_mypy.UserId, test.test_generated_mypy.Email]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["a_boolean",b"a_boolean","a_enum",b"a_enum","a_external_enum",b"a_external_enum","a_inner",b"a_inner","a_nested",b"a_nested","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_string",b"a_string","a_uint32",b"a_uint32","email",b"email","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","inner_message",b"inner_message","nested_enum",b"nested_enum","nested_message",b"nested_message","no_package",b"no_package","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message_in_oneof",b"outer_message_in_oneof","user_id",b"user_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_boolean",b"a_boolean","a_enum",b"a_enum","a_external_enum",b"a_external_enum","a_inner",b"a_inner","a_nested",b"a_nested","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_repeated_string",b"a_repeated_string","a_string",b"a_string","a_uint32",b"a_uint32","email",b"email","email_by_uid",b"email_by_uid","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","inner_message",b"inner_message","nested_enum",b"nested_enum","nested_message",b"nested_message","no_package",b"no_package","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message_in_oneof",b"outer_message_in_oneof","rep_inner_enum",b"rep_inner_enum","rep_inner_message",b"rep_inner_message","user_id",b"user_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["a_oneof",b"a_oneof"]) -> typing.Optional[typing_extensions.Literal["a_oneof_1","a_oneof_2","outer_message_in_oneof","outer_enum_in_oneof","inner_enum_in_oneof"]]: ...
global___Simple1 = Simple1

class Simple2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    A_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text = ...
    def __init__(self,
        *,
        a_string : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> None: ...
global___Simple2 = Simple2

class Extensions1(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXT1_STRING_FIELD_NUMBER: builtins.int
    ext1_string: typing.Text = ...
    ext: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[global___Simple1, global___Extensions1] = ...
    r"""ext"""

    def __init__(self,
        *,
        ext1_string : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ext1_string",b"ext1_string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ext1_string",b"ext1_string"]) -> None: ...
global___Extensions1 = Extensions1

class Extensions2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FLAG_FIELD_NUMBER: builtins.int
    flag: builtins.bool = ...
    foo: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[global___Simple1, global___Extensions2] = ...
    r"""foo"""

    def __init__(self,
        *,
        flag : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flag",b"flag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["flag",b"flag"]) -> None: ...
global___Extensions2 = Extensions2

class _r_None(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALID_FIELD_NUMBER: builtins.int
    valid: builtins.int = ...
    def __init__(self,
        *,
        valid : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["valid",b"valid"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["valid",b"valid"]) -> None: ...
global____r_None = _r_None

class PythonReservedKeywords(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _r_finally(_finally, metaclass=_finallyEnumTypeWrapper):
        pass
    class _finally:
        V = typing.NewType('V', builtins.int)
    class _finallyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_finally.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        valid_in_finally = PythonReservedKeywords._r_finally.V(2)

    valid_in_finally = PythonReservedKeywords._r_finally.V(2)

    class _r_lambda(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CONTINUE_FIELD_NUMBER: builtins.int
        VALID_FIELD_NUMBER: builtins.int
        valid: builtins.int = ...
        def __init__(self,
            *,
            valid : typing.Optional[builtins.int] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["continue",b"continue","valid",b"valid"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["continue",b"continue","valid",b"valid"]) -> None: ...

    FROM_FIELD_NUMBER: builtins.int
    IN_FIELD_NUMBER: builtins.int
    IS_FIELD_NUMBER: builtins.int
    FOR_FIELD_NUMBER: builtins.int
    TRY_FIELD_NUMBER: builtins.int
    DEF_FIELD_NUMBER: builtins.int
    NONLOCAL_FIELD_NUMBER: builtins.int
    WHILE_FIELD_NUMBER: builtins.int
    AND_FIELD_NUMBER: builtins.int
    DEL_FIELD_NUMBER: builtins.int
    GLOBAL_FIELD_NUMBER: builtins.int
    NOT_FIELD_NUMBER: builtins.int
    WITH_FIELD_NUMBER: builtins.int
    AS_FIELD_NUMBER: builtins.int
    ELIF_FIELD_NUMBER: builtins.int
    IF_FIELD_NUMBER: builtins.int
    OR_FIELD_NUMBER: builtins.int
    YIELD_FIELD_NUMBER: builtins.int
    ASSERT_FIELD_NUMBER: builtins.int
    ELSE_FIELD_NUMBER: builtins.int
    IMPORT_FIELD_NUMBER: builtins.int
    PASS_FIELD_NUMBER: builtins.int
    BREAK_FIELD_NUMBER: builtins.int
    EXCEPT_FIELD_NUMBER: builtins.int
    RAISE_FIELD_NUMBER: builtins.int
    FALSE_FIELD_NUMBER: builtins.int
    TRUE_FIELD_NUMBER: builtins.int
    CLASS_FIELD_NUMBER: builtins.int
    NONE_FIELD_NUMBER: builtins.int
    VALID_FIELD_NUMBER: builtins.int
    @property
    def none(self) -> global____r_None:
        r"""Test unreserved identifiers w/ reserved message names"""
        pass
    valid: global___PythonReservedKeywords._r_finally.V = ...
    def __init__(self,
        *,
        none : typing.Optional[global____r_None] = ...,
        valid : typing.Optional[global___PythonReservedKeywords._r_finally.V] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["False",b"False","True",b"True","and",b"and","as",b"as","assert",b"assert","break",b"break","class",b"class","def",b"def","del",b"del","elif",b"elif","else",b"else","except",b"except","for",b"for","from",b"from","global",b"global","if",b"if","import",b"import","in",b"in","is",b"is","none",b"none","nonlocal",b"nonlocal","not",b"not","or",b"or","pass",b"pass","raise",b"raise","try",b"try","valid",b"valid","while",b"while","with",b"with","yield",b"yield"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["False",b"False","True",b"True","and",b"and","as",b"as","assert",b"assert","break",b"break","class",b"class","def",b"def","del",b"del","elif",b"elif","else",b"else","except",b"except","for",b"for","from",b"from","global",b"global","if",b"if","import",b"import","in",b"in","is",b"is","none",b"none","nonlocal",b"nonlocal","not",b"not","or",b"or","pass",b"pass","raise",b"raise","try",b"try","valid",b"valid","while",b"while","with",b"with","yield",b"yield"]) -> None: ...
global___PythonReservedKeywords = PythonReservedKeywords

class PythonReservedKeywordsSmall(google.protobuf.message.Message):
    r"""Do one with just one arg - to make sure it's syntactically correct"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FROM_FIELD_NUMBER: builtins.int
    def __init__(self,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["from",b"from"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["from",b"from"]) -> None: ...
global___PythonReservedKeywordsSmall = PythonReservedKeywordsSmall

class SelfField(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SELF_FIELD_NUMBER: builtins.int
    self: builtins.int = ...
    r"""Field self -> must generate an __init__ method w/ different name"""

    def __init__(self_,
        *,
        self : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["self",b"self"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["self",b"self"]) -> None: ...
global___SelfField = SelfField

class PythonReservedKeywordsService(google.protobuf.service.Service, metaclass=abc.ABCMeta):
    r"""Method name is reserved"""
    @abc.abstractmethod
    def valid_method_name1(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global____r_None], None]],
    ) -> concurrent.futures.Future[global____r_None]:
        r"""valid_method_name1"""
        pass
    @abc.abstractmethod
    def valid_method_name2(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___PythonReservedKeywords._r_lambda], None]],
    ) -> concurrent.futures.Future[global___PythonReservedKeywords._r_lambda]:
        r"""valid_method_name2"""
        pass
class PythonReservedKeywordsService_Stub(PythonReservedKeywordsService):
    r"""Method name is reserved"""
    def __init__(self, rpc_channel: google.protobuf.service.RpcChannel) -> None: ...
    def valid_method_name1(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global____r_None], None]],
    ) -> concurrent.futures.Future[global____r_None]:
        r"""valid_method_name1"""
        pass
    def valid_method_name2(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___PythonReservedKeywords._r_lambda], None]],
    ) -> concurrent.futures.Future[global___PythonReservedKeywords._r_lambda]:
        r"""valid_method_name2"""
        pass
class ATestService(google.protobuf.service.Service, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Echo(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___Simple2], None]],
    ) -> concurrent.futures.Future[global___Simple2]: ...
class ATestService_Stub(ATestService):
    def __init__(self, rpc_channel: google.protobuf.service.RpcChannel) -> None: ...
    def Echo(self,
        rpc_controller: google.protobuf.service.RpcController,
        request: global___Simple1,
        done: typing.Optional[typing.Callable[[global___Simple2], None]],
    ) -> concurrent.futures.Future[global___Simple2]: ...