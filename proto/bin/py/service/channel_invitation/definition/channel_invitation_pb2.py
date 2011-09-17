# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='service/channel_invitation/definition/channel_invitation.proto',
  package='bnet.protocol.channel_invitation',
  serialized_pb='\n>service/channel_invitation/definition/channel_invitation.proto\x12 bnet.protocol.channel_invitation\x1a\x19lib/protocol/entity.proto\x1a\x1dlib/protocol/invitation.proto\x1a\x11lib/rpc/rpc.proto\x1a(service/channel/definition/channel.proto\x1a\x39service/channel_invitation/channel_invitation_types.proto\"n\n\x17\x41\x63\x63\x65ptInvitationRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x15\n\rinvitation_id\x18\x02 \x02(\x06\x12\x11\n\tobject_id\x18\x03 \x02(\x04\"-\n\x18\x41\x63\x63\x65ptInvitationResponse\x12\x11\n\tobject_id\x18\x01 \x02(\x04\"P\n\x10SubscribeRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x02 \x02(\x04\"\xa2\x01\n\x11SubscribeResponse\x12J\n\ncollection\x18\x01 \x03(\x0b\x32\x36.bnet.protocol.channel_invitation.InvitationCollection\x12\x41\n\x13received_invitation\x18\x02 \x03(\x0b\x32$.bnet.protocol.invitation.Invitation\"?\n\x12UnsubscribeRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\xcc\x01\n\x18SuggestInvitationRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12+\n\nchannel_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x03 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12,\n\x0b\x61pproval_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"\xb4\x01\n\x17RevokeInvitationRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\ttarget_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x15\n\rinvitation_id\x18\x03 \x02(\x06\x12+\n\nchannel_id\x18\x04 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"3\n\x1bHasRoomForInvitationRequest\x12\x14\n\x0cservice_type\x18\x01 \x02(\r\"W\n\x1bInvitationAddedNotification\x12\x38\n\ninvitation\x18\x01 \x02(\x0b\x32$.bnet.protocol.invitation.Invitation\"i\n\x1dInvitationRemovedNotification\x12\x38\n\ninvitation\x18\x01 \x02(\x0b\x32$.bnet.protocol.invitation.Invitation\x12\x0e\n\x06reason\x18\x02 \x01(\r\"W\n\x1bSuggestionAddedNotification\x12\x38\n\nsuggestion\x18\x01 \x02(\x0b\x32$.bnet.protocol.invitation.Suggestion2\x91\x06\n\x18\x43hannelInvitationService\x12t\n\tSubscribe\x12\x32.bnet.protocol.channel_invitation.SubscribeRequest\x1a\x33.bnet.protocol.channel_invitation.SubscribeResponse\x12Z\n\x0bUnsubscribe\x12\x34.bnet.protocol.channel_invitation.UnsubscribeRequest\x1a\x15.bnet.protocol.NoData\x12s\n\x0eSendInvitation\x12/.bnet.protocol.invitation.SendInvitationRequest\x1a\x30.bnet.protocol.invitation.SendInvitationResponse\x12\x89\x01\n\x10\x41\x63\x63\x65ptInvitation\x12\x39.bnet.protocol.channel_invitation.AcceptInvitationRequest\x1a:.bnet.protocol.channel_invitation.AcceptInvitationResponse\x12T\n\x11\x44\x65\x63lineInvitation\x12(.bnet.protocol.invitation.GenericRequest\x1a\x15.bnet.protocol.NoData\x12\x64\n\x10RevokeInvitation\x12\x39.bnet.protocol.channel_invitation.RevokeInvitationRequest\x1a\x15.bnet.protocol.NoData\x12\x66\n\x11SuggestInvitation\x12:.bnet.protocol.channel_invitation.SuggestInvitationRequest\x1a\x15.bnet.protocol.NoData2\xff\x03\n\x17\x43hannelInvitationNotify\x12z\n\x1dNotifyReceivedInvitationAdded\x12=.bnet.protocol.channel_invitation.InvitationAddedNotification\x1a\x1a.bnet.protocol.NO_RESPONSE\x12~\n\x1fNotifyReceivedInvitationRemoved\x12?.bnet.protocol.channel_invitation.InvitationRemovedNotification\x1a\x1a.bnet.protocol.NO_RESPONSE\x12z\n\x1dNotifyReceivedSuggestionAdded\x12=.bnet.protocol.channel_invitation.SuggestionAddedNotification\x1a\x1a.bnet.protocol.NO_RESPONSE\x12l\n\x14HasRoomForInvitation\x12=.bnet.protocol.channel_invitation.HasRoomForInvitationRequest\x1a\x15.bnet.protocol.NoDataB\x03\x80\x01\x01')




