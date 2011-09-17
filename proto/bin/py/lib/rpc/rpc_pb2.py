# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='lib/rpc/rpc.proto',
  package='bnet.protocol',
  serialized_pb='\n\x11lib/rpc/rpc.proto\x12\rbnet.protocol\x1a google/protobuf/descriptor.proto\"\r\n\x0bNO_RESPONSE\"N\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12$\n\x04next\x18\x03 \x01(\x0b\x32\x16.bnet.protocol.Address\")\n\tProcessId\x12\r\n\x05label\x18\x01 \x02(\r\x12\r\n\x05\x65poch\x18\x02 \x02(\r\"J\n\rObjectAddress\x12&\n\x04host\x18\x01 \x02(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x11\n\tobject_id\x18\x02 \x02(\x04\"\x08\n\x06NoData:3\n\tmethod_id\x12\x1e.google.protobuf.MethodOptions\x18\xd0\x86\x03 \x01(\r:.\n\x04\x63ost\x12\x1e.google.protobuf.MethodOptions\x18\xd1\x86\x03 \x01(\r:1\n\x07timeout\x12\x1e.google.protobuf.MethodOptions\x18\xd2\x86\x03 \x01(\x02')


METHOD_ID_FIELD_NUMBER = 50000
method_id = descriptor.FieldDescriptor(
  name='method_id', full_name='bnet.protocol.method_id', index=0,
  number=50000, type=13, cpp_type=3, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
COST_FIELD_NUMBER = 50001
cost = descriptor.FieldDescriptor(
  name='cost', full_name='bnet.protocol.cost', index=1,
  number=50001, type=13, cpp_type=3, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
TIMEOUT_FIELD_NUMBER = 50002
timeout = descriptor.FieldDescriptor(
  name='timeout', full_name='bnet.protocol.timeout', index=2,
  number=50002, type=2, cpp_type=6, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_NO_RESPONSE = descriptor.Descriptor(
  name='NO_RESPONSE',
  full_name='bnet.protocol.NO_RESPONSE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=70,
  serialized_end=83,
)


_ADDRESS = descriptor.Descriptor(
  name='Address',
  full_name='bnet.protocol.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='bnet.protocol.Address.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='port', full_name='bnet.protocol.Address.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next', full_name='bnet.protocol.Address.next', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=85,
  serialized_end=163,
)


_PROCESSID = descriptor.Descriptor(
  name='ProcessId',
  full_name='bnet.protocol.ProcessId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='label', full_name='bnet.protocol.ProcessId.label', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='epoch', full_name='bnet.protocol.ProcessId.epoch', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=165,
  serialized_end=206,
)


_OBJECTADDRESS = descriptor.Descriptor(
  name='ObjectAddress',
  full_name='bnet.protocol.ObjectAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.ObjectAddress.host', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.ObjectAddress.object_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  serialized_start=208,
  serialized_end=282,
)


_NODATA = descriptor.Descriptor(
  name='NoData',
  full_name='bnet.protocol.NoData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=284,
  serialized_end=292,
)

import google.protobuf.descriptor_pb2

_ADDRESS.fields_by_name['next'].message_type = _ADDRESS
_OBJECTADDRESS.fields_by_name['host'].message_type = _PROCESSID

class NO_RESPONSE(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NO_RESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.NO_RESPONSE)

class Address(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDRESS
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.Address)

class ProcessId(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCESSID
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.ProcessId)

class ObjectAddress(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OBJECTADDRESS
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.ObjectAddress)

class NoData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NODATA
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.NoData)

google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(method_id)
google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(cost)
google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(timeout)
# @@protoc_insertion_point(module_scope)
