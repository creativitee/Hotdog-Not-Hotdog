# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hashing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hashing.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rhashing.proto\"&\n\x0bHashRequest\x12\x17\n\x0fphotoByteStream\x18\x01 \x01(\t\"\x1e\n\tHashReply\x12\x11\n\thashedKey\x18\x01 \x01(\t2:\n\x11\x42yteStreamHashing\x12%\n\x07Hashing\x12\x0c.HashRequest\x1a\n.HashReply\"\x00\x62\x06proto3')
)




_HASHREQUEST = _descriptor.Descriptor(
  name='HashRequest',
  full_name='HashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photoByteStream', full_name='HashRequest.photoByteStream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=55,
)


_HASHREPLY = _descriptor.Descriptor(
  name='HashReply',
  full_name='HashReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashedKey', full_name='HashReply.hashedKey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['HashRequest'] = _HASHREQUEST
DESCRIPTOR.message_types_by_name['HashReply'] = _HASHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HashRequest = _reflection.GeneratedProtocolMessageType('HashRequest', (_message.Message,), {
  'DESCRIPTOR' : _HASHREQUEST,
  '__module__' : 'hashing_pb2'
  # @@protoc_insertion_point(class_scope:HashRequest)
  })
_sym_db.RegisterMessage(HashRequest)

HashReply = _reflection.GeneratedProtocolMessageType('HashReply', (_message.Message,), {
  'DESCRIPTOR' : _HASHREPLY,
  '__module__' : 'hashing_pb2'
  # @@protoc_insertion_point(class_scope:HashReply)
  })
_sym_db.RegisterMessage(HashReply)



_BYTESTREAMHASHING = _descriptor.ServiceDescriptor(
  name='ByteStreamHashing',
  full_name='ByteStreamHashing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=89,
  serialized_end=147,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hashing',
    full_name='ByteStreamHashing.Hashing',
    index=0,
    containing_service=None,
    input_type=_HASHREQUEST,
    output_type=_HASHREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BYTESTREAMHASHING)

DESCRIPTOR.services_by_name['ByteStreamHashing'] = _BYTESTREAMHASHING

# @@protoc_insertion_point(module_scope)
