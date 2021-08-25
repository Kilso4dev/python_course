import sys
import os

def matches_one(template: str, *args: str) -> bool:
    for c in args:
        if template == c:
            return True
    return False

def split_whole_path(path: str) -> list[str]:
    splitted = []
    rest = path

    while True:
        rest, last = os.path.split(rest)
        
        if last != '':
            splitted.append(last)
        elif rest != '':
            splitted.append(rest)
            break
        else: # rest == '' and last == ''
            break

    splitted.reverse()
    return splitted

def find_common_root(p1: str, p2: str) -> tuple[str, str, str]:
    p1_sp = split_whole_path(p1)
    p1_len = len(p1_sp)
    p2_sp = split_whole_path(p2)
    p2_len = len(p2_sp)


    for i in range(0, min(p1_len, p2_len)):
        if p1_sp[i] != p2_sp[i]:
            return (
                    os.path.join(*p1_sp[:i]),
                    os.path.join(*p1_sp[i:]),
                    os.path.join(*p2_sp[i:])
                    )
    if p1_len == p2_len:
        return (p1, '', '')
    elif p1_len > p2_len:
        return (
                p2,
                os.path.join(*p1_sp[p2_len:]),
                os.path.join('')
                )
    else: # p1_len < p2_len
        return (
                p1,
                os.path.join(''),
                os.path.join(*p2_sp[p1_len:])
                )

def main():
    (common_path, exec_sub_path, c_dir_subpath) = find_common_root(sys.executable, __file__)
    #print((common_path, exec_sub_path, c_dir_subpath))

    exec_sub_path_split = split_whole_path(exec_sub_path)
    wanted = 'venv/bin/python'
    # add 3 postfix to wanted if existent in executable path
    if len(exec_sub_path_split) > 3 and exec_sub_path_split[2].endswith('3'):
        wanted += '3'
    wanted_split = split_whole_path(wanted)

    
    if not matches_one(common_path, '', '\\', '/') and \
            c_dir_subpath == '' and \
            len(wanted_split) == len(exec_sub_path_split) and \
            wanted_split[1] == exec_sub_path_split[1] and \
            wanted_split[2] == exec_sub_path_split[2]:

        print('Executable correct')
    else:
        print('Executable path not correct!')
        print(f'wanted executable: \n\t{os.path.join(common_path, wanted)}')
        print(f'found executable: \n\t{sys.executable}')

if __name__ == '__main__':
    main()
