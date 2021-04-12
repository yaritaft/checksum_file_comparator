from os import listdir
from os.path import isfile, join
import hashlib

def generate_file_md5(rootdir, filename, blocksize=2**20):
    m = hashlib.md5()
    with open( join(rootdir, filename) , "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

def final_report():
    if (len(not_equal_files_in_checksum)==0):
        print("GREAAAT NO DIFFERENCES WERE FOUND AT ALL.")
    else:
        print("THE FOLLOWING FILES HAVE DIFFERENCES")
        for one_file in not_equal_files_in_checksum:
            print(f"File Name: {one_file} First Checksum: {first_dict[one_file]} Second Checksum: {second_dict[one_file]}")

def check_files_differences():
    """The idea is to check both directories at the same time. Every file that is present in both paths will be checksummed and compared."""
    for one_file in first_onlyfiles:
        if one_file in second_onlyfiles:
            print("File being processed: ", one_file)
            first_dict[one_file]=generate_file_md5(first_dir_url, one_file)
            second_dict[one_file]=generate_file_md5(second_dir_url, one_file)
            if (first_dict[one_file] != second_dict[one_file]):
                print("============DIFFERENCES FOUND=================")
                print(f"First checksum: {first_dict[one_file]}")
                print(f"Second checksum: {second_dict[one_file]}")
                not_equal_files_in_checksum.append(one_file)
                print("=============================")
            else:
                print(one_file, "SUCCESS. No differences.")


# first_dir_url = "/media/yari/CuatroTeras/Jujutsu no Kaisen"
first_dir_url = "/media/yari/My_Passport/Jujutsu no Kaisen"
second_dir_url = "/home/yari/Downloads/Jujutsu no Kaisen"
first_onlyfiles = [f for f in listdir(first_dir_url) if isfile(join(first_dir_url, f))]
second_onlyfiles = [f for f in listdir(second_dir_url) if isfile(join(second_dir_url, f))]
first_dict = {}
second_dict = {}
not_equal_files_in_checksum = []
check_files_differences()
final_report()