import os
import subprocess
import shutil
import argparse
from PyPDF2 import PdfMerger


# python3 printPDFs.py --sunday-only

# List of Sunday songs in the desired order.
sunday_songs = [
    "My Jesus",
    "Because He Lives",
    "Trust In God",
    "Blessed Redeemer"
]

# ----- Argument Parsing -----
parser = argparse.ArgumentParser(description="Generate onSong PDFs")
parser.add_argument("--sunday-only", action="store_true", help="Only process Sunday songs")
args = parser.parse_args()
sunday_only = args.sunday_only

# ----- Configuration -----
base_url = "http://127.0.0.1:5503/onSongViewer.html?file=/onSong/"
onsong_folder = "onSong"  # Path to your .onsong files
temp_pdf_folder = "temp_pdfs"
os.makedirs(temp_pdf_folder, exist_ok=True)

# When in sunday-only mode, we only output the Sunday merged PDFs.
if sunday_only:
    output_pdf_regular = "Sunday.pdf"
    output_pdf_capo = "Sunday-Capo.pdf"
else:
    output_pdf_regular = "Songs.pdf"
    output_pdf_capo = "Songs-Capo.pdf"

chrome_path = "google-chrome"  # Adjust for your OS/environment

# ----- Helper Function to Read Files with Fallback Encodings -----
def read_file_with_fallback(file_path):
    encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode file: {file_path}")

# ----- Get List of .onsong Files -----
if sunday_only:
    # Only process files whose base names match the Sunday songs list.
    onsong_files = sorted([
        f for f in os.listdir(onsong_folder)
        if f.endswith(".onsong") and os.path.splitext(f)[0] in sunday_songs
    ])
else:
    onsong_files = sorted([f for f in os.listdir(onsong_folder) if f.endswith(".onsong")])

# Lists for generated PDFs.
pdf_files_regular = []
pdf_files_capo = []

# For full processing, maintain Sunday mappings.
sunday_pdf_map_regular = {}
sunday_pdf_map_capo = {}

