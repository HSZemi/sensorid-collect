# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TestData.proto

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
  name='TestData.proto',
  package='sensorid',
  serialized_pb=_b('\n\x0eTestData.proto\x12\x08sensorid\"\xfc\x03\n\rFeatureVector\x12\x12\n\nsensortype\x18\x01 \x02(\t\x12\x12\n\nsensorname\x18\x02 \x02(\t\x12\x0e\n\x06mean_x\x18\x03 \x02(\x01\x12\x0e\n\x06mean_y\x18\x04 \x02(\x01\x12\x0e\n\x06mean_z\x18\x05 \x02(\x01\x12\r\n\x05min_x\x18\x06 \x02(\x01\x12\r\n\x05min_y\x18\x07 \x02(\x01\x12\r\n\x05min_z\x18\x08 \x02(\x01\x12\r\n\x05max_x\x18\t \x02(\x01\x12\r\n\x05max_y\x18\n \x02(\x01\x12\r\n\x05max_z\x18\x0b \x02(\x01\x12\x10\n\x08stddev_x\x18\x0c \x02(\x01\x12\x10\n\x08stddev_y\x18\r \x02(\x01\x12\x10\n\x08stddev_z\x18\x0e \x02(\x01\x12\x10\n\x08\x61vgdev_x\x18\x0f \x02(\x01\x12\x10\n\x08\x61vgdev_y\x18\x10 \x02(\x01\x12\x10\n\x08\x61vgdev_z\x18\x11 \x02(\x01\x12\x12\n\nskewness_x\x18\x12 \x02(\x01\x12\x12\n\nskewness_y\x18\x13 \x02(\x01\x12\x12\n\nskewness_z\x18\x14 \x02(\x01\x12\x12\n\nkurtosis_x\x18\x15 \x02(\x01\x12\x12\n\nkurtosis_y\x18\x16 \x02(\x01\x12\x12\n\nkurtosis_z\x18\x17 \x02(\x01\x12\x16\n\x0ermsamplitude_x\x18\x18 \x02(\x01\x12\x16\n\x0ermsamplitude_y\x18\x19 \x02(\x01\x12\x16\n\x0ermsamplitude_z\x18\x1a \x02(\x01\x12\r\n\x05\x63ount\x18\x1b \x02(\x01\"(\n\nTestResult\x12\x1a\n\x12result_displayname\x18\x01 \x02(\tB\x19\n\x17\x64\x65.hszemi.sensorid_test')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FEATUREVECTOR = _descriptor.Descriptor(
  name='FeatureVector',
  full_name='sensorid.FeatureVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensortype', full_name='sensorid.FeatureVector.sensortype', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensorname', full_name='sensorid.FeatureVector.sensorname', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_x', full_name='sensorid.FeatureVector.mean_x', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_y', full_name='sensorid.FeatureVector.mean_y', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_z', full_name='sensorid.FeatureVector.mean_z', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_x', full_name='sensorid.FeatureVector.min_x', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_y', full_name='sensorid.FeatureVector.min_y', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_z', full_name='sensorid.FeatureVector.min_z', index=7,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_x', full_name='sensorid.FeatureVector.max_x', index=8,
      number=9, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_y', full_name='sensorid.FeatureVector.max_y', index=9,
      number=10, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_z', full_name='sensorid.FeatureVector.max_z', index=10,
      number=11, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stddev_x', full_name='sensorid.FeatureVector.stddev_x', index=11,
      number=12, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stddev_y', full_name='sensorid.FeatureVector.stddev_y', index=12,
      number=13, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stddev_z', full_name='sensorid.FeatureVector.stddev_z', index=13,
      number=14, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgdev_x', full_name='sensorid.FeatureVector.avgdev_x', index=14,
      number=15, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgdev_y', full_name='sensorid.FeatureVector.avgdev_y', index=15,
      number=16, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgdev_z', full_name='sensorid.FeatureVector.avgdev_z', index=16,
      number=17, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skewness_x', full_name='sensorid.FeatureVector.skewness_x', index=17,
      number=18, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skewness_y', full_name='sensorid.FeatureVector.skewness_y', index=18,
      number=19, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skewness_z', full_name='sensorid.FeatureVector.skewness_z', index=19,
      number=20, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kurtosis_x', full_name='sensorid.FeatureVector.kurtosis_x', index=20,
      number=21, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kurtosis_y', full_name='sensorid.FeatureVector.kurtosis_y', index=21,
      number=22, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kurtosis_z', full_name='sensorid.FeatureVector.kurtosis_z', index=22,
      number=23, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rmsamplitude_x', full_name='sensorid.FeatureVector.rmsamplitude_x', index=23,
      number=24, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rmsamplitude_y', full_name='sensorid.FeatureVector.rmsamplitude_y', index=24,
      number=25, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rmsamplitude_z', full_name='sensorid.FeatureVector.rmsamplitude_z', index=25,
      number=26, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='sensorid.FeatureVector.count', index=26,
      number=27, type=1, cpp_type=5, label=2,
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
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=537,
)


_TESTRESULT = _descriptor.Descriptor(
  name='TestResult',
  full_name='sensorid.TestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_displayname', full_name='sensorid.TestResult.result_displayname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=579,
)

DESCRIPTOR.message_types_by_name['FeatureVector'] = _FEATUREVECTOR
DESCRIPTOR.message_types_by_name['TestResult'] = _TESTRESULT

FeatureVector = _reflection.GeneratedProtocolMessageType('FeatureVector', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREVECTOR,
  __module__ = 'TestData_pb2'
  # @@protoc_insertion_point(class_scope:sensorid.FeatureVector)
  ))
_sym_db.RegisterMessage(FeatureVector)

TestResult = _reflection.GeneratedProtocolMessageType('TestResult', (_message.Message,), dict(
  DESCRIPTOR = _TESTRESULT,
  __module__ = 'TestData_pb2'
  # @@protoc_insertion_point(class_scope:sensorid.TestResult)
  ))
_sym_db.RegisterMessage(TestResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027de.hszemi.sensorid_test'))
# @@protoc_insertion_point(module_scope)
