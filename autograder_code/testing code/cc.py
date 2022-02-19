import os
import sys

if __name__ == '__main__':
    # cur_version = sys.version_info
    # print("{}".format(cur_version))

    output_file = 'op.txt'

    file_path = sys.argv[1]
    # print('first arg val: {}'.format(file_path))
    # state_2 = sys.argv[2]
    # print('{}'.format(state_2))

    # For python 2.7
    # fout = open(file_path, 'r')
    # val1 = fout.readline().rstrip('\n')
    # val2 = fout.readline()
    # fout.close()
    #
    # fout = open(output_file, 'w')
    # fout.write('{}\n'.format(val1))
    # fout.write('{}'.format(val2))
    # fout.close()

    # For python 3 testing
    with open(file_path, 'r') as fp:
        val1 = fp.readline().rstrip('\n')
        val2 = fp.readline()

    with open(output_file, 'w') as fp:
        fp.write(f"{val1}\n")
        fp.write(val2)

    # print('end')