import os
import sys
import shutil

AudioBank_Index_Offset = 0x00C776C0
AudioBank_Index_Size = 0x000002A0
AudioBank_Offset = 0x00020700
AudioBank_Size = 0x000263F0
AudioTable_Index_Offset = 0x00C78380
AudioTable_Index_Size = 0x00000040
AudioTable_Offset = 0x00097F70
AudioTable_Size = 0x00548770

def main():
    if len(sys.argv) != 2:
        print("Usage: python mm_audiobin.py <Majoras Mask Decompressed Rom.z64>")
        sys.exit(1)
    
    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    tmp_directory = "tmp"
    parent_directory = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(parent_directory, tmp_directory)

    os.makedirs(path, mode=0o777, exist_ok=True)

    with open(input_file, 'rb') as rom:
        rom.seek(AudioBank_Index_Offset)
        Audiobank_Index = rom.read(AudioBank_Index_Size)
        file_name = "Audiobank_Index"
        file_path = os.path.join(tmp_directory, file_name)
        with open(file_path, "wb") as file:
            file.write(Audiobank_Index)

        rom.seek(AudioBank_Offset)
        Audiobank = rom.read(AudioBank_Size)
        file_name = "Audiobank"
        file_path = os.path.join(tmp_directory, file_name)
        with open(file_path, "wb") as file:
            file.write(Audiobank)

        rom.seek(AudioTable_Index_Offset)
        Audiotable_Index = rom.read(AudioTable_Index_Size)
        file_name = "Audiotable_Index"
        file_path = os.path.join(tmp_directory, file_name)
        with open(file_path, "wb") as file:
            file.write(Audiotable_Index)

        rom.seek(AudioTable_Offset)
        Audiotable = rom.read(AudioTable_Size)
        file_name = "Audiotable"
        file_path = os.path.join(tmp_directory, file_name)
        with open(file_path, "wb") as file:
            file.write(Audiotable)

        shutil.make_archive("MM", 'zip', tmp_directory)
        os.rename("MM.zip", "MM.audiobin")

        shutil.rmtree(tmp_directory)


        
        

if __name__ == "__main__":
    main()