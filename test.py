import serial

crc_high_list = [
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40
]

crc_low_list = [
    0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06, 0x07, 0xC7,
    0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D, 0xCD, 0x0F, 0xCF, 0xCE, 0x0E,
    0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, 0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9,
    0x1B, 0xDB, 0xDA, 0x1A, 0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC,
    0x14, 0xD4, 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13, 0xD3,
    0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, 0xF2, 0x32,
    0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4, 0x3C, 0xFC, 0xFD, 0x3D,
    0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A, 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38,
    0x28, 0xE8, 0xE9, 0x29, 0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF,
    0x2D, 0xED, 0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26,
    0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60, 0x61, 0xA1,
    0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7, 0x67, 0xA5, 0x65, 0x64, 0xA4,
    0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, 0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB,
    0x69, 0xA9, 0xA8, 0x68, 0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA,
    0xBE, 0x7E, 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75, 0xB5,
    0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, 0x70, 0xB0,
    0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92, 0x96, 0x56, 0x57, 0x97,
    0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C, 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E,
    0x5A, 0x9A, 0x9B, 0x5B, 0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89,
    0x4B, 0x8B, 0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C,
    0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42, 0x43, 0x83,
    0x41, 0x81, 0x80, 0x40
]


def gen_crc16(buffer):
    crc_high = 0xFF
    crc_low = 0xFF

    for one in buffer:
        index = crc_high ^ one
        crc_high = crc_low ^ crc_high_list[index]
        crc_low = crc_low_list[index]

    return crc_high << 8 | crc_low


class Message(object):

    def __init__(self, packet_type, packet_id, cmd_type, args):
        self.packet_type = packet_type
        self.packet_id = packet_id
        self.cmd_type = cmd_type
        self.args = args
        self.length = len(self.args)
        self.crc16 = None

        self.__dump_data = b''

    def __str__(self):
        return "packet_type: {}\n" \
               "packet_id: {}\n" \
               "cmd_type: {}\n" \
               "args: {}\n" \
               "length: {}\n" \
               "crc16: {}".format(self.packet_type, self.packet_id, self.cmd_type, self.args, self.length, self.crc16)

    @classmethod
    def yield_file_bytes(cls, path):
        with open(path, 'rb') as f:
            while True:
                one_byte = f.read(1)
                if not one_byte:
                    break
                yield int.from_bytes(one_byte, 'little')
                # yield one_byte

    @classmethod
    def gen_file_crc16(cls, path):
        buffer = cls.yield_file_bytes(path)
        return gen_crc16(buffer)

    @classmethod
    def check_file_crc16(cls, path, checksum):
        return cls.gen_file_crc16(path) == int(checksum)

    @classmethod
    def crc16_check(cls, data, checksum):
        return gen_crc16(data) == int(checksum)

    @classmethod
    def gen_crc16(cls, bytes_data):
        return gen_crc16(bytes_data)

    def dump(self):
        if self.__dump_data:
            return self.__dump_data

        data = bytearray()
        data.append(self.packet_type)
        data.extend(self.packet_id.to_bytes(4, 'little'))
        data.append(self.cmd_type)
        data.extend(self.length.to_bytes(2, 'little'))
        if self.length != 0:
            data.extend(self.args)
        self.crc16 = self.gen_crc16(data)
        data.extend(self.crc16.to_bytes(2, 'little'))

        self.__dump_data = data
        return data


class TaskCaller(object):
    SerialClass = serial.Serial

    def __init__(self):
        """
        self._serial: 串口通信对象，SerialClass Object，默认是serial.Serial
        self._options: 用于保存可选串口配置参数
        """
        self._serial = None
        self._options = None

    @property
    def serial(self):
        return self._serial

    def open(self, config):
        self._serial = self.SerialClass(**config)

    def send(self, data):
        self._serial.write(data)

    def recv(self, nbytes):
        return self.serial.read(nbytes)


if __name__ == '__main__':
    # >>> CRC16
    # file_crc16 = Message.gen_file_crc16('readme.md')
    # print('file_crc16: ', file_crc16)
    # print(Message.check_file_crc16('readme.md', 5279))
    # <<<

    # >>> 交互调试
    caller = TaskCaller()
    caller.open(dict(port='COM37',
                 baudrate=115200,
                 bytesize=8,
                 parity='N',
                 stopbits=1,
                 timeout=2,
                 xonxoff=False))

    while True:
        content = caller.recv(8)

        if not content:
            print('content: ', content)
            continue

        packet_type = content[0]
        packet_id = int.from_bytes(content[1:5], 'little')
        cmd_type = content[5]
        length = int.from_bytes(content[6:8], 'little')

        content += caller.recv(length + 2)

        args = content[8:-2]
        crc16 = content[-2:]

        print('packet_type: ', packet_type)
        print('packet_id: ', packet_id)
        print('cmd_type: ', cmd_type)
        print('length: ', length)
        print('crc16: ', crc16)
        print('args: ', args)
        print('content: ', content)

        if cmd_type == 0x02:
            try:
                if args[0] == 0x00:
                    print('成功')
                if args[0] == 0xff:
                    print('失败！')
            except:
                break

            data = bytearray()
            data.append(1)
            data.extend(packet_id.to_bytes(4, 'little'))
            data.append(cmd_type)
            data.extend((0).to_bytes(2, 'little'))
            data.extend(Message.gen_crc16(data).to_bytes(2, 'little'))
            caller.send(data)

            break

        data = bytearray()
        data.append(1)
        data.extend(packet_id.to_bytes(4, 'little'))
        data.append(cmd_type)
        data.extend((0).to_bytes(2, 'little'))
        data.extend((Message.gen_crc16(data)).to_bytes(2, 'little'))
        caller.send(data)
        print('----')
        print('send data: ', data)
        print('----')




