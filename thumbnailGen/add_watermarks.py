import argparse, os

debug = False

def main():
    parser = argparse.ArgumentParser(description='Add watermarks to images in path')
    parser.add_argument('--root', help='Root path for images', required=True, type=str)
    parser.add_argument('--watermark', help='Path to watermark image', required=True, type=str)
    parser.add_argument('--name', help='Name addition for watermark', default="-watermark", type=str)
    parser.add_argument('--extension', help='Image extensions to look for', default=".jpg", type=str)
    parser.add_argument('--exclude', help='Path content to exclude', type=str)
    parser.add_argument('--targetRoot', help='Path for output dir ', type=str,required=True)

    args = parser.parse_args()

    files_processed = 0
    files_watermarked = 0
    for dirName, subdirList, fileList in os.walk(args.root):
        if args.exclude is not None and args.exclude in dirName:
            continue
        if debug: print('Walking directory: %s' % dirName)
        for fname in fileList:
            files_processed += 1
            if debug: print('  Processing %s' % os.path.join(dirName, fname))
            if args.extension in fname and args.watermark not in fname and args.name not in fname:
                ext = '.'.join(os.path.basename(fname).split('.')[1:])
                orig = os.path.join(dirName, fname)
                new_name = os.path.join(dirName, '%s.%s' % (os.path.basename(fname).split('.')[0] + args.name, ext))

                new_tgt = new_name.replace(args.root,args.targetRoot)
                new_tgtDir = os.path.dirname(new_tgt) 
                if not os.path.isdir(new_tgtDir):
                    os.makedirs(new_tgtDir, exist_ok=True)###

                if not os.path.exists(new_tgt):
                    files_watermarked += 1
                    print('    Convert %s to %s' % (orig, new_name))
                    os.system('composite -dissolve 10%% -gravity SouthEast -tile %s "%s" "%s"' % (args.watermark, orig, new_tgt))
    print("Files Processed: %s" % "{:,}".format(files_processed))
    print("Files Watermarked: %s" % "{:,}".format(files_watermarked))


if __name__ == '__main__':
    main()
