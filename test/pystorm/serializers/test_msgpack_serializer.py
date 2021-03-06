from __future__ import absolute_import, print_function, unicode_literals

from io import BytesIO
try:
    from unittest import mock
except ImportError:
    import mock

import msgpack

from pystorm.serializers.msgpack_serializer import MsgpackSerializer

from .serializer import SerializerTestCase


class TestMsgpackSerializer(SerializerTestCase):

    INSTANCE_CLS = MsgpackSerializer

    def test_read_message_dict(self):
        msg_dict = {b'hello': b"world",}
        self.instance.input_stream = BytesIO(msgpack.packb(msg_dict))
        assert self.instance.read_message() == msg_dict

    def test_read_message_list(self):
        msg_list = [3, 4, 5]
        self.instance.input_stream = BytesIO(msgpack.packb(msg_list))
        assert self.instance.read_message() == msg_list

    def test_send_message(self):
        msg_dict = {'hello': "world"}
        expected_output = msgpack.packb(msg_dict)
        self.instance.send_message(msg_dict)
        assert self.instance.output_stream.getvalue() == expected_output
