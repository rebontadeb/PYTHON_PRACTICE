'''
move EP files in LINUX 
'''
import glob
import os
import shutil
from os import path

for file in glob.glob("*.pdf"):
    ep_version = file.split('_')[3]
    tarfile = file.split('_')[4].split('.')[0]
    tarpattern = '*'+tarfile+'*.tar.gz'
    src_file_pdf = path.realpath(file)
    head, tail = path.split(src_file_pdf)
    for tar in glob.glob(tarpattern):
        os.mkdir(ep_version)
        dest_file_pdf = head + '/' + ep_version + '/' + file
        src_file_tar = path.realpath(tar)
        head_t, tail_t = path.split(src_file_tar)
        dest_file_tar = head_t + '/' + ep_version + '/' + tail_t
        shutil.copy(src_file_pdf, dest_file_pdf)
        shutil.copy(src_file_tar, dest_file_tar)
