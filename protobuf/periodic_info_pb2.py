# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: periodic-info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='periodic-info.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13periodic-info.proto\"b\n\x0cPeriodicInfo\x12\x16\n\x0egame_server_ip\x18\x01 \x02(\t\x12\n\n\x02\x66\x32\x18\x02 \x01(\r\x12\n\n\x02\x66\x33\x18\x03 \x01(\r\x12\n\n\x02\x66\x34\x18\x04 \x01(\r\x12\n\n\x02\x66\x35\x18\x05 \x01(\r\x12\n\n\x02\x66\x36\x18\x06 \x01(\r\"-\n\rPeriodicInfos\x12\x1c\n\x05infos\x18\x01 \x03(\x0b\x32\r.PeriodicInfo')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERIODICINFO = _descriptor.Descriptor(
  name='PeriodicInfo',
  full_name='PeriodicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_server_ip', full_name='PeriodicInfo.game_server_ip', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f2', full_name='PeriodicInfo.f2', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f3', full_name='PeriodicInfo.f3', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f4', full_name='PeriodicInfo.f4', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f5', full_name='PeriodicInfo.f5', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f6', full_name='PeriodicInfo.f6', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=121,
)


_PERIODICINFOS = _descriptor.Descriptor(
  name='PeriodicInfos',
  full_name='PeriodicInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infos', full_name='PeriodicInfos.infos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=168,
)

_PERIODICINFOS.fields_by_name['infos'].message_type = _PERIODICINFO
DESCRIPTOR.message_types_by_name['PeriodicInfo'] = _PERIODICINFO
DESCRIPTOR.message_types_by_name['PeriodicInfos'] = _PERIODICINFOS

PeriodicInfo = _reflection.GeneratedProtocolMessageType('PeriodicInfo', (_message.Message,), dict(
  DESCRIPTOR = _PERIODICINFO,
  __module__ = 'periodic_info_pb2'
  # @@protoc_insertion_point(class_scope:PeriodicInfo)
  ))
_sym_db.RegisterMessage(PeriodicInfo)

PeriodicInfos = _reflection.GeneratedProtocolMessageType('PeriodicInfos', (_message.Message,), dict(
  DESCRIPTOR = _PERIODICINFOS,
  __module__ = 'periodic_info_pb2'
  # @@protoc_insertion_point(class_scope:PeriodicInfos)
  ))
_sym_db.RegisterMessage(PeriodicInfos)


# @@protoc_insertion_point(module_scope)
