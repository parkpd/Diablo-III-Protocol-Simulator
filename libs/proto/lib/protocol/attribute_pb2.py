# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='lib/protocol/attribute.proto',
  package='bnet.protocol.attribute',
  serialized_pb='\n\x1clib/protocol/attribute.proto\x12\x17\x62net.protocol.attribute\"\xb0\x01\n\x07Variant\x12\x12\n\nbool_value\x18\x02 \x01(\x08\x12\x11\n\tint_value\x18\x03 \x01(\x03\x12\x13\n\x0b\x66loat_value\x18\x04 \x01(\x01\x12\x14\n\x0cstring_value\x18\x05 \x01(\t\x12\x12\n\nblob_value\x18\x06 \x01(\x0c\x12\x15\n\rmessage_value\x18\x07 \x01(\x0c\x12\x14\n\x0c\x66ourcc_value\x18\x08 \x01(\t\x12\x12\n\nuint_value\x18\t \x01(\x04\"J\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x12/\n\x05value\x18\x02 \x02(\x0b\x32 .bnet.protocol.attribute.Variant\"\xe0\x01\n\x0f\x41ttributeFilter\x12>\n\x02op\x18\x01 \x02(\x0e\x32\x32.bnet.protocol.attribute.AttributeFilter.Operation\x12\x35\n\tattribute\x18\x02 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"V\n\tOperation\x12\x0e\n\nMATCH_NONE\x10\x00\x12\r\n\tMATCH_ANY\x10\x01\x12\r\n\tMATCH_ALL\x10\x02\x12\x1b\n\x17MATCH_ALL_MOST_SPECIFIC\x10\x03\x42\x0c\x42\nCAttribute')



_ATTRIBUTEFILTER_OPERATION = descriptor.EnumDescriptor(
  name='Operation',
  full_name='bnet.protocol.attribute.AttributeFilter.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MATCH_NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MATCH_ANY', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MATCH_ALL', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MATCH_ALL_MOST_SPECIFIC', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=451,
  serialized_end=537,
)


_VARIANT = descriptor.Descriptor(
  name='Variant',
  full_name='bnet.protocol.attribute.Variant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bool_value', full_name='bnet.protocol.attribute.Variant.bool_value', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int_value', full_name='bnet.protocol.attribute.Variant.int_value', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='float_value', full_name='bnet.protocol.attribute.Variant.float_value', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='string_value', full_name='bnet.protocol.attribute.Variant.string_value', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='blob_value', full_name='bnet.protocol.attribute.Variant.blob_value', index=4,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message_value', full_name='bnet.protocol.attribute.Variant.message_value', index=5,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fourcc_value', full_name='bnet.protocol.attribute.Variant.fourcc_value', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uint_value', full_name='bnet.protocol.attribute.Variant.uint_value', index=7,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=234,
)


_ATTRIBUTE = descriptor.Descriptor(
  name='Attribute',
  full_name='bnet.protocol.attribute.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='bnet.protocol.attribute.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='bnet.protocol.attribute.Attribute.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=236,
  serialized_end=310,
)


_ATTRIBUTEFILTER = descriptor.Descriptor(
  name='AttributeFilter',
  full_name='bnet.protocol.attribute.AttributeFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='op', full_name='bnet.protocol.attribute.AttributeFilter.op', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.attribute.AttributeFilter.attribute', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTRIBUTEFILTER_OPERATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=313,
  serialized_end=537,
)


_ATTRIBUTE.fields_by_name['value'].message_type = _VARIANT
_ATTRIBUTEFILTER.fields_by_name['op'].enum_type = _ATTRIBUTEFILTER_OPERATION
_ATTRIBUTEFILTER.fields_by_name['attribute'].message_type = _ATTRIBUTE
_ATTRIBUTEFILTER_OPERATION.containing_type = _ATTRIBUTEFILTER;

class Variant(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VARIANT
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.attribute.Variant)

class Attribute(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTRIBUTE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.attribute.Attribute)

class AttributeFilter(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTRIBUTEFILTER
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.attribute.AttributeFilter)

# @@protoc_insertion_point(module_scope)