for file_name in onsong_files:
    file_url = base_url + file_name
    print(file_url)
    output_path_regular = os.path.join(temp_pdf_folder, file_name.replace(".onsong", ".pdf"))
    output_path_capo = os.path.join(temp_pdf_folder, file_name.replace(".onsong", "_capo.pdf"))
    
    # ----------------------------
    # Generate the regular PDF
    command_regular = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_path_regular}",
        file_url
    ]
    print(f"Generating regular PDF for: {file_name}")
    try:
        subprocess.run(command_regular, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating regular PDF for {file_name}: {e}")
        continue

    if os.path.exists(output_path_regular):
        pdf_files_regular.append(output_path_regular)
    else:
        print(f"Regular PDF file was not created for {file_name}")
    
    # ----------------------------
    # Extract Capo value from the onsong file.
    full_file_path = os.path.join(onsong_folder, file_name)
    capo_value = None
    try:
        content = read_file_with_fallback(full_file_path)
        for line in content.splitlines():
            if line.strip().startswith("Capo:"):
                parts = line.split("Capo:")
                if len(parts) > 1:
                    try:
                        capo_value = int(parts[1].strip())
                    except ValueError:
                        print(f"Invalid capo value in {file_name}. Defaulting to 0.")
                break
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
    if capo_value is None:
        capo_value = 0  # Default if not found
    
    # Append the transpose parameter for the capo version.
    file_url_capo = file_url + f"&transpose={capo_value}"
    
    # ----------------------------
    # Generate the Capo PDF
    command_capo = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_path_capo}",
        file_url_capo
    ]
    print(f"Generating capo PDF for: {file_name} (Capo: {capo_value})")
    try:
        subprocess.run(command_capo, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating capo PDF for {file_name}: {e}")
        continue

    if os.path.exists(output_path_capo):
        pdf_files_capo.append(output_path_capo)
    else:
        print(f"Capo PDF file was not created for {file_name}")
    
    # For full processing, build Sunday maps.
    if not sunday_only:
        song_title = os.path.splitext(file_name)[0]
        if song_title in sunday_songs:
            sunday_pdf_map_regular[song_title] = output_path_regular
            sunday_pdf_map_capo[song_title] = output_path_capo

# ----- Merging PDFs -----
if sunday_only:
    # In sunday-only mode, we only merge the PDFs we processed (which are all Sunday songs).
    if not pdf_files_regular:
        print("No Sunday regular PDFs were generated. Exiting.")
    else:
        # Order them according to the sunday_songs list.
        ordered_sunday_regular = []
        ordered_sunday_capo = []
        for song in sunday_songs:
            # Look for the file that matches the song title.
            for file_name in onsong_files:
                if os.path.splitext(file_name)[0] == song:
                    ordered_sunday_regular.append(
                        os.path.join(temp_pdf_folder, file_name.replace(".onsong", ".pdf"))
                    )
                    ordered_sunday_capo.append(
                        os.path.join(temp_pdf_folder, file_name.replace(".onsong", "_capo.pdf"))
                    )
        merger = PdfMerger()
        for pdf in ordered_sunday_regular:
            merger.append(pdf)
        merger.write(output_pdf_regular)
        merger.close()
        print(f"Combined Sunday regular PDF created successfully: {output_pdf_regular}")
        
        if not ordered_sunday_capo:
            print("No Sunday capo PDFs were generated. Exiting.")
        else:
            merger = PdfMerger()
            for pdf in ordered_sunday_capo:
                merger.append(pdf)
            merger.write(output_pdf_capo)
            merger.close()
            print(f"Combined Sunday Capo PDF created successfully: {output_pdf_capo}")
else:
    # Merge full set of PDFs.
    if not pdf_files_regular:
        print("No regular PDFs were generated. Exiting.")
    else:
        merger = PdfMerger()
        for pdf in pdf_files_regular:
            merger.append(pdf)
        merger.write(output_pdf_regular)
        merger.close()
        print(f"Combined PDF created successfully: {output_pdf_regular}")
    
    if not pdf_files_capo:
        print("No capo PDFs were generated. Exiting.")
    else:
        merger = PdfMerger()
        for pdf in pdf_files_capo:
            merger.append(pdf)
        merger.write(output_pdf_capo)
        merger.close()
        print(f"Combined PDF created successfully: {output_pdf_capo}")
    
    # Additionally, merge Sunday PDFs in the order defined by sunday_songs.
    ordered_sunday_regular = []
    ordered_sunday_capo = []
    for song in sunday_songs:
        if song in sunday_pdf_map_regular:
            ordered_sunday_regular.append(sunday_pdf_map_regular[song])
        else:
            print(f"Warning: Sunday song '{song}' not found among generated PDFs.")
        if song in sunday_pdf_map_capo:
            ordered_sunday_capo.append(sunday_pdf_map_capo[song])
        else:
            print(f"Warning: Sunday song '{song}' not found among generated capo PDFs.")
    
    if ordered_sunday_regular:
        merger = PdfMerger()
        for pdf in ordered_sunday_regular:
            merger.append(pdf)
        merger.write("Sunday.pdf")
        merger.close()
        print("Combined Sunday PDF created successfully: Sunday.pdf")
    
    if ordered_sunday_capo:
        merger = PdfMerger()
        for pdf in ordered_sunday_capo:
            merger.append(pdf)
        merger.write("Sunday-Capo.pdf")
        merger.close()
        print("Combined Sunday Capo PDF created successfully: Sunday-Capo.pdf")

# ----- Delete the Temporary PDF Folder -----
try:
    shutil.rmtree(temp_pdf_folder)
    print(f"Temporary folder '{temp_pdf_folder}' has been removed.")
except Exception as e:
    print(f"Error removing temporary folder '{temp_pdf_folder}': {e}")
