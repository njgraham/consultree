from asciitree import LeftAligned
from collections import OrderedDict


def main(argv, consul_kvget_recurse):
    host, key = argv[1:3]

    kvs = [(entry['Key'], entry['Value'])
           for entry in
           consul_kvget_recurse(host=host, key=key)[1]]

    kv_combined = OrderedDict()
    for key, value in kvs:
        sub_dict = kv_combined
        for part in key.split('/') + [value.decode('utf-8')]:
            if part not in sub_dict.keys():
                sub_dict[part] = OrderedDict()
            sub_dict = sub_dict[part]
    tr = LeftAligned()
    print(tr(kv_combined))


if __name__ == "__main__":
    def _tcb():
        from consul import Consul
        from sys import argv

        def consul_kvget_recurse(host, key=''):
            c = Consul(host=host)
            return c.kv.get(key=key, recurse=True)

        main(argv, consul_kvget_recurse)
    _tcb()