_ACCEPTINVITATIONREQUEST = descriptor.Descriptor(
  name='AcceptInvitationRequest',
  full_name='bnet.protocol.channel_invitation.AcceptInvitationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel_invitation.AcceptInvitationRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='invitation_id', full_name='bnet.protocol.channel_invitation.AcceptInvitationRequest.invitation_id', index=1,
      number=2, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel_invitation.AcceptInvitationRequest.object_id', index=2,
      number=3, type=4, cpp_type=4, label=2,
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
  serialized_start=278,
  serialized_end=388,
)


_ACCEPTINVITATIONRESPONSE = descriptor.Descriptor(
  name='AcceptInvitationResponse',
  full_name='bnet.protocol.channel_invitation.AcceptInvitationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel_invitation.AcceptInvitationResponse.object_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=390,
  serialized_end=435,
)


_SUBSCRIBEREQUEST = descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='bnet.protocol.channel_invitation.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel_invitation.SubscribeRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.channel_invitation.SubscribeRequest.object_id', index=1,
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
  serialized_start=437,
  serialized_end=517,
)


_SUBSCRIBERESPONSE = descriptor.Descriptor(
  name='SubscribeResponse',
  full_name='bnet.protocol.channel_invitation.SubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='collection', full_name='bnet.protocol.channel_invitation.SubscribeResponse.collection', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='received_invitation', full_name='bnet.protocol.channel_invitation.SubscribeResponse.received_invitation', index=1,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=520,
  serialized_end=682,
)


_UNSUBSCRIBEREQUEST = descriptor.Descriptor(
  name='UnsubscribeRequest',
  full_name='bnet.protocol.channel_invitation.UnsubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel_invitation.UnsubscribeRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=684,
  serialized_end=747,
)


_SUGGESTINVITATIONREQUEST = descriptor.Descriptor(
  name='SuggestInvitationRequest',
  full_name='bnet.protocol.channel_invitation.SuggestInvitationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel_invitation.SuggestInvitationRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel_invitation.SuggestInvitationRequest.channel_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.channel_invitation.SuggestInvitationRequest.target_id', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='approval_id', full_name='bnet.protocol.channel_invitation.SuggestInvitationRequest.approval_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=750,
  serialized_end=954,
)


_REVOKEINVITATIONREQUEST = descriptor.Descriptor(
  name='RevokeInvitationRequest',
  full_name='bnet.protocol.channel_invitation.RevokeInvitationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.channel_invitation.RevokeInvitationRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='bnet.protocol.channel_invitation.RevokeInvitationRequest.target_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='invitation_id', full_name='bnet.protocol.channel_invitation.RevokeInvitationRequest.invitation_id', index=2,
      number=3, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel_invitation.RevokeInvitationRequest.channel_id', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=957,
  serialized_end=1137,
)


_HASROOMFORINVITATIONREQUEST = descriptor.Descriptor(
  name='HasRoomForInvitationRequest',
  full_name='bnet.protocol.channel_invitation.HasRoomForInvitationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_type', full_name='bnet.protocol.channel_invitation.HasRoomForInvitationRequest.service_type', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=1139,
  serialized_end=1190,
)


_INVITATIONADDEDNOTIFICATION = descriptor.Descriptor(
  name='InvitationAddedNotification',
  full_name='bnet.protocol.channel_invitation.InvitationAddedNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='invitation', full_name='bnet.protocol.channel_invitation.InvitationAddedNotification.invitation', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=1192,
  serialized_end=1279,
)


_INVITATIONREMOVEDNOTIFICATION = descriptor.Descriptor(
  name='InvitationRemovedNotification',
  full_name='bnet.protocol.channel_invitation.InvitationRemovedNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='invitation', full_name='bnet.protocol.channel_invitation.InvitationRemovedNotification.invitation', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reason', full_name='bnet.protocol.channel_invitation.InvitationRemovedNotification.reason', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1281,
  serialized_end=1386,
)


_SUGGESTIONADDEDNOTIFICATION = descriptor.Descriptor(
  name='SuggestionAddedNotification',
  full_name='bnet.protocol.channel_invitation.SuggestionAddedNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='suggestion', full_name='bnet.protocol.channel_invitation.SuggestionAddedNotification.suggestion', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=1388,
  serialized_end=1475,
)

import lib.protocol.entity_pb2
import lib.protocol.invitation_pb2
import lib.rpc.rpc_pb2
import service.channel.definition.channel_pb2
import service.channel_invitation.channel_invitation_types_pb2

_ACCEPTINVITATIONREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUBSCRIBEREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUBSCRIBERESPONSE.fields_by_name['collection'].message_type = service.channel_invitation.channel_invitation_types_pb2._INVITATIONCOLLECTION
_SUBSCRIBERESPONSE.fields_by_name['received_invitation'].message_type = lib.protocol.invitation_pb2._INVITATION
_UNSUBSCRIBEREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUGGESTINVITATIONREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUGGESTINVITATIONREQUEST.fields_by_name['channel_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUGGESTINVITATIONREQUEST.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_SUGGESTINVITATIONREQUEST.fields_by_name['approval_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_REVOKEINVITATIONREQUEST.fields_by_name['agent_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_REVOKEINVITATIONREQUEST.fields_by_name['target_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_REVOKEINVITATIONREQUEST.fields_by_name['channel_id'].message_type = lib.protocol.entity_pb2._ENTITYID
_INVITATIONADDEDNOTIFICATION.fields_by_name['invitation'].message_type = lib.protocol.invitation_pb2._INVITATION
_INVITATIONREMOVEDNOTIFICATION.fields_by_name['invitation'].message_type = lib.protocol.invitation_pb2._INVITATION
_SUGGESTIONADDEDNOTIFICATION.fields_by_name['suggestion'].message_type = lib.protocol.invitation_pb2._SUGGESTION

class AcceptInvitationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCEPTINVITATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.AcceptInvitationRequest)

class AcceptInvitationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCEPTINVITATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.AcceptInvitationResponse)

class SubscribeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSCRIBEREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.SubscribeRequest)

class SubscribeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSCRIBERESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.SubscribeResponse)

class UnsubscribeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNSUBSCRIBEREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.UnsubscribeRequest)

class SuggestInvitationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUGGESTINVITATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.SuggestInvitationRequest)

class RevokeInvitationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REVOKEINVITATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.RevokeInvitationRequest)

class HasRoomForInvitationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HASROOMFORINVITATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.HasRoomForInvitationRequest)

class InvitationAddedNotification(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INVITATIONADDEDNOTIFICATION
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.InvitationAddedNotification)

class InvitationRemovedNotification(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INVITATIONREMOVEDNOTIFICATION
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.InvitationRemovedNotification)

class SuggestionAddedNotification(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUGGESTIONADDEDNOTIFICATION
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel_invitation.SuggestionAddedNotification)


_CHANNELINVITATIONSERVICE = descriptor.ServiceDescriptor(
  name='ChannelInvitationService',
  full_name='bnet.protocol.channel_invitation.ChannelInvitationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1478,
  serialized_end=2263,
  methods=[
  descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.Subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIBERESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Unsubscribe',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.Unsubscribe',
    index=1,
    containing_service=None,
    input_type=_UNSUBSCRIBEREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='SendInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.SendInvitation',
    index=2,
    containing_service=None,
    input_type=lib.protocol.invitation_pb2._SENDINVITATIONREQUEST,
    output_type=lib.protocol.invitation_pb2._SENDINVITATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='AcceptInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.AcceptInvitation',
    index=3,
    containing_service=None,
    input_type=_ACCEPTINVITATIONREQUEST,
    output_type=_ACCEPTINVITATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='DeclineInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.DeclineInvitation',
    index=4,
    containing_service=None,
    input_type=lib.protocol.invitation_pb2._GENERICREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='RevokeInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.RevokeInvitation',
    index=5,
    containing_service=None,
    input_type=_REVOKEINVITATIONREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='SuggestInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationService.SuggestInvitation',
    index=6,
    containing_service=None,
    input_type=_SUGGESTINVITATIONREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
])
'''
class ChannelInvitationService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _CHANNELINVITATIONSERVICE
class ChannelInvitationService_Stub(ChannelInvitationService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _CHANNELINVITATIONSERVICE


_CHANNELINVITATIONNOTIFY = descriptor.ServiceDescriptor(
  name='ChannelInvitationNotify',
  full_name='bnet.protocol.channel_invitation.ChannelInvitationNotify',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=2266,
  serialized_end=2777,
  methods=[
  descriptor.MethodDescriptor(
    name='NotifyReceivedInvitationAdded',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationNotify.NotifyReceivedInvitationAdded',
    index=0,
    containing_service=None,
    input_type=_INVITATIONADDEDNOTIFICATION,
    output_type=lib.rpc.rpc_pb2._NO_RESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='NotifyReceivedInvitationRemoved',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationNotify.NotifyReceivedInvitationRemoved',
    index=1,
    containing_service=None,
    input_type=_INVITATIONREMOVEDNOTIFICATION,
    output_type=lib.rpc.rpc_pb2._NO_RESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='NotifyReceivedSuggestionAdded',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationNotify.NotifyReceivedSuggestionAdded',
    index=2,
    containing_service=None,
    input_type=_SUGGESTIONADDEDNOTIFICATION,
    output_type=lib.rpc.rpc_pb2._NO_RESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='HasRoomForInvitation',
    full_name='bnet.protocol.channel_invitation.ChannelInvitationNotify.HasRoomForInvitation',
    index=3,
    containing_service=None,
    input_type=_HASROOMFORINVITATIONREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
])

class ChannelInvitationNotify(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _CHANNELINVITATIONNOTIFY
class ChannelInvitationNotify_Stub(ChannelInvitationNotify):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _CHANNELINVITATIONNOTIFY

# @@protoc_insertion_point(module_scope)
'''