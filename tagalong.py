#!/usr/bin/env python3
#
# Copyright (c) 2023 Death Inc.. All rights reserved.
#
# Author:
#       Julian Vetter <deathjest3r@web.de>
#
# SPDX-License-Identifier: BSD-3-Clause

import argparse
from pathlib import Path
import os
from tinydb import TinyDB, Query

def main():
    """
    main()
    """
    query = Query()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        dest="add_tag",
                        help="Add a tag to a file or folder",
                        type=str,
                        required=False)
    parser.add_argument("-d",
                        dest="del_tag",
                        help="Delete a tag from a file or folder",
                        type=str,
                        required=False)
    parser.add_argument("filename",
                        help="Operate on the given file or folder")
    args = parser.parse_args()

    tagalong_db_path = os.path.expanduser("~/.config/tagalong")
    if not os.path.exists(tagalong_db_path):
        os.mkdir(tagalong_db_path)
    tagalong_db = TinyDB("{:s}/tagalong_db.json".format(tagalong_db_path))

    folder = tagalong_db.get(query.folder == args.filename)

    if args.add_tag:
        # Get all unique elements from the taglist
        tag_list = list(set(args.add_tag.split(",")))
        if folder:
            tag_list = list(set(tag_list + folder["tags"]))
            tagalong_db.update({"tags" : tag_list}, query.folder == args.filename)
        else:
            tagalong_db.insert({"folder" : args.filename, "tags" : tag_list})
    elif args.del_tag:
        if folder:
            tag_list  = list(set(folder["tags"]) - set(args.del_tag.split(",")))
            if not len(tag_list):
                tagalong_db.remove(query.folder == args.filename)
            tagalong_db.update({"tags" : tag_list}, query.folder == args.filename)
    else:
        while(args.filename is not "/"):
            folder = tagalong_db.get(query.folder == args.filename)
            if folder and len(folder["tags"]):
                print(*folder["tags"], sep=", ")
                break
            path = Path(args.filename)
            args.filename = str(path.parent.absolute())
        if not folder:
            print("_")

if __name__ == "__main__":
    main()
