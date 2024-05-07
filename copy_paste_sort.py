import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    try:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                extension = os.path.splitext(file)[1][1:]  # Отримуємо розширення файлу без точки
                if extension == '':
                    extension = 'no_extension'  # Папка для файлів без розширення
                target_dir = os.path.join(dest_dir, extension)
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                
                shutil.copy(file_path, target_dir)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    default_source = '/Users/admin/Desktop/Documents'
    default_dest = '/Users/admin/Desktop/SortedFiles'

    parser = argparse.ArgumentParser(description='Copy files from one directory to another sorted by file extension.')
    parser.add_argument('source_dir', type=str, nargs='?', default=default_source, help='Path to the source directory.')
    parser.add_argument('dest_dir', type=str, nargs='?', default=default_dest, help='Path to the destination directory.')
    args = parser.parse_args()

    if not os.path.exists(args.source_dir):
        print("Source directory does not exist.")
        return
    
    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)
    
    copy_files(args.source_dir, args.dest_dir)
    print(f"All files have been copied from {args.source_dir} to {args.dest_dir}.")

if __name__ == '__main__':
    main()
